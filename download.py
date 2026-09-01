# Step 3 ERA5 + Step 4 GFS - demo with dummy data
import xarray as xr, numpy as np, pandas as pd
print("Downloading ERA5 via cdsapi + GFS via NOAA... (sample)")
time = pd.date_range("2024-07-01", periods=10, freq="D")
lat = np.arange(8, 36, 0.25); lon = np.arange(68, 98, 0.25)
forecast = np.random.rand(len(time), len(lat), len(lon))*30+5
actual = forecast + np.random.randn(len(time), len(lat), len(lon))*2
ds = xr.Dataset({"forecast":(["time","lat","lon"],forecast),"actual":(["time","lat","lon"],actual)}, coords={"time":time,"lat":lat,"lon":lon})
ds.to_netcdf("sample_data.nc")
print("Saved sample_data.nc - Step 5: replaceable with NCMRWF feed in prod")