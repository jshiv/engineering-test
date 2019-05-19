import geopandas as gpd
import pandas as pd
import psycopg2 
import config
from functools import lru_cache
import requests
import shutil

@lru_cache(maxsize=128)
def get_image_url(id_str):
    sql = """SELECT id, image_url FROM properties WHERE properties.id = '{id_str}';"""
    con = psycopg2.connect(database=config.DATABASE,user=config.USER, password=config.PASSWORD, host=config.HOST, port=config.PORT)
    image_url = pd.read_sql(sql.format(id_str=id_str), con).image_url.tolist()[0]
    return image_url

@lru_cache(maxsize=128)
def get_ids():
    sql = 'SELECT id FROM properties;'
    con = psycopg2.connect(database=config.DATABASE,user=config.USER, password=config.PASSWORD, host=config.HOST, port=config.PORT)
    id_list = pd.read_sql(sql, con).id.tolist()
    return id_list

@lru_cache(maxsize=128)
def download_image(image_url, path = './images/file.image'):
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)   

@lru_cache(maxsize=128)
def get_ids_within_distance(geojson, distance):
    con = psycopg2.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD, host=config.HOST, port=config.PORT)
    sql = """
    SELECT id,
        image_url,
        geocode_geo
    FROM properties
    WHERE ST_Distance(ST_GeomFromGeoJSON('{geojson}'), geocode_geo) <= {distance};
    """.format(geojson=geojson, distance=distance)
    df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col='geocode_geo' )
    return df.id.tolist()

def get_geo_stats(id_list, distance):
    id_str = ', '.join(["'{}'".format(_id) for _id in id_list])
    sql = """
    SELECT 
        id,
        geocode_geo,
        ST_Area(parcel_geo) As parcel_area,
        ST_Area(building_geo) As building_area,
        ST_Distance(geocode_geo, ST_Centroid(building_geo)) AS building_distance_to_center,
        ST_Area(building_geo)/ST_Area(ST_Buffer(geocode_geo, {distance})) AS zone_density
    FROM properties 
        WHERE id in ({id_str})
    ;""".format(id_str=id_str, distance=distance)
    con = psycopg2.connect(database=config.DATABASE, user=config.USER, password=config.PASSWORD, host=config.HOST, port=config.PORT)
    df = gpd.GeoDataFrame.from_postgis(sql, con, geom_col='geocode_geo' )
    stats = df[['id', 'parcel_area', 'building_area',
        'building_distance_to_center', 'zone_density']].to_dict('records')
    return stats


if __name__=='__main__':
    print(get_ids())
    print(get_image_url('f853874999424ad2a5b6f37af6b56610'))
    # download_image(
    #     image_url = 'https://storage.googleapis.com/engineering-test/images/f853874999424ad2a5b6f37af6b56610.tif',
    #     path = './images/f853874999424ad2a5b6f37af6b56610')
    print(get_ids_within_distance('{"type": "Point", "coordinates": [-73.748751, 40.9185483]}', 100))
    print(get_geo_stats(id_list = ['f1650f2a99824f349643ad234abff6a2','f853874999424ad2a5b6f37af6b56610'],
                        distance = 100))