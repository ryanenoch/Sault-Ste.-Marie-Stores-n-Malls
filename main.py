#Flask web app to plot locations of various grocery stores and shopping malls using Folium

from flask import Flask

app = Flask(__name__)


@app.route('/')
def sault():
    import folium
    from folium import plugins
    import pandas as pd
    import json

    #names of csv files (same filenames will be used later while making GeoJson Files )
    file1 = 'ssmstores'
    file2 = 'ssmmalls'
    #name for the main GeoJson file (to be created later)
    filemain = 'SSM'

    #dataframes
    df1 = pd.read_csv(f'{file1}.csv')
    df2 = pd.read_csv(f'{file2}.csv')
    #concatenating dataframes using append()
    dfmain = df1.append(df2)

    #view the dataset
    print(df1.head())
    print()
    print(df2.head())
    print()
    print(dfmain)
    print()

    #Dataframe to GeoJSON converter function by Geoff Boeing
    #https://geoffboeing.com/2015/10/exporting-python-data-geojson/
    def df_to_geojson(df, properties, lat='lat', lon='lng'):
        geojson = {'type': 'FeatureCollection', 'features': []}
        for _, row in df.iterrows():
            feature = {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                    'type': 'Point',
                    'coordinates': []
                }
            }
            feature['geometry']['coordinates'] = [row[lon], row[lat]]
            for prop in properties:
                feature['properties'][prop] = row[prop]
            geojson['features'].append(feature)
        return geojson

    cols = ['name', 'address']  #select columns other than lat and long
    geojson1 = df_to_geojson(df1, cols)  #passing df & columns to function
    geojson2 = df_to_geojson(df2, cols)
    geojson_main = df_to_geojson(dfmain, cols)

    #dumping GeoJSONs into separate files(optional)
    output_filename = f'{file1}.js'
    with open(output_filename, 'w') as output_file:
        output_file.write('var dataset = ')
        json.dump(geojson1, output_file, indent=2)

    output_filename = f'{file2}.js'
    with open(output_filename, 'w') as output_file:
        output_file.write('var dataset = ')
        json.dump(geojson2, output_file, indent=2)

    output_filename = f'{filemain}.js'
    with open(output_filename, 'w') as output_file:
        output_file.write('var dataset = ')
        json.dump(geojson_main, output_file, indent=2)

    center = [46.5277912, -84.3306842]
    map_ssm = folium.Map(location=center, zoom_start=14)
    title_html = '''
                 <h3 align="center" style="font-size:20px; margin-top:0px"><b>Sault Ste. Marie Stores n' Malls</b></h3>
                 '''
    map_ssm.get_root().html.add_child(folium.Element(title_html))
  
    #setting up different icons & color for stores & malls
    #Link for icons - https://fontawesome.com/v4/
    store_marker = folium.Marker(
        icon=folium.Icon(icon='fa-shopping-cart', prefix='fa', color='blue'))
    mall_marker = folium.Marker(
        icon=folium.Icon(icon='fa-shopping-bag', prefix='fa', color='red'))

    #create GeoJSON objects from each GeoJSON file
    store_obj = folium.GeoJson(
        geojson1,
        name="Grocery Stores",
        marker=store_marker,
        tooltip=folium.GeoJsonTooltip(fields=["name", "address"],
                                      aliases=["Name", "Address"],
                                      localize=True),
    ).add_to(map_ssm)

    mall_obj = folium.GeoJson(
        geojson2,
        name="Shopping Malls",
        marker=mall_marker,
        tooltip=folium.GeoJsonTooltip(fields=["name", "address"],
                                      aliases=["Name", "Address"],
                                      localize=True),
    ).add_to(map_ssm)

    main_obj = folium.GeoJson(
        geojson_main,
        name="",
        show=False,  #to hide the markers by default
        tooltip=folium.GeoJsonTooltip(fields=["name", "address"],
                                      aliases=["Name", "Address"],
                                      localize=True),
    ).add_to(map_ssm)

    #User can search for malls & stores within the main GeoJSON object using Search()
    main_search = plugins.Search(
        layer=main_obj,
        geom_type='Point',
        placeholder="Search for stores & malls",
        collapsed=True,
        search_label='name'  #search_label is the column you want to search for
    ).add_to(map_ssm)

    #This enables user to hide/unhide each category
    folium.LayerControl().add_to(map_ssm)

    #save map to html file
    #map_sault.save('ssm.html')

    return map_ssm._repr_html_()


app.run(host='0.0.0.0', port=8080)
