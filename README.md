# Mi primera app con Streamlit · Una semana en la heladería

si mañana hace 28 °C, ¿qué día de nuestra tabla mirarías para decidir cuántos helados preparar?

En 50 minutos vas a convertir una tabla de siete filas en una página que responde cuando eliges un sabor. Solo necesitas una cuenta de GitHub, un navegador y saber copiar, pegar y guardar. Streamlit convierte instrucciones de Python en elementos de una página. Hoy vas a escribir esas instrucciones de una en una y comprobar su efecto.

[Abrir la clase en GitHub Codespaces](https://codespaces.new/I-say/clase-streamlit)

## 1. Abre tu primera página · 8 minutos

1. Entra al repositorio del taller con tu cuenta de GitHub. Pulsa **Code → Codespaces → Create codespace on main**. Si ya abriste tu espacio, selecciónalo en esa misma lista.
2. Espera a que termine la preparación. A la izquierda están los archivos. Abre **practica.py**. Las tres líneas que ves importan Streamlit, dibujan un título y escriben una pregunta. El nombre corto `st` sirve para llamar a Streamlit.
3. En **Terminal → New Terminal**, pega esta orden y pulsa Enter. Deja esa terminal abierta mientras trabajas.

   ```sh
   python -m streamlit run practica.py --server.address=0.0.0.0 --server.port=8501
   ```

4. Pulsa **Open in Browser** en el aviso. También puedes abrir la pestaña **Ports / Puertos** junto a la terminal y pulsar el icono de globo del puerto **8501**. Tendrás dos pestañas, el editor y tu página.
5. En el editor, cambia `Mi primera heladería` por el nombre de tu heladería. Conserva las comillas. Guarda con **Ctrl+S** o **⌘S**. Vuelve a la página y pulsa **Rerun** si aparece. Si eliges **Always rerun**, se actualizará con cada cambio guardado.

**Comprueba:** el título de tu página muestra el nombre que elegiste.

## 2. Lee los siete días · 7 minutos

Abre **helados.csv**. Un CSV es una tabla escrita como texto. Las comas separan columnas. Debajo del encabezado, la fila `1,22,8,6` dice que el día 1 hubo 22 °C y se vendieron 8 helados de vainilla y 6 de chocolate. Son datos inventados para la práctica.

Vuelve a **practica.py**. A partir de aquí, **añade cada bloque al final del archivo**, en el orden de la guía. Guarda y mira la página después de cada bloque. Copia solo el código que aparece en el recuadro.

```python
import pandas as pd

datos = pd.read_csv("helados.csv")
st.dataframe(datos, hide_index=True)
```

`pandas` lee tablas. Le damos el nombre corto `pd`. El signo `=` guarda la tabla con el nombre `datos` para volver a usarla. Busca el día 6 en la tabla de tu página. Deberías ver **30 °C, 18 de vainilla y 15 de chocolate**.

## 3. Dibuja cinco gráficas · 22 minutos

### Barras · Compara días

```python
sabor = st.selectbox("Elige un sabor", ["vainilla", "chocolate"])
st.subheader("Ventas por día")
horizontal = st.checkbox("Ver barras horizontales")
st.bar_chart(datos, x="dia", y=sabor, horizontal=horizontal)
```

El menú guarda la opción elegida en `sabor`. Al principio, `x` coloca los días de izquierda a derecha e `y` indica la altura según las ventas. **Prueba:** elige chocolate y activa la casilla. ¿Qué barra llega más lejos? La del día 6, con 15. Al usar el menú, Streamlit vuelve a leer el programa de arriba abajo con tu nueva elección.

### Líneas · Sigue dos sabores a la vez

```python
st.subheader("La semana de cada sabor")
st.line_chart(datos, x="dia", y=["vainilla", "chocolate"])
```

Los corchetes reúnen dos columnas y cada una se convierte en una línea. **Prueba:** cambia temporalmente la lista por `["chocolate"]`, guarda y observa cuántas líneas quedan. Después recupera la lista original. ¿En qué día casi se tocan? El día 5, con 12 y 11.

### Puntos · Relaciona temperatura y ventas

```python
st.subheader("Temperatura y ventas")
st.scatter_chart(datos, x="temperatura", y=sabor)
```

Cada punto es un día. **Prueba:** selecciona vainilla y busca el punto más a la derecha. A 30 °C se vendieron 18. Cambia a chocolate. El punto sigue en 30 °C y baja a 15. Estos siete días permiten describir lo que ocurrió. Para pronosticar otras semanas necesitaríamos más datos.

### Área · Suma ambos sabores

```python
datos["total"] = datos["vainilla"] + datos["chocolate"]
st.subheader("Total diario")
st.area_chart(datos, x="dia", y="total")
```

Las comillas dentro de los corchetes identifican una columna. Aquí creamos `total` sumando los dos sabores **en cada fila**. El primer día tiene 14 helados. **Prueba:** sustituye `y="total"` por `y="vainilla"`. ¿A qué altura empieza ahora el área? A 8. Vuelve a poner `y="total"`.

### Línea acumulada · Lleva la cuenta de la semana

```python
datos["acumulado"] = datos[sabor].cumsum()
st.subheader("Ventas acumuladas del sabor elegido")
st.line_chart(datos, x="dia", y="acumulado")
```

`cumsum()` suma lo vendido hoy a lo que ya llevábamos. Para vainilla, los primeros tres puntos son **8, 18 y 27**. **Prueba:** cambia el menú a chocolate. ¿Cuántos helados llevábamos al cierre del día 7? El último punto marca **69**. Con vainilla marca **86**.

## 4. Reto · Predice antes de guardar · 8 minutos

En **helados.csv**, cambia las ventas de chocolate del día 7 de 12 a 14. Antes de guardar, anota qué esperas que pase en las barras de vainilla, el área del total diario y la línea acumulada de chocolate. Guarda el CSV y cambia de sabor en la app para que vuelva a leerlo.

**Comprueba tu predicción:** las barras de vainilla conservan sus valores. El total del día 7 pasa de 27 a 29 y el acumulado de chocolate termina en 71. Devuelve el 14 a 12 y cambia el menú otra vez para recuperar el ejemplo original.

## 5. Cierre y solución de referencia · 5 minutos

Explica con tus palabras qué representa un punto de la gráfica de temperatura y qué representa el último punto de la línea acumulada. Luego responde la pregunta inicial. En nuestra tabla, el día 7 tuvo 28 °C y se vendieron 15 de vainilla y 12 de chocolate. Esa observación sirve como referencia para planear.

**app.py** contiene el ejemplo completo y comentado. Para verlo, haz clic en la terminal donde corre la práctica, pulsa **Ctrl+C** y ejecuta:

```sh
python -m streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

Abre otra vez el puerto 8501. Cuando termines la clase, ve a [tus Codespaces](https://github.com/codespaces), abre el menú **…** de tu espacio y elige **Stop codespace** para detenerlo.

## Si algo se atora

| Lo que ves | Qué hacer |
|---|---|
| Aparece `No module named streamlit` | En la terminal ejecuta `python -m pip install -r requirements.txt`. Espera a que termine y repite la orden de arranque. |
| Falta `helados.csv` o `practica.py` | Escribe `pwd` y `ls` en la terminal. Debes estar en la carpeta que contiene ambos archivos. Si los subiste dentro de otra carpeta, entra con `cd nombre-de-la-carpeta`. |
| No se abrió la página | En **Ports / Puertos**, busca 8501. Si falta, pulsa **Forward a Port**, escribe 8501 y abre el globo. Mantén el programa en ejecución. |
| Aparece un error después de pegar código | Mira la línea que señala el mensaje. Comprueba comillas, paréntesis y nombres de columnas. En el código, `dia` se escribe sin acento, tal como figura en el CSV. |
| El puerto ya está en uso | En la terminal de la app anterior pulsa **Ctrl+C** antes de lanzar la siguiente. |

Consulta las [gráficas de Streamlit](https://docs.streamlit.io/develop/api-reference/charts) y la [guía de puertos de GitHub Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
