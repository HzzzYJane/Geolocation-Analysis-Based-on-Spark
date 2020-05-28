# Geolocation-Analysis-Based-on-Spark
The big data project on NYU yellow cab pick-up location
## Introduction
In this project, we developed a k-means clustering algorithm and investigated its applications to both small and large datasets. During this process, we looked into the effect of k and distance function on the clustering, and analyzed the run-time across different k, data size, and implementation. 
## Results 
We ran the Spark_Kmeans_geo.py on the AWS EMR and the outcomes were stored in the folder NY_pickup. On cluster_visualization_E.ipynb and cluster_visualization_G.ipynb two files,we plot data points on the actual New York map with Folium. And we determine 7 as the optimal k through visual inspection with references to the maps.
