from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

import matplotlib.pyplot as plt
import numpy as np

def etiquetar_tipo_subrubro(df_grupo):
    # Si hay empate en la cantidad de Vacíos, seleccionamos el que tenga el menor Promedio
    min_vacios = df_grupo['Vacios'].min()
    max_montos = df_grupo[df_grupo['Vacios'] == min_vacios]['Montos'].max()
    
    # Identificar el Primario y Secundarios
    df_grupo['Tipo_subrubro'] = 'Secundario'
    df_grupo.loc[(df_grupo['Vacios'] == min_vacios) & (df_grupo['Montos'] == max_montos), 'Tipo_subrubro'] = 'Primario'
    
    return df_grupo

def determinar_decision(row):
    # Crear una función para determinar la decisión
    if row['Modelo'] == 1:
        if row['Tipo_subrubro'] == 'Primario':
            if row['Vacios'] == 0:
                return 'No hacer nada'
            elif row['Vacios'] <= 68:
                return 'Imputar'
            else:
                return 'Tirar'
        elif row['Tipo_subrubro'] == 'Secundario':
            if row['Vacios'] == 0:
                return 'No hacer nada'
            elif row['Vacios'] <= 34:
                return 'Imputar'
            else:
                return 'Tirar'
    elif row['Modelo'] == 0:
        if row['Tipo_subrubro'] == 'Primario':
            if row['Vacios'] == 0:
                return 'No hacer nada'
            elif row['Vacios'] <= 14:
                return 'Imputar'
            else:
                return 'Tirar'
        elif row['Tipo_subrubro'] == 'Secundario':
            if row['Vacios'] == 0:
                return 'No hacer nada'
            elif row['Vacios'] <= 7:
                return 'Imputar'
            else:
                return 'Tirar'
    return 'Desconocido'

def plot_silueta_lineas(X, k_min, k_max):
    
    n_clusters_range = range(k_min, k_max+1)

    silhouette_score_values = []
    for n_clust in n_clusters_range:
        kmeans = KMeans(n_clusters=n_clust, n_init='auto')
        kmeans.fit(X)
        silhouette_score_values.append(silhouette_score(X, kmeans.labels_))
        
    plt.figure(figsize=(10, 6))
    plt.plot(n_clusters_range, silhouette_score_values, marker='o')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score de Silueta')
    plt.title('Score de Silueta vs. Número de Clusters')
    plt.xticks(n_clusters_range)
    plt.grid(True)
    plt.show()

def plot_silueta_diagram(X, k_min, k_max):
    """
    Hace Kmeans de varios K y plotea el diagrama de silueta de cada uno
    X: data frame con los valores numéricos para clusterizar
    k_min: mínimo número de clusters
    k_max: máximo número de clusters
    """
    
    n_clusters_range = range(k_min, k_max+1)
    
    plot_num_filas = int(np.ceil((k_max+1-k_min)/2))
    
    plt.figure(figsize=(12, 8))
    for i, n_clusters in enumerate(n_clusters_range, 1):
        plt.subplot(plot_num_filas, 2, i)
        kmeans = KMeans(n_clusters=n_clusters, n_init='auto')
        cluster_labels = kmeans.fit_predict(X)

        silhouette_avg = silhouette_score(X, cluster_labels)
        silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for j in range(n_clusters):
            cluster_silhouette_values = silhouette_values[cluster_labels == j]
            cluster_silhouette_values.sort()
            size_cluster_j = cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_j

            color = plt.cm.nipy_spectral(float(j) / n_clusters)
            plt.fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_values, facecolor=color, alpha=0.7)
            plt.text(-0.05, y_lower + 0.5 * size_cluster_j, str(j))
            y_lower = y_upper + 10

        plt.axvline(x=silhouette_avg, color="red", linestyle="--")
        plt.title(f"K = {n_clusters}, Silhouette Score = {silhouette_avg:.2f}")
        plt.xlabel("Silhouette Coefficient")
        plt.ylabel("Cluster")
        plt.xlim(-0.1, 1)
        plt.ylim(0, len(X) + (n_clusters + 1) * 10)

    plt.tight_layout()
    plt.show()