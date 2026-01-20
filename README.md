Backend de formulario de contacto (Django + Gmail SMTP)

API sencilla de contacto desarrollada con Django 5 y Django REST Framework, que permite recibir mensajes desde un formulario y enviarlos directamente al correo electrónico utilizando SMTP de Gmail.

---

⚙️ Tecnologías utilizadas

- Python 
- Django
- Django REST Framework 
- python-dotenv
- SMTP (Gmail)

---


📦 Instalación y ejecución 

1. Clona el repositorio:

```bash

https://github.com/Patogol35/contacto-backend-gmail/

```

2. Ingresa a la carpeta del proyecto

```bash

cd contacto-backend-gmail/

```

3. Crea y activa un entorno virtual:

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

5. Variables de entorno 
Crea un archivo .env en la raíz del pro

```bash

EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_clave_de_aplicacion
SECRET_KEY=tu_secret_key

```
📌 Nota:
Para Gmail es obligatorio usar una clave de aplicación, no tu contraseña personal.
Si no defines SECRET_KEY, el proyecto funcionará en local con una clave insegura (solo para desarrollo).

6. Ejecutar el servidor 

```bash

python manage.py runserver

```

Servidor disponible en:


👉 http://127.0.0.1:8000

---

🔗 Endpoints disponibles

🔹 Enviar un mensaje al correo 

POST /api/contact/

🔸 Body (JSON)

```bash

{
  "from_name": "Jorge Patricio",
  "from_email": "jorge-pateicio@gmail.com",
  "message": "aquí escribes tu mensaje"
}

```
Respuesta exitosa


{
  "success": "Mensaje enviado correctamente"
}


Error (campos faltantes)


{
  "error": "Todos los campos son obligatorios"
}

--- 

👨‍💻 Autor

Jorge Patricio Santamaría Cherrez
Máster en Ingeniería de Software y Sistemas Informáticos




