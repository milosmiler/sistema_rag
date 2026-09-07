# Sistema RAG

Backend de un sistema RAG construido con Python y FastAPI.

## Arquitectura

La aplicación sigue una arquitectura modular por capas:

- **API:** rutas HTTP y documentación de la API.
- **Schemas:** validación y serialización de datos.
- **Services:** lógica de negocio y casos de uso.
- **Models:** entidades persistentes.
- **Database:** sesiones, configuración de acceso y migraciones Alembic.
- **Core:** configuración general de la aplicación.
- **Infraestructura:** Docker Compose para ejecutar la API y PostgreSQL.

El flujo principal es:

```text
Cliente -> API -> Services -> Database
                    |
                 Schemas
```

## Ejecución en desarrollo

### Requisitos

- Docker Desktop.
- Python 3.12 o compatible para ejecutar pruebas localmente.

### Levantar los servicios

Desde la raíz del proyecto:

```bash
docker compose up --build
```

La API expone sus rutas y la documentación interactiva de FastAPI durante la
ejecución del entorno de desarrollo.

Para ejecutar los servicios en segundo plano:

```bash
docker compose up -d --build
```

Para revisar el estado:

```bash
docker compose ps
```

Para detener los servicios sin eliminar los datos persistidos:

```bash
docker compose down
```

La configuración sensible debe gestionarse mediante variables de entorno y no
debe publicarse en el repositorio.

### Ejecutar pruebas localmente

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

En Windows, activa el entorno con:

```text
.venv\\Scripts\\activate
```

## Estructura principal

```text
.
├── backend/
│   ├── app/
│   │   ├── api/routes/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── alembic/
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── requirements-dev.txt
├── docker-compose.yml
└── README.md
```
