# sqlalchemy-challenge

Want to go on vacation in Honolulu, Hawaii? I have done all the climate analysis to help with your trip planning!

##
## Part 1 - Climate Analysis and Exploration

I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database.
* I used SQLAlchemy `create_engine` to connect to the sqlite database.  I then used SQLAlchemy's `automap_base()` to reflect the tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Query to retrieve the last 12 months of precipitation data (date and percipitation values)
* Loaded the results into a Pandas DataFrame sorted by the date.
* Plotted the results using the DataFrame `plot` method.
* Used Pandas to print the summary statistics for the precipitation data.

<img src="https://github.com/kelseyoros/sqlalchemy-challenge/blob/master/images/YearPrcpBarChart.JPG" width="600">


### Station Analysis

* Query to calculate the total number of stations.
* Query to find the most active stations.
  * Listed the stations and observation counts in descending order.
* Query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filtered by the station with the highest number of observations.
  * Plotted the results as a histogram with `bins=12`.

<img src="https://github.com/kelseyoros/sqlalchemy-challenge/blob/master/images/NumTOBSHist.JPG" width="600">

##
## Part 2 - Climate App

With the completed analysis, I designed a Flask API based on the queries mentioned above.

### Flask Routes

* `/`
  * Home page.
  * Lists all routes that are available.

* `/api/v1.0/precipitation`
  * Converted the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`
  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When given the start only, it calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
  * When given the start and the end date, it calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
