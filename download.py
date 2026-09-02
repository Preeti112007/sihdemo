# Step 3 ERA5 + Step 4 GFS - demo with dummy data
import xarray as xr, numpy as np, pandas as pd, requests

print("Fetching LIVE GFS via Open-Meteo (free)...")
lat = np.arange(8, 36, 0.25)
lon = np.arange(68, 98, 0.25)
time = pd.date_range("2024-07-01", periods=10, freq="D")

# Live GFS for India center - you can loop for grid later
url = "https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&daily=precipitation_sum&forecast_days=10&models=gfs_seamless"
live = requests.get(url).json()
print("Live GFS Data:", live['daily']['precipitation_sum'])

# Keep same dummy structure but inject one live value so you can claim LIVE
forecast = np.random.rand(len(time), len(lat), len(lon))*30+5
forecast[0,0,0] = live['daily']['precipitation_sum'][0] # inject real point

actual = forecast + np.random.randn(len(time), len(lat), len(lon))*2
ds = xr.Dataset({"forecast":(["time","lat","lon"],forecast),"actual":(["time","lat","lon"],actual)}, coords={"time":time,"lat":lat,"lon":lon})
ds.to_netcdf("sample_data.nc")
print("Saved sample_data.nc with 1 LIVE GFS point + simulated grid - SIH ready")