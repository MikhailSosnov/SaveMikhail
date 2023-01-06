

import pyowm
from pyowm import OWM
city = "New York, USA"
owm = pyowm.OWM('7d2dc58c49406df6017063b97db5ae4c')
mgr = owm.weather_manager()
daily_forecast = mgr.forecast_at_place(city, 'daily').forecast
tree_h_forecast = mgr.forecast_at_place(city, '3h').forecast

print(daily_forecast)
printtree_h_forecast()


# import pyowm
# from pyowm import OWM
# city = "New York, USA"
# owm = pyowm.OWM('7d2dc58c49406df6017063b97db5ae4c')
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# w = observation.weather
# temp = w.temperature('celcius')['temp']
#
# print("В городе" + city + "сейчас" + str(temp) + "градусов")
#
#

# import eel
# import pyowm
# from pyowm import OWM
# city = "New York, USA"
# owm = pyowm.OWM('7d2dc58c49406df6017063b97db5ae4c')
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# w = observation.weather
# temp = w.temperature('celcius')['temp']
#
# print("В городе" + city + "сейчас" + str(temp) + "градусов")

# from pyowm import OWM
# from pyowm.utils.config import get_default_config
# from pyowm.commons.exceptions import NotFoundError
#
#
# config_dict = get_default_config()
# config_dict['language'] = 'ru'  # your language here
# owm = OWM('7d2dc58c49406df6017063b97db5ae4c')  # You MUST provide a valid API key
#
# place = input("Введи Город/страну: ")
# mgr = owm.weather_manager()
#
# try:
#     observation = mgr.weather_at_place(place)
#     w = observation.weather
#     temp = w.temperature('celsius')["temp"]
#
#     print(f"В городе {place} сейчас {w.detailed_status}")
#     print(f"Температура: {temp}")
#
# except NotFoundError:
#     print(f'Не найдено место: {place}')


# from pyowm.owm import OWM
#
# owm = pyowm.OWM('7d2dc58c49406df6017063b97db5ae4c')
# mgr = owm.weather_manager()
#
# observation = mgr.weather_at_place('Tokyo,JP')
# w = observation.weather
#     # get_weather()
#
# print(w)