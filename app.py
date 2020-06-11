# import dependencies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# DATABASE SETUP
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# FLASK SETUP
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    """List all routes that are available"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yyyy-mm-dd<br/>"
        f"/api/v1.0/yyyy-mm-dd/yyyy-mm-dd<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a dictionary using date as the key and prcp as the value"""
    session = Session(engine)
    sel = [Measurement.date,Measurement.prcp]
    result = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)


@app.route('/api/v1.0/stations')
def stations():
    """Return a JSON list of stations from the dataset."""
    session = Session(engine)
    sel = [Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation]
    result = session.query(*sel).all()
    session.close()

    stations = []
    for station,name,latitude,longitude,elevation in result:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = latitude
        station_dict["Lon"] = longitude
        station_dict["Elevation"] = elevation
        stations.append(station_dict)

    return jsonify(stations)


@app.route('/api/v1.0/tobs')
def tobs():
    """Query the dates and temperature observations of the most active station for the last year of data.
    Return a JSON list of temperature observations (TOBS) for the previous year."""
    session = Session(engine)
    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = (dt.datetime.strptime(end_date[0],'%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')
    sel= [Measurement.station,Measurement.date,Measurement.tobs]
    result = session.query(*sel).filter(Measurement.station=='USC00519281').filter(Measurement.date >= year_ago).all()
    session.close()

    tobs = []
    for station, date, temperature in result:
        tobs_dict = {}
        tobs_dict["Station"] = station
        tobs_dict["Date"] = date
        tobs_dict["Temperature"] = temperature
        tobs.append(tobs_dict)
    return jsonify(tobs)


@app.route('/api/v1.0/<date>')
def start(date):
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date
    Return a JSON list of the minimum temperature, the average temperature, and the max temperature"""
    session = Session(engine)
    result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                filter(Measurement.date >= date).all()
    session.close()

    temperatures = []
    for minimum, maximum, average in result:
        temperature_dict = {}
        temperature_dict['Lowest Temperature'] = minimum
        temperature_dict['Highest Temperature'] = maximum
        temperature_dict['Average Temperature'] = average
        temperatures.append(temperature_dict)
        print(temperature_dict)

    return jsonify(temperatures)


@app.route('/api/v1.0/<start_date>/<end_date>')
def start_end(start_date,end_date):
    session = Session(engine)
    result = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
                filter(Measurement.date >= start_date, Measurement.date <= end_date).all()
    session.close()

    temperatures = []
    for minimum, maximum, average in result:
        temperature_dict = {}
        temperature_dict['Lowest Temperature'] = minimum
        temperature_dict['Highest Temperature'] = maximum
        temperature_dict['Average Temperature'] = average
        temperatures.append(temperature_dict)

    return jsonify(temperatures)


if __name__ == "__main__":
    app.run(debug=True)
