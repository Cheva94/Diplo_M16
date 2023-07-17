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
    * Existen 26 registros con ventas negativas asociadas a comisiones nulas. De éstos, 25 tienen comisión nula y uno tiene comisión del 0.18%. Como en todos los casos son ventas negativas, puede ser que esta sea la razón de tener una comisión nula. Ninguno de estos 26 registros corresponde a vendedor modelo.
    * Hay 2232 registros con ventas positivas asociadas a comisiones nulas. De éstos:
        * 34 registros corresponden a vendedores modelo.
        * 1458 registros con alícuota nula.
        * 774 registros con alícuota no nula.
    * No hay ningún modelo con ventas nulas: la mayoría de sus registros son ventas positivas, aunque hay algunos con ventas negativas.
    * Todos los modelos tienen alícuotas bajas (muy ceranas al 0%). Hay 5374 registros asociados a vendedores modelo y sus alícuotas van desde 0.0084% hasta 3.25%. Sin embargo, la mayoría se concentra en alícuotas menores a 0.075 %, teniendo un pico en 0.05%.
* Relación $\text{Comision} = \text{Alicuota} \times \text{Ventas}$:
    * En las ventas negativas, el 97.65% de los registros **NO** cumplen la relación: el 96.19% de los registros la subestiman. Todos los que no cumplen caen en el caso *pendiente grande*. Ni se perciben los modelo dentro de estos registros.

* Respecto a chequear unicidad (vars cat):
    * Existen vendedores modelo que participan en más de un subrubro. Si un vendedor es calificado como modelo, lo es en todos los subrubros donde aparece.
    * El atributo `Trat_Fisc_Agg` **NO** es el mismo para todas los registros de un mismo vendedor. Existen vendedores que dentro de un mismo mes, venden desde el mismo depósito y dentro de un mismo subrubro, pero con más de un `Trat_Fisc_Agg`. Esto hace pensar que el tratamiento fiscal depende del cliente o de la venta en particular y no del vendedor. Se corroboró que no existe un punto de corte en `Ventas` que de lugar a estar en una u otra categoría. ¿Contradicción con el data-statement? (o mejor dicho: con la info que nos brindaron). En la categoría `Min` no hay ningún modelo (en esa categoría sólo cae 1 vendedor).
    * Ocurre lo mismo para `Trat_Fisc`. Sólo 5 de las 15 categorías presentan vendedores modelo: `3`, `1`, `0`, `Vacío` y `Norm`.
    * Para el caso de `Trat_Dif` no se presentan cambios en el atributo dentro de un mismo mes, pero sí para diferentes meses. Hay 4 categorías que no presentan vendedores modelo: artículos 16, 28, 31 y 34.
    * Un único vendedor forma parte del convenio multilateral. Sus 42 registros contienen venta nulas. Se guarda esta información en un dataset aparte y se descarta esta variable.

* Relación entre variables fiscales: nos quedamos sólo con `Trat_Fisc`.

* 