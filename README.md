# Geolocation-Analysis-Based-on-Spark
The big data project on the analysis of NYU yellow cab pick-up location
## Introduction
In this project, we developed a k-means clustering algorithm and investigated its applications to both small and large datasets. For the large dataset, you could find it on the [data souce](https://www.kaggle.com/asrsaiteja/aaic-yellowtaxi-demand-prediction). During this process, we looked into the effect of k and distance function on the clustering, and analyzed the run-time across different k, data size, and implementation.
## Results 
We ran the Spark_Kmeans_geo.py on preprocessed dataset the AWS EMR and stores the outcomes in AWS S3. With **cluster_visualization_E.ipynb** and **cluster_visualization_G.ipynb** two files, we plot data points on the actual New York map with Folium. And we determine 7 as the optimal k through visual inspection with references to the maps. And you could see the final image as below:  
![](/image.7%20clusters.png)
To help understand the clustering results, the table below describes the locations of the centroid of each cluster.
[^_^]:
  <p align="center">
    <img width="160" height="200" src="https://github.com/HzzzYJane/Geolocation-Analysis-Based-on-    Spark/blob/master/cluster%20centroids%20table.png">
  </p>
![](/image.7%20clusters.png)

## Conclusions  
The clustering gave information about areas in NYC with high cab demands. The position of centroids were the most popular spots among that cluster area. These information could be beneﬁcial to the cab company in their management and marketing.




