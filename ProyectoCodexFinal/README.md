# Practica API con FastAPI, pandas y web

Proyecto pequeno pero con estructura real para aprender a crear una API en Python que lee datos con pandas y los muestra en una pagina web.

## Que contiene

- `app/main.py`: punto de entrada de FastAPI.
- `app/api/routes.py`: endpoints HTTP de la API.
- `app/services/sales_service.py`: logica de negocio y lectura de datos con pandas.
- `app/schemas/sales.py`: modelos de respuesta con Pydantic.
- `app/core/config.py`: configuracion centralizada.
- `app/web/`: pagina HTML, CSS y JavaScript que consume la API.
- `data/sales.csv`: datos de ejemplo.
- `tests/`: pruebas automaticas basicas.

## Instalacion en Windows

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Ejecutar

```powershell
.\.venv\Scripts\python -m uvicorn app.main:app --reload
```

Abre:

- Web: http://127.0.0.1:8000
- Documentacion API: http://127.0.0.1:8000/docs

## Endpoints principales

- `GET /api/health`: comprueba que la API esta viva.
- `GET /api/sales`: devuelve ventas.
- `GET /api/sales/summary`: devuelve resumen de ventas.
- `GET /api/sales/by-product`: agrupa ventas por producto.
- `GET /api/sales/by-region`: agrupa ventas por region.

Ejemplo:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/api/sales?region=Madrid&limit=5"
```

## Ideas clave que debes entender

1. FastAPI recibe peticiones HTTP y llama a funciones Python.
2. pandas lee el CSV y permite filtrar, agrupar y calcular totales.
3. Pydantic define la forma de los datos que devuelve la API.
4. JavaScript usa `fetch()` para pedir datos a la API y pintarlos en HTML.
5. La estructura separa responsabilidades para que el proyecto pueda crecer.

Lee tambien `docs/estructura.md` para entender el recorrido completo de una peticion.

Para estudiar paso a paso, sigue `docs/guia_aprendizaje.md`.

## Ejecutar pruebas

```powershell
.\.venv\Scripts\python -m pytest
```
