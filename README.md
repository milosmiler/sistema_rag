# Sistema RAG — Paso 1

Base del backend construida con Python, FastAPI, PostgreSQL y Docker.

## Requisitos

- Docker Desktop instalado y en ejecución.
- Python 3.12 o compatible para ejecutar las pruebas fuera de Docker.

## Iniciar el proyecto

Desde la carpeta raíz del proyecto ejecuta:

```bash
docker compose up -d --build
```

Servicios disponibles:

- API: http://localhost:8000
- Health check: http://localhost:8000/api/health
- Documentación Swagger: http://localhost:8000/docs
- PostgreSQL: `127.0.0.1:5433`

La ruta de salud debe responder:

```json
{
## Conexión a PostgreSQL

Para conectarte desde DBeaver u otra herramienta utiliza:

```text
Host:       127.0.0.1
Port:       5433
Database:   rag_db
Username:   rag_user
Password:   rag_password
```

La API se conecta internamente usando el servicio Docker `db` en el puerto `5432`.

## Volumen de PostgreSQL

Los datos se guardan en el volumen Docker `postgres_data`. Las variables
`POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB` solo se aplican cuando el
volumen se inicializa por primera vez.

Si necesitas reinicializar la base de datos desde cero, detén los servicios y
elimina el volumen:

```bash
docker compose down -v
  "service": "rag-api"
```

> `docker compose down -v` elimina todos los datos almacenados en PostgreSQL.

## Detener el proyecto
}
Para detener los contenedores sin eliminar los datos:

## Detener el proyecto

En la terminal donde se está ejecutando presiona `Ctrl + C`. Después puedes usar:

```bash
docker compose down
```

python3 -m venv .venv

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

En Windows, activa el entorno con `.venv\\Scripts\\activate`.

## Estructura actual

```text
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── documents.py
│   │   │       └── health.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   └── document.py
│   │   ├── schemas/
│   │   │   └── document.py
│   │   ├── services/
│   │   │   └── document_service.py
│   │   └── main.py
│   ├── tests/
│   │   └── test_health.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── requirements-dev.txt
├── docker-compose.yml
└── README.md
```
