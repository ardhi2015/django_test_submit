from django.db import models


class Weather(models.Model):
    """
    Weather data
    """

    weather_code = (
        (0, 'Clear'),
        (3, 'Partly Cloudy'),
        (51, 'Drizzle'),
        (61, 'Rain'),
        (80, 'Rain Showers'),
        (95, 'Thunderstorm'),
        (96, 'Thunderstorm'),
    )

    date = models.DateField(auto_now_add=True)
    weathercode = models.IntegerField(choices=weather_code, default=0)
    temperature = models.FloatField(default=0.0)
    max_temperature = models.FloatField(default=0.0)
    min_temperature = models.FloatField(default=0.0)
    sunrise = models.DateTimeField(null=True)
    sunset = models.DateTimeField(null=True)

    class Meta:
        managed = True
