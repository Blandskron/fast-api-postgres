# FastAPI CRUD con PostgreSQL

Este proyecto es una API RESTful construida con **FastAPI** y **PostgreSQL**. Permite realizar operaciones CRUD (Create, Read, Update, Delete) sobre una tabla de estudiantes, conectada a una base de datos PostgreSQL.

## Características

- Crear nuevos estudiantes.
- Leer todos los estudiantes o un estudiante en particular por su ID.
- Actualizar la información de un estudiante existente.
- Eliminar un estudiante por su ID.
- Documentación interactiva generada automáticamente con **Swagger UI** y **ReDoc**.

---

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

- Python 3.8 o superior.
- PostgreSQL.
- pip (administrador de paquetes de Python).

---

## Configuración

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd fast-api-postgres
```

### 2. Crear un entorno virtual
```bash
python -m venv env
source env/bin/activate # Linux/macOS
env\Scripts\activate    # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
Asegúrate de que tu servidor PostgreSQL esté en funcionamiento y crea una base de datos llamada `escuela_fastapi`:

```sql
CREATE DATABASE escuela_fastapi;
```

Configura las credenciales de conexión en el archivo `.env`:

```plaintext
DATABASE_URL=postgresql://postgres:admin1234@localhost:5432/escuela_fastapi
```

### 5. Iniciar el servidor
Ejecuta el siguiente comando para iniciar la API:

```bash
uvicorn app.main:app --reload
```

Accede a la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Endpoints

| Método   | Endpoint             | Descripción                              |
|----------|----------------------|------------------------------------------|
| **GET**  | `/students/`         | Lista todos los estudiantes.             |
| **GET**  | `/students/{id}`     | Obtiene un estudiante por su ID.         |
| **POST** | `/students/`         | Crea un nuevo estudiante.                |
| **PUT**  | `/students/{id}`     | Actualiza un estudiante existente.       |
| **DELETE**| `/students/{id}`    | Elimina un estudiante por su ID.         |

---

## Estructura del Proyecto

```plaintext
fast-api-postgres/
├── app/
│   ├── __init__.py
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── config.py         # Configuración de la base de datos
│   ├── database.py       # Configuración de la conexión a PostgreSQL
│   ├── models.py         # Definición de los modelos (ORM)
│   ├── schemas.py        # Validaciones con Pydantic
│   ├── crud.py           # Lógica CRUD
│   └── routers/
│       └── students.py   # Rutas relacionadas con estudiantes
├── .env                  # Variables de entorno
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación
```

---

## Dependencias

- **FastAPI**: Framework para construir APIs rápidas y modernas.
- **SQLAlchemy**: ORM para manejar la base de datos.
- **Pydantic**: Validaciones de datos.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **psycopg2**: Conector de PostgreSQL para Python.

Instálalas con:
```bash
pip install -r requirements.txt
```

---

## Pruebas

1. Inicia el servidor con:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Accede a la documentación interactiva:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

3. Prueba los endpoints directamente desde la documentación o usando herramientas como **Postman** o **cURL**.

---

## Contribución

Si deseas contribuir a este proyecto, sigue los pasos a continuación:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y haz un commit:
   ```bash
   git commit -m "Añadir nueva funcionalidad"
   ```
4. Sube los cambios a tu rama:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un Pull Request en GitHub.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

¡Gracias por usar esta API! Si tienes preguntas o problemas, no dudes en contactarme. 😊
