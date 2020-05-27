import sys
from random import randint
from pyspark import SparkContext
from math import sqrt, sin, cos, sqrt, atan2, radians


# given two points, add each of their dimensions
def AddPoints(point_1, point_2):
    return point_1[0] + point_2[0], point_1[1] + point_2[1], point_1[2] + point_2[2]


# given the sum of a list of points and the length of the list, compute the mean 
def UpdateCentroids(points_sum):
    return points_sum[1][0] / points_sum[1][2], points_sum[1][1] / points_sum[1][2]


# given two points, return their Euclidean distance
def EuclideanDistance(point_1, point_2):
    return sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


# given two points, return their great circle distance.
# NOTICE: formula from https://www.movable-type.co.uk/scripts/gis-faq-5.1.html
def GreatCircleDistance(point_1, point_2):
    dlat = radians(point_1[0] - point_2[0]);
    dlon = radians(point_1[1] - point_2[1])
    a = sin(dlat / 2) ** 2 + cos(radians(point_1[0])) * cos(radians(point_2[0])) * sin(dlon / 2) ** 2
    return 2 * atan2(sqrt(a), sqrt(1 - a))


# given the centroid list and one point, return the closest centroid index together with the distance
def closestPoint(the_centroids, point, dis):
    closest_dis = float("inf");
    min_index = 0

    for index in range(len(the_centroids)):
        dis = EuclideanDistance(the_centroids[index], point) if dis == "E" else GreatCircleDistance(
            the_centroids[index], point)
        if dis < closest_dis:
            closest_dis = dis;
            min_index = index

    return min_index


# given the current and previous centroids lists,
# return the converge distance based on the user specified distance measure
def ComputeConvergeDist(cur_centroids, cache_centroids, dis):
    if dis == "E":
        return sum([EuclideanDistance(cur_centroids[i], cache_centroids[i]) for i in range(len(cur_centroids))])
    else:
        return sum([GreatCircleDistance(cur_centroids[i], cache_centroids[i]) for i in range(len(cur_centroids))])


if __name__ == "__main__":

    # defensive programming
    if len(sys.argv) < 5:
        print >> sys.stderr, "Usage: <input_file_dir> <output_centers_dir> k <G,E>"
        exit(-1)

    # initialize the Spark Context object and parse command line input
    sc = SparkContext()
    input_file = sys.argv[1]
    output_centroid = sys.argv[2]
    input_k = int(sys.argv[3])
    input_dis = sys.argv[4]

    # create the raw data RDD and persist
    all_data = sc.textFile(input_file) \
        .filter(lambda x: len(x) > 0) \
        .map(lambda x: x.split("\t")) \
        .map(lambda x: (float(x[0]), float(x[1]))) \
        .persist()

    # initialize initial k centroids by random taking k samples
    # centroids_initial = all_data.takeSample(False, input_k, randint(1, 100)) # a list
    centroids_initial = all_data.takeSample(False, input_k, 1)  # a list # for debugging
    centroids = list(centroids_initial)
    print centroids

    # while the converge distance is more than the threshold,
    # 1) find the closest centroid for each point, and "assign" it to the corresponding cluster
    # 2) compute and update the mean of each cluster
    # 3) compute the converge difference between the previous centroids and the current centroids
    convergeDist = float("inf")
    while convergeDist > 0.000001:
        cur_centroids = all_data.map(lambda p: (closestPoint(centroids, p, input_dis), p)) \
            .mapValues(lambda p: (p[0], p[1], 1)) \
            .reduceByKey(lambda p1, p2: AddPoints(p1, p2)) \
            .map(lambda p_sum: UpdateCentroids(p_sum)) \
            .collect()

        convergeDist = ComputeConvergeDist(cur_centroids, centroids, input_dis)
        centroids = list(cur_centroids)

    print centroids  # TODO: save here

    sc.stop()
