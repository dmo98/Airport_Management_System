from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL

import mysql.connector as mysql

#import MySQLdb.cursors
#import re

app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'AMS_v3'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


"""
@app.route('/')
def index():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM airport")
    results = cursor.fetchall()
    print(results)
    return results[0]['airport_name']
"""

"""
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST" and request.form['btn'] == 'Manager Login':
        details = request.form
        airport = details['airport']
        ssn = details['ssn']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM airport WHERE airport.airport_name = (%s) AND airport.gm_ssn = (%s)", [airport, ssn])
        data = cursor.fetchall()

        print('CYCYCY', url_for('login'), data)

        if data == ((1,),):
            return render_template('login.html', message=(('Log In Successful!',),))
        elif data == ((0,),):
            return render_template('login.html', message=(('Please enter the correct login information.',),))

"""


@app.route('/', methods=['GET', 'POST'])
def login():
    print('here')

    if request.method == "POST" and request.form['btn'] == 'Manager Login':
        details = request.form
        airport = details['airport']
        ssn = details['ssn']
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM airport WHERE airport.airport_name = (%s) AND airport.gm_ssn = (%s)", [airport, ssn])
        data = cur.fetchall()

        print('CYCYCY', url_for('login'), data)

        if data == ((1,),):
            cur.execute("SELECT employee.Fname, employee.M, employee.Lname FROM employee WHERE employee.ssn = (%s)", [ssn])
            data = cur.fetchall()
            print(data)
            fname, m, lname = str(data[0][0]), str(data[0][1]), str(data[0][2])
            print('Identity Verified: Welcome General Manager {} {} {}'.format(fname, m, lname))
            #return render_template('login.html', message='Identity Verified: Welcome General Manager {} {} {}'.format(fname, m, lname))
            return redirect(url_for('index'))
        elif data == ((0,),):
            return render_template('login.html', message='Please enter the correct login information.')

    return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    data = 'Empty'

    if request.method == "POST" and request.form['btn'] == "Get Manager's Info":
        details = request.form
        airport = details['airport']
        cur = mysql.connection.cursor()
        if airport == 'All Airports':
            query = """
            SELECT employee.Fname, employee.M, employee.Lname, employee.phone_number, airport.airport_name
            FROM employee
            JOIN airport
            ON employee.ssn = airport.gm_ssn
            """
            cur.execute(query)
        else:
            query = """
            SELECT employee.Fname, employee.M, employee.Lname, employee.phone_number, airport.airport_name
            FROM employee
            JOIN airport
            ON employee.ssn = airport.gm_ssn
            WHERE airport.airport_name = (%s)
            """
            cur.execute(query, [airport])
        data = cur.fetchall()
        print(data)
        return render_template('index.html', manager_info=data)

    if request.method == "POST" and request.form['btn'] == "Get Average Crew Experience On A Route":
        details = request.form
        d_airport = details['d_airport']
        a_airport = details['a_airport']
        cur = mysql.connection.cursor()

        if d_airport == 'All Airports' and a_airport == 'All Airports':
            query = """
            SELECT flight.d_airport, flight.a_airport, flight_crew.jobtype, AVG(flight_crew.yrs_exp)
            FROM flight
            INNER JOIN crew 
            ON flight.flightID = crew.flightID
            INNER JOIN flight_crew
            ON crew.passport_number = flight_crew.passport_number
            WHERE flight.d_airport IN (
                SELECT DISTINCT flight.d_airport
                FROM flight
            ) AND flight.a_airport IN (
                SELECT DISTINCT flight.a_airport
                FROM flight
            ) AND flight.d_airport <> flight.a_airport
            GROUP BY flight.d_airport, flight.a_airport, flight_crew.jobtype
            """
            cur.execute(query)
        else:
            query = """
            SELECT flight.d_airport, flight.a_airport, flight_crew.jobtype, AVG(flight_crew.yrs_exp)
            FROM flight
            INNER JOIN crew 
            ON flight.flightID = crew.flightID
            INNER JOIN flight_crew
            ON crew.passport_number = flight_crew.passport_number
            WHERE flight.d_airport = (%s) AND flight.a_airport = (%s)
            GROUP BY flight_crew.jobtype
            """
            cur.execute(query, [d_airport, a_airport])
        data = cur.fetchall()
        print(data)
        return render_template('index.html', crew_experience=data)

    if request.method == "POST" and request.form['btn'] == "Get Flights where this Aircraft was used":
        details = request.form
        sno = details['aircraft_sno']
        cur = mysql.connection.cursor()

        if True:
            query = """
            SELECT flight.flightID, flight.d_airport, flight.a_airport
            FROM flight 
            WHERE flight.aircraft_sno = (%s)
            """
            cur.execute(query, [sno])

        data = cur.fetchall()
        print(data)
        return render_template('index.html', aircraft_flights=data)

    if request.method == "POST" and request.form['btn'] == "Get Flights where this Aircraft Model was used":
        details = request.form
        model = details['aircraft_model']
        cur = mysql.connection.cursor()

        if True:
            query = """
            SELECT flight.flightID, flight.d_airport, flight.a_airport
            FROM flight 
            JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            WHERE aircraft.model = (%s)
            """
            cur.execute(query, [model])

        data = cur.fetchall()
        print(data)
        return render_template('index.html', aircraft_model_flights=data)

    if request.method == "POST" and request.form['btn'] == "Get Flights Departing From or Arriving At this Airport":
        details = request.form
        airport = details['airport']
        cur = mysql.connection.cursor()

        if True:
            query = """
            SELECT flight.flightID, flight.airline, flight.d_airport, flight.d_gate, flight.d_time, flight.a_airport, flight.a_gate, flight.a_time, aircraft.model
            FROM flight 
            JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            WHERE flight.d_airport = (%s) OR flight.a_airport = (%s)
            ORDER BY flight.a_airport, flight.d_time
            """
            cur.execute(query, [airport, airport])

        data = cur.fetchall()
        print(data)
        return render_template('index.html', airport_flights=data)

    if request.method == "POST" and request.form['btn'] == "Get Aircraft used for Flights Arriving At this Airport and Hangars they were kept in":
        details = request.form
        d_airport = details['d_airport']
        a_airport = details['a_airport']
        cur = mysql.connection.cursor()

        if d_airport == 'All Airports':
            query = """
            SELECT flight.d_airport, flight.a_airport, flight.aircraft_sno, flight.airline, aircraft.model, undergoes_maintenance.hangarID
            FROM flight 
            INNER JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            INNER JOIN undergoes_maintenance
            ON undergoes_maintenance.airport_name = flight.a_airport AND undergoes_maintenance.hangarID IN (
                SELECT hangar.hangarID
                FROM hangar
                WHERE hangar.airport_name = "John F. Kennedy International Airport"
            ) AND undergoes_maintenance.aircraft_sno = flight.aircraft_sno
            WHERE flight.a_airport = (%s)
            """
            cur.execute(query, [a_airport])
        else:
            query = """
            SELECT flight.d_airport, flight.a_airport, flight.aircraft_sno, flight.airline, aircraft.model, undergoes_maintenance.hangarID
            FROM flight 
            INNER JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            INNER JOIN undergoes_maintenance
            ON undergoes_maintenance.airport_name = flight.a_airport AND undergoes_maintenance.hangarID IN (
                SELECT hangar.hangarID
                FROM hangar
                WHERE hangar.airport_name = "John F. Kennedy International Airport"
            ) AND undergoes_maintenance.aircraft_sno = flight.aircraft_sno
            WHERE flight.d_airport = (%s) AND flight.a_airport = (%s)
            """
            cur.execute(query, [d_airport, a_airport])
        data = cur.fetchall()
        print(data)
        return render_template('index.html', aircrafts_and_hangars=data)

    if request.method == "POST" and request.form['btn'] == "Get Engineer's Phone Number and Hangar Location":
        details = request.form
        flightID = details['flightID']
        cur = mysql.connection.cursor()

        if True:
            query = """
            SELECT employee.phone_number, hangar.hangarID, hangar.location
            FROM flight 
            INNER JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            INNER JOIN aircraft_model
            ON aircraft.model = aircraft_model.model
            INNER JOIN specialize_in
            ON aircraft_model.model = specialize_in.model
            INNER JOIN employee
            ON specialize_in.emp_ssn = employee.ssn
            INNER JOIN works_at
            ON works_at.airport_name = flight.a_airport AND works_at.hangarID IN (
                SELECT hangar.hangarID
                FROM hangar
                WHERE hangar.airport_name = flight.a_airport
            ) AND works_at.emp_ssn = employee.ssn
            INNER JOIN hangar
            ON works_at.airport_name = hangar.airport_name AND works_at.hangarID = hangar.hangarID
            WHERE flight.flightID = (%s) AND employee.airport = flight.a_airport;
            """
            cur.execute(query, [flightID])

        data = cur.fetchall()
        print(data)
        return render_template('index.html', emp_phonenum_and_hangar=data)

    if request.method == "POST" and request.form['btn'] == "List Aircraft that haven't undergone maintenance since":
        details = request.form
        last_maintenance_date = details['date']
        cur = mysql.connection.cursor()

        if True:
            query = """
            SELECT DISTINCT undergoes_maintenance.aircraft_sno, undergoes_maintenance.date
            FROM undergoes_maintenance
            WHERE undergoes_maintenance.date IN (
                SELECT MAX(undergoes_maintenance.date)
                FROM undergoes_maintenance
                GROUP BY undergoes_maintenance.aircraft_sno
            ) AND undergoes_maintenance.date < (%s)
            ORDER BY undergoes_maintenance.aircraft_sno
            """
            cur.execute(query, [last_maintenance_date])

        data = cur.fetchall()
        print(data)
        return render_template('index.html', aircraft_maintenance=data)

    if request.method == "POST" and request.form['btn'] == "Go to Retrieval Page":
        return redirect(url_for('retrieval'))
    return render_template('index.html')


@app.route('/retrieval', methods=['GET', 'POST'])
def retrieval():
    data = 'Empty'
    if request.method == "POST" and request.form['btn'] == "Get Average Employee Salary":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT employee.airport, employee.jobtype, AVG(employee.salary)
            FROM employee
            GROUP BY employee.airport, employee.jobtype
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', employee_salary=data)

    if request.method == "POST" and request.form['btn'] == "Get Average Crew Experience":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT crew.flightID, AVG(flight_crew.yrs_exp)
            FROM crew 
            JOIN flight_crew
            ON crew.passport_number = flight_crew.passport_number
            GROUP BY crew.flightID
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', crew_experience=data)

    if request.method == "POST" and request.form['btn'] == "Get Last Flight and Maintenance":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT aircraft.sno, aircraft.model, flight.flightID, flight.d_time, MAX(undergoes_maintenance.date), undergoes_maintenance.maintenance_type
            FROM aircraft
            JOIN flight
            ON aircraft.sno = flight.aircraft_sno
            INNER JOIN undergoes_maintenance
            ON airport_name IN (
                SELECT DISTINCT flight.d_airport
                FROM flight
            ) AND hangarID IN (
                SELECT DISTINCT hangar.hangarID
                FROM hangar
            ) AND undergoes_maintenance.aircraft_sno = flight.aircraft_sno
            WHERE flight.a_time IN (
                SELECT MAX(flight.a_time)
                FROM flight
                JOIN aircraft
                ON aircraft.sno = flight.aircraft_sno
                GROUP BY aircraft.sno
            )
            GROUP BY aircraft.sno
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', aircraft_flight_and_maintenance=data)

    if request.method == "POST" and request.form['btn'] == "Get Most Common Aircraft Models":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT aircraft_model.manufacturer AS Manufacturer, aircraft_model.model AS Model, COUNT(*) AS Number_of_flights
            FROM aircraft_model
            INNER JOIN aircraft
            ON aircraft.model = aircraft_model.model
            INNER JOIN flight
            ON aircraft.sno = flight.aircraft_sno
            GROUP BY aircraft_model.model
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', common_aircraft_models=data)

    if request.method == "POST" and request.form['btn'] == "Get count of flights per day by airline":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT CAST(flight.d_time AS DATE), flight.airline, COUNT(*)
            FROM flight
            GROUP BY CAST(flight.d_time AS DATE), flight.airline
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', flights_count_airline=data)

    if request.method == "POST" and request.form['btn'] == "Get count of flights per day by aircraft model":
        cur = mysql.connection.cursor()
        if True:
            query = """
            SELECT CAST(flight.d_time AS DATE), aircraft.model, COUNT(*)
            FROM flight
            INNER JOIN aircraft
            ON flight.aircraft_sno = aircraft.sno
            GROUP BY CAST(flight.d_time AS DATE), aircraft.model
            """
            cur.execute(query)

        data = cur.fetchall()
        print(data)
        return render_template('retrieval.html', flights_count_aircraft_model=data)

    if request.method == "POST" and request.form['btn'] == "Go to Retrieval Page":
        return redirect(url_for('retrieval'))
    return render_template('retrieval.html')


if __name__ == "__main__":
    app.run(debug=True)
