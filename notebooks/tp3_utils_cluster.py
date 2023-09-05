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
        kmeans = KMeans(n_clusters=n_clust, n_init=10)
        cluster_labels = kmeans.fit_predict(X)
        silhouette_score_values.append(silhouette_score(X, cluster_labels))

    plt.figure(figsize=(5, 3))
    plt.plot(n_clusters_range, silhouette_score_values, marker='o', ls=':')
    plt.xlabel('Cantidad de clusters')
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

    fig, axs = plt.subplots(1, 4, figsize=(50, 10))

    k=0
    for n_clusters in n_clusters_range[:5]:

        kmeans = KMeans(n_clusters=n_clusters, n_init=10)
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
            axs[k].fill_betweenx(np.arange(y_lower, y_upper), 0, cluster_silhouette_values, facecolor=color, alpha=0.7)
            axs[k].text(-0.05, y_lower + 0.5 * size_cluster_j, str(j), fontsize=30)
            y_lower = y_upper + 10

        axs[k].set_title(f"K = {n_clusters}, Silhouette Score = {silhouette_avg:.2f}", fontsize=30)
        axs[k].set_xlabel("Coef. de silueta", fontsize=30)
        axs[k].set_ylabel("ID cluster", fontsize=30)
        axs[k].axvline(x=silhouette_avg, color="red", linestyle="--")
        axs[k].set_yticks([])
        axs[k].set_xlim(-0.1, 1)
        axs[k].set_ylim(0, len(X) + (n_clusters + 1) * 10)
        k += 1

    plt.show()