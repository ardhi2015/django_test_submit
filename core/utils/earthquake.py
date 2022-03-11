from typing import Union
import requests


class Earthquakes:
    urls: dict = {
        "felt": "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json",
        "latest": "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json",
    }

    def get_data(self, url: str) -> Union[dict, None]:
        try:
            response = requests.get(url)

            if response.status_code != 200:
                return None

            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None

    def get_felt_earthquakes(self) -> list:
        data = self.get_data(self.urls["felt"])
        return data.get("Infogempa", {}).get("gempa", []) if data else []

    def get_latest_earthquakes(self) -> list:
        data = self.get_data(self.urls["latest"])
        return data.get("Infogempa", {}).get("gempa", []) if data else []
