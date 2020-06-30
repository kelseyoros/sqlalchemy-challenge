# sqlalchemy-challenge

Want to go on vacation in Honolulu, Hawaii? I have done all the climate analysis to help with your trip planning!

##
## Step 1 - Climate Analysis and Exploration

I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database.
* I used SQLAlchemy `create_engine` to connect to the sqlite database.
* I used SQLAlchemy `automap_base()` to reflect the tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

I designed a query to retrieve the last 12 months of precipitation data (date and percipitation values) and loaded the results into a Pandas DataFrame sorted by the date.


* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Which station has the highest number of observations?

  * Hint: You may need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)
