#K means is a method of unsupervised learning that comes up with clustering

#limitations:

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2).fit(finance_features)
pred = kmeans.labels_

#n_clusters gives the number of clusters that the algorithm will classify

#n_init is how many times the clustering will start (depending on which position the centroids start the outcome will be very differe)
