# World_Weather_Analysis 
Using Jupyter Notebook, CityPy API, Google's APIs, Pandas, Python and Numpy to create weather database and map visualization for vacation search and vacation itinerary 

## Create Weather Database
Being able to create city data using the CityPy API, was incredibly fast. 
When I think about how long this would have taken to just find the cities, I can see the maps, tools surrounding me. Up on the wall I see the minute and hour hands turn. The days turn into weeks; and finally, between the third and fourth week, I am done. I am totally exhausted.  

### City Database: 
![](Images/CityDatabase.png)

## Create Vacation Search
Here an input minimum and maximum temperatures were used to find all the locations around the  world whose temperature was between these temperatures. After that, using Google’s 
NearBySearch API, we listed hotels within 5000 meters from the locations and created a map. 

### Here’s the map created: 
![](Images/WeatherPy_vacation_map.png)

## Create Vacation Itinerary
From the lasts map, we pick 4 locations. Then, using Google’s Directions API, mapped a route that would take us from one city to the next and then back to the origin location. 

### Here are the cities picked: 
![](Images/WeatherPy_travel_map_markers.png)

### Here are the city's route:
![](Images/WeatherPy_travel_map.png)
