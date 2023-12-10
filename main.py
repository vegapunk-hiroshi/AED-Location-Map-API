from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from utility.kml import Kml
from utility.route import LonLat, Route
import json
# import sys
# print(sys.path)

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:8000 ",
    "http://localhost:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.5
#     tags: list[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]

@app.get("/locations")
async def fast():
    filepath = r"data/aed_aoba_20221223.kml"
    kml = Kml(filepath)
    placemarks = kml.generate_placemark()

    return placemarks

@app.get("/closest")
async def getKMLPath(longitude: float = 0, latitude: float = 0):
    filepath = r"data/aed_aoba_20221223.kml"
    kml = Kml(filepath)
    placemarks = kml.generate_placemark()
    my_location = LonLat(longitude, latitude)
    closest_aed = kml.get_closest_placemark(my_location)
    closest_aed = LonLat(closest_aed.x, closest_aed.y)
    return kml.get_polyline(my_location, closest_aed)
    

