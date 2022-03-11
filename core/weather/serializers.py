from rest_framework import serializers

from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    weathercode = serializers.IntegerField(write_only=True)
    weather = serializers.CharField(read_only=True, source="get_weathercode_display")
    temperature = serializers.FloatField()
    max_temperature = serializers.FloatField()
    min_temperature = serializers.FloatField()
    sunrise = serializers.DateTimeField()
    sunset = serializers.DateTimeField()

    class Meta:
        model = Weather
        fields = "__all__"


class WeatherGetResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    result = WeatherSerializer(many=True)


class WeatherPostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    result = WeatherSerializer()
