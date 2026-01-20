Backend de formulario de contacto (Django + Gmail SMTP)

API de contacto desarrollada con Django 5 y Django REST Framework, diseñada para recibir mensajes desde un formulario web y enviarlos de forma segura al correo electrónico mediante SMTP de Gmail.

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

5. Variables de entorno:
 
Crea un archivo .env en la raíz del proyecto

```bash

EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=tu_clave_de_aplicacion
SECRET_KEY=tu_secret_key

```
📌 Nota:
Si no defines SECRET_KEY, el proyecto funcionará en local con una clave insegura (solo para desarrollo).

6. Configuración de Gmail (SMTP)

Para que el envío de correos funcione, es obligatorio generar una clave de aplicación en tu cuenta de Google.
No se debe usar la contraseña personal de Gmail.

Pasos:

- Activa la verificación en dos pasos en tu cuenta de Google.
  
- Ve a Seguridad → Claves de aplicación.
  
- Crea una nueva clave para Correo.
  
- Copia la clave generada.
  
⚠️ Importante sobre la clave de aplicación

Google muestra la clave de aplicación separada por espacios (por ejemplo: abcd efgh ijkl mnop), pero en el archivo .env debe copiarse SIN espacios.

```bash

EMAIL_HOST_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=abcdefghijklmnop
SECRET_KEY=tu_secret_key

```

7. Ejecutar el servidor 

```bash

python manage.py runserver

```

Servidor disponible en:


👉 http://127.0.0.1:8000/api/contact/

---

🔗 Endpoints disponibles

🔹 Enviar un mensaje al correo 

POST /api/contact/

🔸 Body (JSON)

```bash

{
  "from_name": "Jorge Patricio",
  "from_email": "patogol3535@gmail.com",
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




