# Diplomatura en ciencia de datos, aprendizaje automático y sus aplicaciones - Edición 2023 - FAMAF (UNC)

## Mentoría 16 - ¿Cómo identificar fuga de ventas? Inteligencia artificial aplicada al sector comercial.

### Curación (TP2)

**Integrantes:**
- Canalis, Patricio.
- Chevallier-Boutell, Ignacio José.
- Villarroel Torrez, Daniel.

**Mentores:**
- Gonzalez, Lucía
- Lahoz, Nahuel

---
# Reporte

> Cosas que pueden servir:
* Respecto a las ventas (vars num):
    * Todas las ventas nulas se corresponden a comisiones nulas
    * Existen 26 registros con ventas negativas asociadas a comisiones nulas. De éstos, 25 tienen comisión nula y uno tiene comisión del 0.18%. Como en todos los casos son ventas negativas, puede ser que esta sea la razón de tener una comisión nula. Ninguno de estos 26 registros corresponde a vendedor modelo. De hecho no hay ningún modelo con ventas negativas.
    * Hay 2232 registros con ventas positivas asociadas a comisiones nulas. De éstos:
        * 34 registros corresponden a vendedores modelo.
        * 1458 registros con alícuota nula.
        * 774 registros con alícuota no nula.
    * No hay ningún modelo con ventas nulas: la mayoría de sus registros son ventas positivas, aunque hay algunos con ventas negativas.
    * Todos los modelos tienen alícuotas bajas (muy ceranas al 0%). Hay 5374 registros asociados a vendedores modelo y sus alícuotas van desde 0.0084% hasta 3.25%. Sin embargo, la mayoría se concentra en alícuotas menores a 0.075 %, teniendo un pico en 0.05%.

* Respecto a chequear unicidad (vars cat):
    * Existen vendedores modelo que participan en más de un subrubro. Si un vendedor es calificado como modelo, lo es en todos los subrubros donde aparece.
    * El atributo `Trat_Fisc_Agg` **NO** es el mismo para todas los registros de un mismo vendedor. Existen vendedores que dentro de un mismo mes, venden desde el mismo depósito y dentro de un mismo subrubro, pero con más de un `Trat_Fisc_Agg`. Esto hace pensar que el tratamiento fiscal depende del cliente o de la venta en particular y no del vendedor. Se corroboró que no existe un punto de corte en `Ventas` que de lugar a estar en una u otra categoría. ¿Contradicción con el data-statement? (o mejor dicho: con la info que nos brindaron). En la categoría `Min` no hay ningún modelo (en esa categoría sólo cae 1 vendedor).
    * Ocurre lo mismo para `Trat_Fisc`. Sólo 5 de las 15 categorías presentan vendedores modelo: `3`, `1`, `0`, `Vacío` y `Norm`.
    * Para el caso de `Trat_Dif` no se presentan cambios en el atributo dentro de un mismo mes, pero sí para diferentes meses. Hay 4 categorías que no presentan vendedores modelo: artículos 16, 28, 31 y 34.
    * Un único vendedor forma parte del convenio multilateral. Sus 42 registros contienen venta nulas. Se guarda esta información en un dataset aparte y se descarta esta variable.

* Relación entre variables fiscales: nos quedamos sólo con `Trat_Fisc`.

* Serie temporal por subrubro y modelos:
    * Modelos vs tiempo (ventas totales):
        - Los valores de ventas de Modelo son cerca de la mitad de las ventas de no-Modelo.
        - Durante el confinamiento obligatorio (primera mitad de 2020) las caídas en ventas fueron muy fuertes, pero más fuertes en proporción para vendedores Modelo,
        - Si la indexación es confiable, parece que los Modelos no han recuperado sus valores de ventas previos a la Pandemia, mientas que los no-Modelo parecen estar levemente por encima.
        - A lo largo de todo el período, los no modelo lograron vender un 14% más, mientras que los modelo han bajado sus ventas en un 10%.
        - Hay menos dispersión de datos para vendedores no-modelo: ventas más consistentes o es simplemente un efecto de la mayor cantidad de datos?
        - Si nos fijamos en la comisión, si bien la pandemia afectó tanto a modelos como no modelos (ver valle en el primer semestre de 2020), los modelo han recuperado su nivel de aporte, mientras que los no modelo lo han superado. A lo largo de todo el periódo la variación de los modelo es prácticamente nula, pero la de los no modelo aumentó en un 40%.
    * Modelos vs tiempo (ventas positivas):
        - Se repite el patrón de que los valores de ventas de Modelo son cerca de la mitad de las ventas de no-Modelo.
        - Se sigue viendo el decaimiento en pandemia.
        - En todo el período, las ventas de los no modelo aumentaron un 23%, mientras que las ventas de modelo apenas disminuyeron.
        - Si nos fijamos en la comisión, se sigue viendo el efecto de la pandemia. A lo largo de todo el periódo la variación de los modelo es prácticamente nula, pero la de los no modelo aumentó en un 50%.
    * Modelos y subrubro vs tiempo (ventas totales):
        - Los valores de venta en Modelos son menores en todos los Subrubros, con la excepción de tres: "Góndola", "Comb." y "Comb. Ley".
        - En los subrubros "Vehículos", "Farmacia" y "Supermercado" los valores de ventas de modelo parecen ser despreciables en comparación con no-Modelo. Tienen valores muy bajos y con muy poca variablidad.
        - "Mantenimiento" no parece tener muchos valores Modelo, se podría descartar.
    * Modelos y subrubro vs tiempo (ventas positivas):
        - Los valores de venta en Modelos son menores en todos los Subrubros, con la excepción de tres: "Góndola" y "Comb.". Ahora "Comb. Ley" se pusieron cabeza a cabeza.
        - Se repite lo de "Vehículos", "Farmacia" y "Supermercado".
        - "Mantenimiento" no muestra ningún modelo: no hay modelos con ventas positivas en esta categoría