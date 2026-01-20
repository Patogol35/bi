 Backend para formulario de contacto al correo electrónico 

API sencilla de contacto desarrollada con Django 5 y Django REST Framework, que permite recibir mensajes desde un formulario y enviarlos por correo electrónico usando SMTP de Gmail.

---

⚙️ Tecnologías utilizadas

- Python 
- Django
- Django REST Framework 
- python-dotenv
- SMTP Gmail

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

6. El servidor estará disponible en:

👉 http://127.0.0.1:8000

---

🔗 Endpoints disponibles

🔹 Enviar un mensaje al correo 

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
Respuesta exitosa

```bash
{
  "success": "Mensaje enviado correctamente"
}

```
❌ Error (campos faltantes)

```bash
{
  "error": "Todos los campos son obligatorios"
}
```
--- 

👨‍💻 Autor

Jorge Patricio Santamaría Cherrez
Máster en Ingeniería de Software y Sistemas Informáticos




