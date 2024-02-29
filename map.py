import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# Given bounding box coordinates for Maharashtra
latitude_north = 21.3869
latitude_south = 15.6025
longitude_east = 80.8586
longitude_west = 72.6597

# Create a GeoDataFrame with a polygon representing the bounding box
geometry = Polygon(
    [
        (longitude_west, latitude_north),
        (longitude_east, latitude_north),
        (longitude_east, latitude_south),
        (longitude_west, latitude_south),
    ]
)
gdf = gpd.GeoDataFrame(geometry=[geometry])

# World map data from GeoPandas
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Plot the world map
ax = world.plot(figsize=(10, 6), color="lightgray")

# Plot the bounding box
gdf.plot(ax=ax, color="red", alpha=0.5)

# Set plot title
plt.title("Bounding Box of Maharashtra on World Map")

# Show the plot
plt.show()
