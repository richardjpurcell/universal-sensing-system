# 1. Define the Grid Coordinates

## Central Point:
**Fort McMurray, Alberta**:  
- **Latitude**: ~56.7°N  
- **Longitude**: ~111.4°W  

## Revised ERA5-Land Grid Layout:
- The downloaded map has an extent of:  
   - **Longitude Range**: -112.1°W to -110.7°W  
   - **Latitude Range**: 56.0°N to 57.4°N  
- The grid consists of a **14x14 layout** (width = 14, height = 14), with:  
   - **Spatial Resolution**: 0.1° × 0.1° (~9 km grid spacing).  
   - **Data Type**: Float32 (32-bit floating point).

---

## Grid Boundaries:
1. **Latitude Range**:  
   - **Lower Bound**: 56.0°N  
   - **Upper Bound**: 57.4°N  

2. **Longitude Range**:  
   - **Left Bound**: -112.1°W  
   - **Right Bound**: -110.7°W  

---

## Final Grid:
| **Latitude**          | **Longitude**           |
|-----------------------|-------------------------|
| 56.0°N to 57.4°N      | -112.1°W to -110.7°W    |

This grid forms a **14x14 grid** of ERA5-Land cells at a resolution of 0.1° × 0.1° (~9 km per cell).

---

## Dataset Details:
- **Format**: NetCDF  
- **Driver**: GDAL NetCDF  
- **Data Type**: Float32 (32-bit floating point)  
- **Coverage**: Hourly temperature data at 2 meters above ground level.  

This updated extent provides accurate geospatial coverage for analyzing temperature variability during the Fort McMurray 2016 wildfire.
