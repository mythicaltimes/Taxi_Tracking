# Taxi_Tracking
Use gmaps API to track the location of taxi's with information from the NY Taxi company.

The original goal of the program is to load the taxi dataset and determine the total time that a taxi was in service, 
along with the number of times it stopped at a specific location. 

Information needed to attain our results is:
* Original tutorial: https://jupyter-gmaps.readthedocs.io/en/latest/tutorial.html#base-maps
* Taxi Data: https://data.cityofnewyork.us/Transportation/2018-Yellow-Taxi-Trip-Data/t29m-gskq
  * VendorID
  * tpep-pickup_datetime
  * tpep_dropoff_datetime
  * PULOcationID
  * DOLocationID

With this information we can determine which taxi made the specific dropoffs to different locations throughout the day.
The known obstacle to overcome is gmaps limit on API requests without being charged. At this time, the dataset is 112 million rows.
