# **Universal Sensing Framework: Multi-Modal Sensor Encoding Proof of Concept**

This repository presents a **multi-modal sensor encoding framework** within the principles of the **Universal Sensing System (USS)**. The implementation expands on dynamic sensor behavior, input adaptivity, and resource efficiency in extreme environmental conditions such as wildfire scenarios. It integrates temperature, u-wind, and v-wind components, introducing advanced **multi-resolution encoding** and **state-aware precision control** to optimize energy and bandwidth usage.

---

## **Project Overview**

### **Scenario: Multi-Modal Sensing in Wildfire Monitoring**
The extended framework simulates and encodes **multi-modal sensors** that measure:
1. **Temperature**: Adaptive sampling based on environmental variability.
2. **U-Wind and V-Wind Components**: Precision control based on wind variability and input states.

### **Key Advances**
1. **Dynamic Resolution Control**:
   - Adjusts reporting precision based on input variability (low, medium, high).
   - Transitions to lower precision or symbolic states for resource savings.

2. **Multi-Resolution Encoding**:
   - Efficient representation of environmental data at multiple levels of precision.
   - Balances data granularity with transmission efficiency.

3. **State-Aware Precision Control**:
   - Fine resolution for high variability data.
   - Coarse resolution for low variability states to optimize resources.

4. **Operational Status Reporting**:
   - Ensures sensors encode "operational status" in extreme conditions while minimizing data overhead.

---

## **Purpose**
This proof of concept extends the **Universal Sensing System (USS)** by demonstrating:
- **Input Adaptivity**: Dynamic precision and symbolic state encoding for temperature and wind data.
- **Unified Multi-Modal Encoding**: Encoding temperature, u-wind, and v-wind into a normalized representation.
- **Feedback-Driven Behavior**: Sensors adapt precision based on environmental variability.
- **Resource Management**: Optimized energy and bandwidth usage for real-world wildfire scenarios using UAV-based or remote deployments.

---

## **Key Features**

### **1. Multi-Modal Adaptive Sampling**
   - Introduces precision control for **temperature**, **u-wind**, and **v-wind**.
   - Adaptive thresholds:
     - **Temperature**:
       - Low Variability: 2–5°C increments.
       - High Variability: 0.1–0.5°C increments.
     - **Wind (u-wind, v-wind)**:
       - Low Variability: 1 m/s increments.
       - High Variability: 0.1–0.5 m/s increments.

### **2. Multi-Resolution Encoding**
   - Normalizes sensor values into a range \([0, 1]\) for efficient transmission:
     \[
     E_{\text{sensor}} = \sum_{i=1}^N \sum_{t=1}^T 
     \left[ \frac{V_{\text{temperature}}(i, t) - (-50)}{50 - (-50)} \right] \cdot R_{\text{temperature}} +
     \left[ \frac{V_{\text{u-wind}}(i, t) - (-20)}{20 - (-20)} \right] \cdot R_{\text{wind}} +
     \left[ \frac{V_{\text{v-wind}}(i, t) - (-20)}{20 - (-20)} \right] \cdot R_{\text{wind}}
     \]

### **3. Symbolic State Reporting**
   - Encodes sensor states such as **"operational"** in extreme environmental conditions to minimize transmission overhead.

### **4. Sensor Distribution and Visualization**
   - Randomized sensor placement with geospatial plotting.
   - Sensors are annotated with:
     - Sensor ID
     - Distance to central server
     - State-aware precision control.

---

## **Grid Setup**

### **Central Location**:
**Fort McMurray, Alberta**:  
- **Latitude**: ~56.75°N  
- **Longitude**: ~111.25°W  

### **ERA5 Grid Layout**:
- **Spatial Extents**:
   - **Latitude Range**: 56.0°N to 57.4°N  
   - **Longitude Range**: -112.1°W to -110.7°W  
- **Resolution**: 0.1° × 0.1° (~9 km grid spacing).  

| **Latitude**          | **Longitude**           |
|-----------------------|-------------------------|
| 56.0°N to 57.4°N      | -112.1°W to -110.7°W    |

The grid forms a **14x14 layout** for high-resolution wildfire analysis.

---

## **Data Sources**
- **NetCDF Files**:
   - Temperature: `April-30-temp.nc`, `May-01-temp.nc`, `May-02-temp.nc`, `May-03-temp.nc`  
   - U-Wind: `April-30-u-wind.nc`, `May-01-u-wind.nc`, `May-02-u-wind.nc`, `May-03-u-wind.nc`  
   - V-Wind: `April-30-v-wind.nc`, `May-01-v-wind.nc`, `May-02-v-wind.nc`, `May-03-v-wind.nc`  

- **Coverage**: Hourly temperature and wind component data.  
- **Format**: NetCDF with Float32 data type.  

---

## **Visualizations**

1. **Temperature Comparison**:
   - Grid cells with **widest** and **narrowest** temperature variability.

2. **Wind Intensity Analysis**:
   - U-Wind and V-Wind intensities plotted for cells with widest and narrowest temperature ranges.

3. **Sensor Placement Visualization**:
   - Geospatial plot with sensor locations, IDs, and distances to the central server.

4. **Efficiency Gains**:
   - Bar chart showing efficiency gain of **adaptive vs. fixed** interval reporting.

---

## **Dependencies**
- Python Libraries:
   - `xarray`, `pandas`, `matplotlib`, `numpy`  
- Tools:
   - ERA5-Land data via NetCDF format.

---

## **Future Work**
- Integration of **state-aware symbolic encoding** for multi-modal data fusion.  
- Application of **multi-resolution encoding** in dynamic wildfire modeling and UAV-based systems.  
- Exploration of predictive models using encoded sensor states.

---

## **Conclusion**
This proof of concept demonstrates how **multi-modal, state-aware adaptive sensors** within a **universal encoding framework** optimize precision, efficiency, and resource management in dynamic wildfire scenarios.
