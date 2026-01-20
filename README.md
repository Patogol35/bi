 Contact API – Django REST Framework

API sencilla de contacto desarrollada con Django 5 y Django REST Framework, que permite recibir mensajes desde un formulario y enviarlos por correo electrónico usando SMTP de Gmail.

---

⚙️ Tecnologías utilizadas

- Python 
- Django
- Django REST Framework 
- python-dotenv
- SMTP Gmail

⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.9+

- MySQL Server

- pip (gestor de paquetes de Python)

---

🗄️ Configuración de la base de datos



📦 Instalación y ejecución 

1. Clona el repositorio:

```bash

git clone https://github.com/Patogol35/bi

```

2. Ingresa a la carpeta del proyecto

```bash

cd bi

```

3. Crea un entorno virtual e instalalo:

```bash

python -m venv venv

```

En Linux/Mac: 

```bash

source venv/bin/activate

```

En Windows: 

```bash

venv\Scripts\activate

```


4. Instala las dependencias:

```bash

pip install -r requirements.txt

```

5. Variables de entorno (.env)
Crea un archivo .env en la raíz del pro

```bash

EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_clave_de_aplicacion
SECRET_KEY=tu_secret_key

```
Nota
Para Gmail debes usar una clave de aplicación, no tu contraseña normal.
Si no defines SECRET_KEY, la app funcionará en local con una clave insegura por defecto (solo para desarrollo).

6. Endpoint disponible
POST /api/contact/
Envía un mensaje de contacto por correo.
🔸 Body (JSON)

```bash

{
  "from_name": "Jorge Patricio",
  "from_email": "jorge-pateicio@gmail.com",
  "message": "aquí escribes tu mensaje"
}

```


6. El servidor estará disponible en:

👉 http://127.0.0.1:8000


La documentación interactiva estará en:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

---

🔗 Endpoints disponibles

🔹 Crear un libro

POST /books/

Body (JSON):

{
  "title": "Las Catilinarias",
  "author": "Juan Montalvo",
  "year": 1880
}

🔹 Obtener todos los libros

GET /books/

🔹 Obtener un libro por ID

GET /books/{book_id}

Ejemplo:

/books/1

🔹 Actualizar un libro

PUT /books/{book_id}

Body (JSON):

{
  "title": "El Cosmopolita",
  "author": "Juan Montalvo",
  "year": 1886
}

🔹 Eliminar un libro

DELETE /books/{book_id}

Ejemplo:

/books/1

--- 

👨‍💻 Autor

Jorge Patricio Santamaría Cherrez
Máster en Ingeniería de Software y Sistemas Informáticos




