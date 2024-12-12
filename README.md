# Universal Sensing Framework: Adaptive Temperature Sensor Proof of Concept

This repository contains a proof of concept for an **adaptive temperature sensor** designed to align with the principles of the **Universal Sensing System (USS)**. The implementation showcases dynamic sensor behavior, input adaptivity, and resource efficiency in extreme environmental conditions, such as wildfire scenarios.

---

## **Project Overview**

### **Scenario: Adaptive Temperature Sensor**
The adaptive sensor:
1. **Discrete Reporting**:
   - Once a temperature threshold (e.g., 200°F) is crossed, the sensor reports in discrete increments (e.g., 220°F, 240°F).
2. **Logarithmic Scaling**:
   - At higher temperature ranges, the sensor adopts a **logarithmic reporting scale** to balance efficiency and detail.
3. **Operational Status Reporting**:
   - At extreme thresholds, the sensor stops recording temperature but **still reports its operational status**, ensuring reliability in critical conditions.

### **Purpose**
This proof of concept demonstrates key principles of the **Universal Sensing System (USS)**:
- **Input Adaptivity**: Dynamic adjustment of precision and reporting behavior.
- **Unified Encoding**: Efficient representation of sensor states (e.g., "still working" status).
- **Feedback and Efficiency**: Feedback loops drive sensor behavior to optimize energy and bandwidth.
- **Resource Management**: Focus on energy efficiency and minimal data transmission, especially in remote or extreme environments.

---

## **Key Features**

1. **Adaptive Sampling**:
   - Traditional sensors operate at fixed sampling rates.
   - This implementation introduces **threshold-based adaptivity**, where:
     - **Precision** decreases after specific thresholds (e.g., temperature increments increase).
     - Reporting transitions to a **logarithmic scale** for extreme values.

2. **Symbolic State Reporting**:
   - Encodes higher temperatures as a "still operational" state instead of precise measurements.
   - Reduces energy consumption and data transmission overhead.

3. **Real-Time Feedback**:
   - The sensor adjusts its resolution and reporting frequency based on its current state and input conditions.

4. **Energy and Bandwidth Efficiency**:
   - Optimizes resource usage, essential for wildfire scenarios with remote sensors or UAV-based monitoring systems.

---
In Progress.....


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
