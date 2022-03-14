from http.client import responses
from unittest import mock
from urllib import response
from django.test import TestCase
from ..views import EarthquakeView



class EarthquakeTest(TestCase):
  json_fake = [
      {
        "Tanggal": "06 Mar 2022",
        "Jam": "04:38:43 WIB",
        "DateTime": "2022-03-13T21:38:43+00:00",
        "Coordinates": "-0.66,98.45",
        "Lintang": "0.66 LS",
        "Bujur": "98.45 BT",
        "Magnitude": "6.0",
        "Kedalaman": "26 km",
        "Wilayah": "154 km Tenggara NIASSELATAN-SUMUT",
        "Potensi": "Tidak berpotensi tsunami"
      },
      {
        "Tanggal": "06 Mar 2022",
        "Jam": "05:40:28 WIB",
        "DateTime": "2022-03-05T22:40:28+00:00",
        "Coordinates": "3.55,126.10",
        "Lintang": "3.55 LU",
        "Bujur": "126.10 BT",
        "Magnitude": "5.0",
        "Kedalaman": "43 km",
        "Wilayah": "67 km Tenggara TAHUNA-KEP.SANGIHE-SULUT",
        "Potensi": "Tidak berpotensi tsunami"
      },
    ]

    

  
  @mock.patch("core.utils.earthquake.Earthquakes.get_latest_earthquakes", return_value=[])
  def test_data_empty(self, request):
    res = EarthquakeView.get(self, request)
    self.assertEqual(res.data["result"], [])
    self.assertEqual(res.data["status"], 'success')

    
  @mock.patch("core.utils.earthquake.Earthquakes.get_latest_earthquakes", return_value=json_fake)
  def test_date_data_exist(self, request):
    res = EarthquakeView.get(self, request)
    self.assertEqual(res.data["status"], 'success')
    items = list(res.data["result"][0].values())
    self.assertEqual(items[0], self.json_fake[0]["DateTime"])

  

    