from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.kml import Kml
from src.route import LonLat, Route
import json
# import sys
# print(sys.path)

app = FastAPI()

origins = [
    "http://106.172.29.214:80",
    "http://106.172.29.214",
    "https://106.172.29.214",
    "https://106.172.29.214/",
    "http://localhost",
    "https://d2xmjga6x6xkar.cloudfront.net/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/locations")
async def get_placemarks():
    filepaths = []
    filepaths.append(r"data/aed_aoba_20221223.kml")
    filepaths.append(r"data/aed_izumi_20221223.kml")
    filepaths.append(r"data/aed_miyagino_20221223.kml")
    filepaths.append(r"data/aed_taihaku_20221223.kml")
    filepaths.append(r"data/aed_wakabayashi_20221223.kml")
    kml = Kml(filepaths)
    placemarks = kml.generate_placemarks()
    return placemarks

@app.get("/closest")
async def get_closest_placemarks(longitude: float = 0, latitude: float = 0):
    filepaths = []
    filepaths.append(r"data/aed_aoba_20221223.kml")
    filepaths.append(r"data/aed_izumi_20221223.kml")
    filepaths.append(r"data/aed_miyagino_20221223.kml")
    filepaths.append(r"data/aed_taihaku_20221223.kml")
    filepaths.append(r"data/aed_wakabayashi_20221223.kml")
    kml = Kml(filepaths)
    placemarks = kml.generate_placemarks()
    my_location = LonLat(longitude, latitude)
    closest_aed = kml.get_closest_placemark(my_location)
    closest_aed = LonLat(closest_aed.x, closest_aed.y)
    return kml.get_polyline(my_location, closest_aed)
    

