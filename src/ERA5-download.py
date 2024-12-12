import cdsapi

# Define dataset and request parameters
dataset = "reanalysis-era5-land"
request = {
    "variable": ["2m_temperature"],
    "year": ["2016"],
    "month": ["04", "05"],
    "day": ["30", "01", "02", "03"],
    "time": [
        "00:00", "01:00", "02:00", "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
    ],
    "data_format": "netcdf",
    "area": [57.2, -111.9, 56.2, -110.9]  # North, West, South, East
}

# Authenticate and retrieve the data
client = cdsapi.Client()  # Ensure ~/.cdsapirc has the updated credentials
client.retrieve(dataset, request, "era5_land_fort_mcmurray_2016.nc")

print("Data successfully downloaded: 'era5_land_fort_mcmurray_2016.nc'")
