import cdsapi

dataset = "reanalysis-era5-land"
request = {
    "variable": ["10m_v_component_of_wind"],
    "year": "2016",
    "month": "05",
    "day": ["03"],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [57.35, -112.05, 56.05, -110.75]
}

client = cdsapi.Client()

target = "May-03-v-wind.nc"
client.retrieve(dataset, request, target)
