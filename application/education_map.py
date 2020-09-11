import folium
import pandas as pd
import os

regions = os.path.join("./static/data", "uganda_subregion_boundaries.geojson")
education_regions = os.path.join("./static/data", "education_data.csv")
education_data = pd.read_csv(education_regions)

m = folium.Map(location=[0.347596, 32.582520], zoom_start=7)

folium.Choropleth(
    geo_data=regions,
    name="Choropleth",
    data=education_data,
    columns=["Geography", "2017 Male", "2017 Female"],
    key_on="feature.properties.SUB_REGION",
    fill_color="BuPu",
    fill_opacity=0.6,
    line_opacity=0.2,
    legend_name="Education among Genders %",
).add_to(m)

# folium.LayerControl().add_to(m)
m.save("./templates/maps/education_map.html")

