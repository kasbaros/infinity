import folium
import pandas as pd
import os

regions = os.path.join("./static/data", "15_Statistical_Regions.geojson")
education_regions = os.path.join("./static/data", "education_data.csv")
education_data = pd.read_csv(education_regions)

m = folium.Map(
    location=[0.347596, 32.582520],
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ",
    zoom_start=7,
)

tiles = ["stamenwatercolor", "cartodbpositron", "openstreetmap", "stamenterrain"]
for tile in tiles:
    folium.TileLayer(tile).add_to(m)

choropleth = folium.Choropleth(
    geo_data=regions,
    name="Choropleth",
    data=education_data,
    columns=["Geography", "2017 Male", "2017 Female"],
    key_on="feature.properties.F15Regions",
    fill_color="PuBuGn",
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name="Education among Genders %",
).add_to(m)

folium.LayerControl().add_to(m)
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(["F15Regions"], labels=False)
)

m.save("./templates/maps/education_map.html")

