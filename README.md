# Sault-Ste.-Marie-Stores-n-Malls
This is a Python flask web app that displays the various grocery stores and shopping malls on a map using Folium. The web app also includes a search function to allow the user to find a specific store or mall 
<img width="1552" alt="Screen Shot 2023-02-27 at 11 59 33 PM" src="https://user-images.githubusercontent.com/105472843/221758545-1c86bfc8-77eb-46bc-97f3-97e8eb16955e.png">
<img width="1552" alt="Screen Shot 2023-02-28 at 12 00 03 AM" src="https://user-images.githubusercontent.com/105472843/221758650-7f93040a-8d5a-4a51-9a28-de4cfa41da4e.png">
<img width="1552" alt="Screen Shot 2023-02-28 at 12 00 12 AM" src="https://user-images.githubusercontent.com/105472843/221758662-263fcac9-800f-4c24-9d6e-fd40c675c122.png">


## How does it work?
The web app will read the CSV files containing names and location of each store/mall as a dataframe which in turn is converted into GeoJSON data. This data is then represented on the map as location points using Folium

## Acknowledgement
Thanks to Geoff Boeing (https://github.com/gboeing) for this amazing Dataframe to GeoJSON converter function

https://geoffboeing.com/2015/10/exporting-python-data-geojson/
