# Sault-Ste.-Marie-Stores-n-Malls
This is a Python flask web app that displays the various grocery stores and shopping malls on a map using Folium. The web app also includes a search function to allow the user to find a specific store or mall 

## How does it work?
The web app will read the CSV files containing names and location of each store/mall as a dataframe which in turn is converted into GeoJSON data. This data is then represented on the map as location points using Folium

## Acknowledgement
Thanks to Geoff Boeing (https://github.com/gboeing) for this amazing Dataframe to GeoJSON converter function

https://geoffboeing.com/2015/10/exporting-python-data-geojson/
