import numpy as np
from kmeans import kmeans
import matplotlib.pyplot as plt
from matplotlib.image import imread

def test_kmeans():
    image = imread('cat.png')
    pixels = image.reshape(-1, 3)
    np.random.seed(42)
    K = 2
    random_sample_idxs = np.random.choice(pixels.shape[0], K, replace=False)
    initial_centroids = [pixels[idx] for idx in random_sample_idxs]
    centroids = kmeans(pixels, initial_centroids, max_iter=100)
    expected_centroids = np.array([[0.96084172, 0.90596837, 0.80747569], [0.35131353, 0.26238891, 0.21711203]])
    assert np.allclose(centroids, expected_centroids, atol=1e-1), "Centroids do not match expected values."
