

## Simple Forecast model
# Import data
import pandas as pd


# Fitting model to Novermber forecasting data

### Import Data

data = "https://raw.githubusercontent.com/harrymmurphy/old-cocoa_thesis_data/main/forecast%20ivory%20coast.csv"

forecast_data = pd.read_csv(data)

forecast = forecast_data[["datetime","temp", "precip", "humidity"]]


temperature = forecast_data["temp"]
precipitation = forecast_data["precip"]
humidity = forecast_data["humidity"]



# Create column fit to model

nov_forecast = temperature*0.5 +humidity*0.28 - precipitation*0.05 - 20

#save to csv file

forecast['nov_forecast'] = nov_forecast

forecast.to_csv('C:/Users/Harry Murphy/OneDrive/Desktop/BP_Nov_Forecast')
print(forecast.style)
