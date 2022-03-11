from rest_framework import serializers


class EarthquakeSerializer(serializers.Serializer):
    date = serializers.DateField(read_only=True, source="DateTime")
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()
    depth = serializers.SerializerMethodField()
    magnitude = serializers.FloatField(read_only=True, source="Magnitude")
    location = serializers.CharField(read_only=True, source="Wilayah")
    tsunami_potential = serializers.SerializerMethodField()

    def parse_coordinates(self, coordinates: str) -> tuple:
        return tuple(coordinates.split(","))

    def get_latitude(self, obj) -> float:
        return self.parse_coordinates(obj.get("Coordinates"))[0]

    def get_longitude(self, obj) -> float:
        return self.parse_coordinates(obj.get("Coordinates"))[1]

    def get_depth(self, obj) -> float:
        return float(obj.get("Kedalaman").replace(" km", ""))

    def get_tsunami_potential(self, obj) -> bool:
        if obj.get("Potensi") == "Tidak berpotensi tsunami":
            return False
        else:
            return True


class EarthquakeGetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    result = EarthquakeSerializer(many=True)
