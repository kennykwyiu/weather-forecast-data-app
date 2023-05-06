import requests

API_KEY = "bb5ac2ca514605f1dce9d6c60e43560d"


def get_data(place, forecast_days=None):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="hongkong", forecast_days=3))
    print(len(get_data(place="hongkong", forecast_days=3)))