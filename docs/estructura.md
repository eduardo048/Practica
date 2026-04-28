# Estructura mental del proyecto

Este proyecto no esta montado como un script unico porque una API real necesita separar responsabilidades.

## Recorrido de una peticion

1. El navegador abre `http://127.0.0.1:8000`.
2. `app/main.py` sirve `app/web/index.html`.
3. `app/web/app.js` hace peticiones con `fetch()` a `/api/sales`, `/api/sales/summary` y `/api/sales/by-product`.
4. `app/api/routes.py` recibe esas peticiones HTTP.
5. Cada ruta llama a `SalesService`.
6. `app/services/sales_service.py` lee `data/sales.csv` con pandas.
7. pandas filtra, agrupa y calcula campos como `total`.
8. `app/schemas/sales.py` define que forma debe tener la respuesta.
9. FastAPI convierte la respuesta a JSON.
10. JavaScript pinta ese JSON en la tabla y en las metricas.

## Que debes mirar primero

1. `app/main.py`: como nace la aplicacion.
2. `app/api/routes.py`: como se definen endpoints y parametros.
3. `app/services/sales_service.py`: como pandas prepara los datos.
4. `app/schemas/sales.py`: como se documenta y valida la salida.
5. `app/web/app.js`: como la web consume la API.

## Conceptos importantes

- Endpoint: una URL que ejecuta una funcion, por ejemplo `/api/sales`.
- Query parameter: dato que viaja en la URL, por ejemplo `?region=Madrid`.
- DataFrame: tabla de pandas cargada desde CSV, Excel, base de datos, etc.
- Schema: contrato de datos que dice que campos devuelve la API.
- Service: clase donde va la logica de negocio para no ensuciar las rutas.
- Test: prueba automatica que confirma que algo sigue funcionando.

## Ejercicios para practicar

1. Crear un endpoint `/api/sales/by-category`.
2. Anadir filtros por fecha inicial y fecha final.
3. Cambiar el CSV por un Excel con `pd.read_excel`.
4. Crear una columna nueva de margen o beneficio.
5. Sustituir el CSV por una base de datos cuando entiendas bien este flujo.

