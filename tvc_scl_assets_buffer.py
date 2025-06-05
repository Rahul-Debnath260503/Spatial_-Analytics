##importing required library
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#load the csv dataset(school.csv)
school = pd.read_csv(r"C:\Users\User\OneDrive\Desktop\Advance Geospatia p\Data_24_2_2024\Data_24_2_2024\Schools.csv")
school.head()#head of the csv data

#convert csv to point shape file.
point = gpd.points_from_xy(school['Long'],school['Lat'],crs='EPSG:4326')
school_gdf = gpd.GeoDataFrame(school, geometry = point, crs = 'EPSG:4326')
type(school_gdf)

#converting the coordinate gcs to pcs(4326 to 32643) 
#its needed for distance based calculations like buffering.
scl_cng_crs = school_gdf.to_crs('EPSG:32643')
scl_cng_crs.crs
scl_cng_crs.plot() #visualize the school location 
#Load the Thiruvananthapuram Corporation and Assets Shapefiles.
#each coordinate should be same crs for correct spatial operatons
tvc_cor = gpd.read_file(r"C:\Users\User\OneDrive\Desktop\Advance Geospatia p\Data_24_2_2024\Data_24_2_2024\TVM_Corp.shp")
print(tvc_cor.crs) #checking crs 
tvc_cor.plot()

tvc_assets = gpd.read_file(r"C:\Users\User\OneDrive\Desktop\Advance Geospatia p\Data_24_2_2024\Data_24_2_2024\Assets.shp")
print(tvc_assets.crs) #checking crs
print(tvc_assets.geom_type)  #checking geometry type
tvc_assets.plot()

#schools under tvm corporation
tvc_school = gpd.clip(scl_cng_crs,tvc_cor)

#create 2000m buffer around schools
cor_scl_buff = tvc_school.buffer(2000)

#conver buffer (geoseries) to GeoDataFrame.
cor_scl_gdf = gpd.GeoDataFrame(geometry = gpd.GeoSeries(cor_scl_buff),crs = 'EPSG:32643')
cor_scl_gdf.plot() #plot buffer zone around school
plt.title('schools under 2000m of tvc corporation')
plt.show()

#conver buffer to geographic crs
proper_geom = cor_scl_buff.to_crs('EPSG:4326')
print(proper_geom.crs)

#identify assets within 2000m of schools
assets_scl = gpd.clip(cor_scl_buff,tvc_assets)
#assets_in_scl = assets_scl.buffer(2000)
assets_scl.plot() #plot the selected assets

#finally plotting the all layers 
fig, ax = plt.subplots(figsize=(8,6)) 
tvc_cor.boundary.plot(ax=ax,color='purple') #plot the tvc boundary
cor_scl_gdf.plot(ax=ax, color='gray') #plot the school buffer zones(2000m)
tvc_school.plot(ax=ax, color = 'blue') #plot the school under boundary of tvm corporation.
assets_scl.plot(ax=ax,color='red') #plot the assets under school buffer zone(2000m)
plt.show()

#save the output as shape file.
cor_scl_buff.to_file(r"C:\Users\User\Desktop\Advance Geospatia p\practical\school_buffer.shp")
assets_scl.to_file(r"C:\Users\User\Desktop\Advance Geospatia p\practical\assets_within_schools.shp")