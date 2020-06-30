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

<img src="https://github.com/kelseyoros/sqlalchemy-challenge/blob/master/images/YearPrcpBarChart.JPG" width="800">


### Station Analysis

* Query to calculate the total number of stations.
* Query to find the most active stations.
  * Listed the stations and observation counts in descending order.
* Query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filtered by the station with the highest number of observations.
  * Plotted the results as a histogram with `bins=12`.

<img src="https://github.com/kelseyoros/sqlalchemy-challenge/blob/master/images/NumTOBSHist.JPG" width="800">

