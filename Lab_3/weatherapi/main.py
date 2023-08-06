import swagger_client
from swagger_client.rest import ApiException
import datetime


class Client:
    def __init__(self, key):
        self.__configuration = swagger_client.Configuration()
        self.__configuration.api_key['key'] = key

    def get_current_temperature(self, city):
        api_instance = swagger_client.APIsApi(swagger_client.ApiClient(self.__configuration))
        try:
            api_response = api_instance.realtime_weather(city)
            return api_response.current.temp_c
        except ApiException as e:
            print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

    def get_temperature_after(self, city, days, hour=None):
        api_instance = swagger_client.APIsApi(swagger_client.ApiClient(self.__configuration))
        try:
            if hour:
                api_response = api_instance.forecast_weather(city, days, hour=hour)
                return api_response.forecast.forecastday[-1].hour[hour - 1].temp_c
            else:
                api_response = api_instance.forecast_weather(city, days)
                return api_response.forecast.forecastday[-1].hour[int(datetime.datetime.now().strftime("%H"))].temp_c
        except ApiException as e:
            print("Exception when calling APIsApi->forecast_weather: %s\n" % e)

    def get_lat_and_long(self, city):
        api_instance = swagger_client.APIsApi(swagger_client.ApiClient(self.__configuration))
        try:
            api_response = api_instance.search_autocomplete_weather(city)
            return api_response[0]['lat'], api_response[0]['lon']
        except ApiException as e:
            print("Exception when calling APIsApi->search_autocomplete_weather: %s\n" % e)
