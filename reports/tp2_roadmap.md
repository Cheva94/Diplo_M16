> Objetivo del práctico

Generar variables que discriminen vendedores ‘modelos’ de ‘no modelos’.

¿Lo más importante del práctico? Generar gráficas donde tenga discriminado por modelo dentro de cada rubro.

> Cambio de dataset: exploración inicial

* El dataset anterior estaba mal cortado: al quedarse con Omega=1, dejaron de lado algunos vendedores modelo que eran necesarios para poder después clasificar en subrubros. Chequear que estos nuevos vendedores no sean Omega=1, entonces ya no se puede tirar esta columna (ver disclaimer). Parece que sólo se van a agregar 23 registros nuevos.

<span style="background-color: white"><span style="color:black">Hay algunos modelos que no son omega</span>

* Como va a ser un nuevo dataset, creo que deberíamos repetir algunas cosas del práctico anterior, para chequear que ciertos supuestos y resultados que vimos se sigan cumpliendo o, en caso de no hacerlo, actuar en consecuencia. Igual iría al hueso, no tan "exploratorio" ya que más o menos sabemos cómo viene la mano.

<span style="background-color: white"><span style="color:black">Parte de variables categóricas le metí bastante de análisis. Pero de cosas q no habíamos visto en el anterior TP.</span>

* En este sentido, esta primera parte incluye el `Paso 1`. Al medio hacer las discriminaciones que ya habíamos hecho antes (el CM -esto es `Paso 4`-, los nulos y los no nulos - quizás mejor positivos y negativos-, etc). Observación: quizás esta diferenciación no haga falta ahora, ya que después vamos a hacer el dataset de vendedores como registros y quizás ahí quede resumido esto. Incluso es probable que ahí la podamos entender mejor. Vendedores que tienen los 42 registros nulos: tirarlos (ojo chequear tema modelo).

* Respecto al `Paso 3` medio que ya lo hicimos al mapear el hash a un entero, no? Y tenemos el dic por si hace falta identificarlo puntualmente al vendedor. Respecto a esto me parece que dijeron que revisemos el data statement. Habla de variables demográficas: la única demográfica es la CM04 me parece. La idea de anonimizar es evitar que la identificación sea unívoca: quizás está haseado, pero es el único vendedor con ventas de un millón, entonces se puede identificar de todas formas. No es necesario borrar el registro, sino alterarlo de alguna forma que evite esta identificación unívoca. Por ejemplo, poner rango de valores (decidir granularidad).

* Para el `Paso 6` ya hicimos lo de crear la variable "Fecha". Además, ploteamos cosas agregando por años y por meses. Entiendo que refiere más a eso. Cuota es mes.

* Podemos cerrar esta primera parte con el `Paso 2`. Notas de la grabación (parte 1):
    * Me importan sólo los rubros donde sí tengo vendedores modelo dentro. Los otros ni ahí. ¿Una vez que generamos la categoría "Otros" podemos tirar todos estos registros? (de última no tirarlos y chau, sino separarlos en un dataset, por si en el futuro lo necesitamos). Lo de tirar es porque no voy a poder tener un predictor para ese rubro al no tener un modelo como guía.
    * ¿Por qué es tan importante lo de separar por subrubro? Alguien con conocimiento de dominio nos dijo que algo que diferencia las ventas son los rubros, cada uno tiene un nivel de ventas distinto. Resulta incluso más importante diferenciar por rubro que por cosas fiscales. ¿Quizás discriminar primero por rubro y dentro de cada rubro discriminar fiscalmente? Podemos hacer alguna gráfica para cada subrubro, discriminando por las variables fiscales y ahí podemos ver cuál nos da más info y decidir con cuál quedarnos. 

* El `Paso 5` nos pide que tomemos una decisión respecto a las 3 variables de tratamiento fiscal. Con lo dicho hasta ahora no sé cuál tirar y cuál quedarnos.

* Hacer de nuevo 2 notebooks? Y que todo esta primera parte vaya al uno?

> Ahora con todo el dataset nuevo y prolijito: análisis detallado

* El `Paso 7` pide graficar por subrubro la variación en el tiempo del Total de ventas, diferenciando modelos de no modelos. Notas de la grabación (parte 1):
    * Graficar series temporales por rubro y hue de modelo. Ver lo que posteo en discord. Se puede distinguir por vendedor o por algún promedio (mensual, anual, trimestral, etc). 
    * Un posibles análisis de las ventas: antes, durante y después de la pandemia. Esto sirve para enteder cuál es la situación normal y así saber cuándo se desvía (y probablemente también el por qué).

* El `Paso 8` es el de la generación de vectores. Dijeron que todo lo anterior lo podíamos dividir, pero que este estaría bueno hacerlo juntos. Notas de la grabación (parte 1):
    * Se trata de generar nuevas variables que nso sirvan para después darle de comer al modelo. Los modelos usan vectores numéricos en sus predicciones.
    * Armar sí o sí un vector con la comisión. Otro puede ser con comisiones promedio y/o con ventas. Creo que iría con comisión y con ventas.
    * Las preguntas que están ahí son disparadoras, para ayudarnos a convertir gráficas en inforamción accionable.
    * Ventas absolutas vs relativas: ver qué es lo que conviene. Lo de absolutas es tomar el valor tal cual está. Lo de relativas es tomar, por ejemeplo, los incrementos. Esto de los incrementos ya lo mencionó varias veces la Lu.
    * Todas las tendencias en las series temporales son positivas, debido a que los precios siemrpe suben: inflación. Lu decia que si bien la inlación influe, es como un serrucho creciente (pendiente constante en principio). Se pueden ver cosas raras si hay picos que sobresalen de ese serrucho. La otra es ver de normalizar por inflación. ¿Pato?
    * Volviendo a lo de los vectores. Hasta ahora el dataset que tenemos tiene registros que constan de las ventas realizadas por un vendedor en un depósito cierto mes/año. En un problema de fraudes de tarjetas de crédito lo que me importa es identificar transacciones (registros) fraudulentos. Nuestro problema es diferente: no queremos discriminar cada transacción en sospechosa o no, sino que queremos discriminar si un vendedor es sospechoso o no. Por eso necesito generar un nuevo dataset donde los registros sean los vendedores y no las transacciones: hay que hacer algún tipo de agregado sobre los datos. Este nuevo dataset será el que alimente a los modelos.
    * Para que el modelo nos responad bien tenemos que ayudarlo y direccionarlo para que sepa a qué darle bola. Acá volvió a hablar de que es mucho más importante el tema del rubro y no así la parte fiscal. 
    * Vendedores en más de un subrubro: creo que me quedaría con todos, ya que quedarse con el mayor, por ejemplo, no es fiable (volviendo a esto de que cada rubro maneja diferentes volúmenes de dinero).
    * Vendedores con más de un depósito: me inclinaría por quedarme con todos sus depósitos, tomando un promedio de sus ventas en cada uno de ellos.

* Los `Pasos 9-11` medio que van en una misma línea y se basan en lo que hayamos hecho en el `Paso 8`. Notas de la grabación (parte 1):
    * El `Paso 9` y el `Paso 10` son "el comportamiento del comportamiento", ya que es la varianza y la media de ese vendedor a lo largo de **TODA** la serie temporal. Medio que es buscarle la tendencia central y la dispersión a cada vendedor a lo largo de todo el período bajo análisis.

> Notas que no sabía dónde ponerlas

* Según negocio las variables que más le importan son ventas y comisión (cambiar nombre a "Recaudación", creo que me gusta más). Esto hace que la "serie temporal principal" pueda ser alguna de estas dos.

* Se le puede llegar a dar un tratamiento más de clasificación (AS) o cluster (AnS) que de series temporales.

* Este problema no está bueno para redes neuronales, donde pierdo info del por qué. Acá yo quiero tener inforamción de por qué tal persona es o no riesgosa, para poder después justificar en términos de negocio y legales.

> Cosas que quedaron en el tintero del práctico anterior

* Qué vendedores se agrupan en qué depositos.

* Tema de los tratamientos fiscales: ¿Se puede unificar todo como `Trat_Fisc`, eliminando entonces `Trat_Fisc_Agg`? ¿Tiene sentido que falte la descripción asociada al tratamiento?

* Analizando los porcentajes de comisión, ¿tiene sentido que haya porcentajes nulos? Puede deberse a algo fiscal

* Hay que decidir sobre las variables numéricas:
    * Qué hacemos con valores negativos.
    * Qué hacemos con valores nulos.
    * Si truncamos valores extremos y, en caso afirmativo, la manera/los límites.