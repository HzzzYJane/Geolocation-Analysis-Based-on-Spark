# Geolocation-Analysis-Based-on-Spark
The big data project on the analysis of NYU yellow cab pick-up location
## Introduction
In this project, we developed a k-means clustering algorithm and investigated its applications to both small and large datasets. For the large dataset, you could find it on the [data souce](https://www.kaggle.com/asrsaiteja/aaic-yellowtaxi-demand-prediction). During this process, we looked into the effect of k and distance function on the clustering, and analyzed the run-time across different k, data size, and implementation.
## Results 
We ran the Spark_Kmeans_geo.py on the preprocessed data, with each datapoint in the form of (longitude, latitude). Running the Pyspark file on the AWS EMR, we then stored the outcomes in AWS S3. With **cluster_visualization_E.ipynb** and **cluster_visualization_G.ipynb** two files, we plot data points on the actual New York map with Folium. And we determine 7 as the optimal k through visual inspection with references to the maps. And you could see the final image as below:  
<p align="center">
  <img width="600" height="500" src="https://github.com/HzzzYJane/Geolocation-Analysis-Based-on-Spark/blob/master/image/7%20clusters.png">
</p>
To help understand the clustering results, the table below describes the locations of the centroid of each cluster. And these locations of centroids corresponding to 7 clusters are transportation hubs, Tourist attractions and popular detinations, i.e.,  the busiest points in New York.
<p align="center">
  <img width="450" height="200" src="https://github.com/HzzzYJane/Geolocation-Analysis-Based-on-Spark/blob/master/image/7%20cluster%20centroids.png">
</p>  

## Conclusion  
The clustering gave information about areas in NYC with high cab demands. The position of centroids were the most popular spots among that cluster area. These information could be beneﬁcial to the cab company in their management and marketing.




