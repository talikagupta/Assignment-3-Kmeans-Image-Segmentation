# KMeans for Image Segmentation

In this assignment, you will implement the K-Means algorithm for image segmentation by clustering the pixels of an image based on their RGB values.

## Assignment Instructions

### Objective
Implement the `kmeans` function in `kmeans.py` to perform image segmentation on an image. The function should output:
1. The final centroids.
2. An array indicating the centroid each pixel belongs to.
Update the centroids iteratively until convergence, i.e., until the centroids no longer change.

### Input Format
- A `numpy.ndarray` of shape `(num_pixels, 3)` where each row represents an RGB pixel.
- Initial centroids as a `numpy.ndarray` of shape `(n_clusters, 3)`.

### Output Format
- Final centroids as a `numpy.ndarray` of shape `(n_clusters, 3)`.

### Starter Code
The starter code is in `kmeans.py`. Implement the `kmeans` function. Do not import any other libraries than the ones imported already in the starter code. 
