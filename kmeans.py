import numpy as np

def kmeans(pixels: np.ndarray, initial_centroids: np.ndarray, max_iter: int = 300):
    """
    Parameters:
        pixels (np.ndarray): The dataset to cluster, of shape (n_samples, 3).
        initial_centroids (np.ndarray): Initial cluster centers, of shape (n_clusters, 3).

    Returns:
        centroids (np.ndarray): Final cluster centers of shape (n_clusters, 3).
    """
    # Implement the KMeans algorithm here.
    