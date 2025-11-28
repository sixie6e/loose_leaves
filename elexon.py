from datetime import datetime
import pandas as pd
import future
import time
import elexonpy
from elexonpy.rest import ApiException
from pprint import pprint
from elexonpy.api_client import ApiClient
from elexonpy.api.generation_forecast_api import GenerationForecastApi
from elexonpy.api.demand_api import DemandApi

api_client = ApiClient()
forecast_api = GenerationForecastApi(api_client)
demand_api = DemandApi(api_client)
temp_api = elexonpy.TemperatureApi()
_from = '2025-11-20'
to = '2025-11-26'
format = 'json_xml' 

from_date = datetime(2025, 11, 7)
to_date = datetime(2025, 11, 13)  # 7 day max

# wind/solar
dff = forecast_api.forecast_generation_wind_and_solar_day_ahead_get(
    _from=from_date,
    to=to_date,
    process_type='day ahead',
    format='dataframe'
)

# temp
try:
    api_response = api_instance.temperature_get(_from=_from, to=to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling temperature_get: %s\n" % e)

# all
dft = demand_api.demand_actual_total_get(
    _from=from_date,
    to=to_date,
    settlement_period_from=1,
    settlement_period_to=48,
    format='dataframe'
)

print(dff.head(), dft.head())
