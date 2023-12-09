import openrouteservice

class LonLat:
    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"{self.longitude}, {self.latitude}"

    def get_lonlat(self):
        return (self.longitude, self.latitude)
        

class Route:
    def __init__(self, start: LonLat, end: LonLat):
        # coords = ((8.34234,48.23424),(8.34423,48.26424))
        self.coords = (start.get_lonlat(), end.get_lonlat())
        self.client = openrouteservice.Client(key='5b3ce3597851110001cf62480a0b07b915894b6b846751c5f6690b88') # Specify your personal API key
    
    def get_direction(self):
        routes = self.client.directions(self.coords)
        print(routes)
        return routes
