
# **README: Spatial Analysis of Schools and Assets in Thiruvananthapuram Corporation**

## Project Overview
This project analyzes the spatial relationship between schools and assets within Thiruvananthapuram Corporation (TVC) using GeoPandas, Pandas, and Matplotlib. The key objectives are:

*   Convert school location data from CSV into a GeoDataFrame.
*   Reproject the data for accurate distance-based calculations.
*   Identify schools that fall within TVC boundaries.
*   Create a 2000m buffer zone around schools.
*   Identify assets within these buffer zones.
*   Visualize the results with matplotlib.

## Dataset Description
**Input Files:**
*   Schools.csv - Contains school names and their coordinates (longitude & latitude).
*   TVM_Corp.shp - Shapefile of Thiruvananthapuram Corporation boundary.
*   Assets.shp - Shapefile containing asset locations.

**Output Files:**
*   school_buffers.shp - 2000m buffer zones around schools.
*   assets_within_schools.shp - Assets found within the school buffer zones.

## Installation & Setup
### 1. Install Dependencies
Ensure you have the required Python libraries installed:
