import numpy as np

def k_means_clustering(
    points: list[tuple[float, ...]],
    k: int,
    initial_centroids: list[tuple[float, ...]],
    max_iterations: int
) -> list[tuple[float, ...]]:

    points = np.array(points, dtype=float)
    cen = np.array(initial_centroids, dtype=float)

    for _ in range(max_iterations):

        labels = []

        for point in points:
            distances = []

            for centroid in cen:
                distance = np.sqrt(np.sum((point - centroid) ** 2))
                distances.append(distance)

            labels.append(np.argmin(distances))

        labels = np.array(labels)

        new_cent = []

        for cluster_id in range(k):
            cluster_points = points[labels == cluster_id]

            new_centroid = np.mean(cluster_points, axis=0)
            new_cent.append(new_centroid)

        new_cent = np.array(new_cent)

        if np.allclose(cen, new_cent):
            break

        cen = new_cent

    return [tuple(c) for c in cen]