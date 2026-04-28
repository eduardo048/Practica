# Guia de aprendizaje: Python para APIs, pandas y web

Esta guia esta pensada para alguien que ya sabe programar en Java, C, C++ y lenguajes de marcas. No empieza desde "que es una variable", sino desde como se trabaja en Python de forma practica.

La forma de usarla sera por fases. Cuando acabes una fase, me dices: "pasamos a la siguiente fase", y seguimos con ejercicios concretos.

## Fase 1: Python basico aplicado

Objetivo: entender la sintaxis esencial de Python comparandola con lenguajes que ya conoces.

Debes dominar:

- `def` para crear funciones.
- Indentacion en lugar de llaves.
- Tipos basicos: `str`, `int`, `float`, `bool`, `list`, `dict`, `tuple`.
- Condicionales: `if`, `elif`, `else`.
- Bucles: `for`, `while`.
- `return`.
- Importaciones: `import`, `from ... import ...`.
- F-strings: `f"Hola {nombre}"`.

Ejercicios:

1. Crear una funcion que reciba dos numeros y devuelva suma, resta, multiplicacion y division.
2. Crear una lista de productos y recorrerla con `for`.
3. Crear una lista de diccionarios simulando ventas.
4. Filtrar ventas por region usando una funcion.

Resultado esperado:

Saber leer funciones Python sin perderte con la sintaxis.

## Fase 2: Estructura de proyecto Python

Objetivo: dejar de trabajar con scripts sueltos y entender una estructura real.

Debes dominar:

- Que es un modulo.
- Que es un paquete.
- Para que sirve `__init__.py`.
- Como se organizan carpetas.
- Que es un entorno virtual `.venv`.
- Que es `requirements.txt`.
- Como ejecutar codigo desde terminal.

Ejercicios:

1. Crear una carpeta `scripts`.
2. Crear un archivo `scripts/practica_funciones.py`.
3. Importar una funcion desde otro archivo.
4. Ejecutar el archivo desde PowerShell.

Resultado esperado:

Entender por que el proyecto tiene carpetas como `app/api`, `app/services` y `app/schemas`.

## Fase 3: pandas desde cero practico

Objetivo: cargar datos, filtrarlos y transformarlos.

Debes dominar:

- `pd.read_csv`.
- Que es un `DataFrame`.
- Ver filas con `.head()`.
- Ver columnas con `.columns`.
- Filtrar filas.
- Crear columnas nuevas.
- Agrupar con `.groupby()`.
- Ordenar con `.sort_values()`.
- Convertir datos a diccionarios con `.to_dict()`.

Ejercicios:

1. Leer `data/sales.csv`.
2. Mostrar las primeras 5 ventas.
3. Crear una columna `total`.
4. Filtrar ventas de Madrid.
5. Agrupar ingresos por producto.
6. Agrupar ingresos por region.

Resultado esperado:

Entender el archivo `app/services/sales_service.py`.

## Fase 4: API minima con FastAPI

Objetivo: crear endpoints simples antes de mezclarlo con pandas.

Debes dominar:

- Crear una app con `FastAPI()`.
- Crear rutas con `@app.get()`.
- Devolver diccionarios y listas.
- Query parameters.
- Ejecutar con `uvicorn`.
- Ver `/docs`.

Ejercicios:

1. Crear endpoint `/hola`.
2. Crear endpoint `/suma?a=2&b=3`.
3. Crear endpoint `/productos`.
4. Crear endpoint `/productos?categoria=...`.

Resultado esperado:

Entender como una URL termina ejecutando una funcion Python.

## Fase 5: API + pandas

Objetivo: conectar FastAPI con datos reales.

Debes dominar:

- Leer CSV dentro de una funcion.
- Devolver datos de pandas como JSON.
- Filtrar usando parametros HTTP.
- Separar rutas y servicios.

Ejercicios:

1. Crear `/api/sales`.
2. Crear `/api/sales?region=Madrid`.
3. Crear `/api/sales/summary`.
4. Crear `/api/sales/by-product`.
5. Crear `/api/sales/by-category`.

Resultado esperado:

Entender el flujo completo entre `routes.py` y `sales_service.py`.

## Fase 6: Pydantic y contratos de datos

Objetivo: definir claramente que devuelve la API.

Debes dominar:

- `BaseModel`.
- Campos tipados.
- `response_model`.
- Validacion de salida.
- Documentacion automatica en `/docs`.

Ejercicios:

1. Crear un modelo `Product`.
2. Crear un modelo `Sale`.
3. Usar `response_model=list[Sale]`.
4. Probar que `/docs` muestra el contrato correcto.

Resultado esperado:

Entender `app/schemas/sales.py`.

## Fase 7: Web consumiendo la API

Objetivo: pintar en HTML los datos que vienen de FastAPI.

Debes dominar:

- `fetch()`.
- JSON.
- Manipular el DOM.
- Pintar tablas.
- Enviar filtros desde inputs.

Ejercicios:

1. Hacer `fetch("/api/sales")`.
2. Pintar una tabla de ventas.
3. Crear un filtro por region.
4. Crear metricas resumen.

Resultado esperado:

Entender `app/web/app.js`.

## Fase 8: Proyecto pequeno completo

Objetivo: construir una version simple desde cero sin copiar la actual.

Proyecto:

Crear una API de productos con ventas.

Debe tener:

- CSV propio.
- Endpoint para listar datos.
- Endpoint de resumen.
- Endpoint agrupado por categoria.
- Pagina web con tabla.
- Filtro por categoria.

Resultado esperado:

Ser capaz de crear una primera API real sin depender de una plantilla.

## Fase 9: Buenas practicas reales

Objetivo: acercarte a estructura profesional.

Debes dominar:

- Tests con `pytest`.
- Variables de entorno.
- Manejo de errores.
- Separacion de capas.
- Logs basicos.
- Preparacion para base de datos.

Ejercicios:

1. Test para `/api/health`.
2. Test para `/api/sales/summary`.
3. Error claro si falta el CSV.
4. Configurar ruta del CSV con `DATA_FILE`.

Resultado esperado:

Entender que una API no solo debe funcionar, tambien debe ser mantenible.

## Orden recomendado

No saltes directamente a FastAPI si todavia no lees bien funciones, imports, listas y diccionarios en Python. Como ya sabes programar, la parte basica sera rapida, pero conviene hacerla bien porque todo FastAPI se apoya en funciones, tipos y diccionarios.

Cada fase deberia terminar con codigo escrito por ti, no solo leido.

