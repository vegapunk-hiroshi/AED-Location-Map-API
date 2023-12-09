from fastkml import kml
from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points

from utility.route import LonLat, Route


class PlaceMark:
    def __init__(self, name, description, latitude, longitude, style):
        self.name: str = name
        self.description: str = description
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.style: str = style

class Kml:
    def __init__(self, filepath):
        self.filepath = filepath
        self.placemarks = []

    def generate_placemark(self):
        with open(self.filepath, 'rt', encoding="utf-8") as the_file:
            doc = the_file.read()
            k = kml.KML()
            k.from_string(doc)
            features = list(k.features())
            feat = list(features[0].features())
            for pm in feat[0]._features:
                self.placemarks.append(
                    PlaceMark(pm.name, pm.description, 
                    pm.geometry.y, pm.geometry.x, pm.styleUrl)
                )
        return self.placemarks

    def get_closest_placemark(self, latlon: LonLat):
        # TODO: algorithm to generate a geojson to the path to the closest AED using library
        orig = Point(latlon.longitude, latlon.latitude)
        dest = []
        for i in self.placemarks:
            dest.append(Point(i.longitude, i.latitude))

        destinations = MultiPoint(dest)
        nearest_geoms = nearest_points(orig, destinations)
        return nearest_geoms[1]


    def get_route(self, start, end):
        print('start: ', start)
        print('end: ', end)
        route = Route(start, end)
        # TODO 
        return route.get_direction()
