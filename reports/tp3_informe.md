# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

### Explorando Patrones de Datos a través de Clustering (TP3)

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---

## Cosas a poner en el informe

**`clustering1.ipynb`**
* Contiene todos los pasos necesarios para la curación, partiendo desde el dataset crudo hasta llegar al dataset pivoteado. Aclarar qué es un registro en cada uno (ventas vs vendedores) y que el pivoteado está en pct Y y F para com y ven.
* Son los mismos pasos que hicimos para el tp2, más el paso nuevo de mapear valores a 0.
* Además de eso contiene un análisis del dataset resultante luego de la curación y antes de hacer cualquier agregación y pivotearlo. Análisis de variables categóricas, variables numéricas y de la serie temporal. No hay cambios apreciables en estos gráficos respecto a sus equivalentes del tp2.
* Al final hay una comparación entre los dataset pivoteados (tp2 vs tp3). Hablar sobre la variación de medias y SD gracias al nuevo punto que agregamos. Los datos son muchísimo menos ruidosos ahora. Sin embargo, se ve que algunos subrubros presentan una mayor variación entre el tp2 y tp3 que otros: 'Farmacia', 'Comb.', 'Vehiculos', 'Tabaco' y 'Comb. Reventa' presentan las variaciones más leves.

**`clustering2.ipynb`**
* Identificamos los datos faltantes, tanto globales como por subrubro. Vemos que hay de todo: desde 0 datos faltantes hasta casi la totalidad de datos faltantes. Incluso hay modelos con datos faltantes, pero en muchos casos se debe a que participan en más de un subrubro.
* Definimos reglas para conservar, desechar o imputar registros. Tiramos. Imputamos por KNN.