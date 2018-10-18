import matplotlib.pyplot as plt
import scipy.spatial as spatial
import numpy as np
import Welzls
from sys

# Input validation & variable declaration
sites = []
with open(sys.argv[1]) as f:
    for line in f:
        for number in line.split():
            sites.append(number)
if sites[0] != "Telephone" or sites[1] != "sites":
    print("Invalid Input Format")
    exit()
sites.remove("Telephone")
sites.remove("sites")
i = 0
point_radius = 1
sitesXY = []
while i < len(sites) - 1:
    sitesXY.append([float(sites[i]), float(sites[i+1])])
    i += 2
num_points = len(sitesXY)
if num_points > 12:
    # KDTree Stuff
    pts = np.array([[0,0],[250,250]])
    smallestKDCell = 999999999
    smallestCellPoints = []
    value = np.array(sitesXY)
    # Create the KDTree
    kdTree = spatial.KDTree(value, 12)
    # Find the smallest Cell
    num = 0
    smallest = 10000000
    smallest2 = 1000000
    smallest3 = 1000000

    for point in kdTree.data:
        data = kdTree.query(point, 12)
        for item in data:
            value = (data[0][-1])
            if value < smallest:
                smallestCellPoints.clear()
                smallest = data[0][-1]
                for point in data[1]:
                    smallestCellPoints.append(sitesXY[point])
        num += 1

    # Perform Welzl's algorithm on this set of points
    Rs = Welzls.make_circle(smallestCellPoints)

    # Get Data and shrink circle by radius of a point
    radius = Rs[2] - point_radius

    # Plot the points
    fig, ax = plt.subplots()
    for point in sitesXY:
        plt.plot(point[0], point[1], 'k.')
    plt.axis([-50, 250, -50, 250])
    plt.axis('equal')
    circle = plt.Circle((Rs[0], Rs[1]), radius, color='r')
    ax.add_artist(circle)
    plt.show()
else:
    radius = "Infinity"
print("Radius of circle that encloses only 11 points: ", radius)

