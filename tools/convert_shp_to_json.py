import sys

if len(sys.argv) != 3:
    print("Usage: python convert_shp_to_json.py SHAPE_FILE OUT_FILE")
    exit(2)

print("Importing modules...")
import geopandas as gpd

print("Reading file...")
gdf = gpd.read_file(sys.argv[1])

print("Writing to file...")
jsonfile = gdf.to_json()
with open(sys.argv[2], "w+") as f:
    f.write(jsonfile)

print("Done !")
