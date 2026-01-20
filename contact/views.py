from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings


@api_view(["POST"])
def contact_view(request):
    name = request.data.get("from_name")
    email = request.data.get("from_email")
    message = request.data.get("message")

    if not all([name, email, message]):
        return Response(
            {"error": "Todos los campos son obligatorios"},
            status=400,
        )

    full_message = (
        f"Nombre: {name}\n"
        f"Email: {email}\n\n"
        f"Mensaje:\n{message}"
    )

    send_mail(
        subject="Nuevo mensaje desde el portafolio",
        message=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )

    return Response({"success": "Mensaje enviado correctamente"})
