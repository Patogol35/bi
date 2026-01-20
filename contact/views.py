from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


@api_view(["POST"])
def contact_view(request):
    name = request.data.get("from_name")
    email = request.data.get("from_email")
    message = request.data.get("message")

    if not name or not email or not message:
        return Response(
            {"error": "Todos los campos son obligatorios"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Validar email
    try:
        validate_email(email)
    except ValidationError:
        return Response(
            {"error": "Email inválido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    full_message = (
        f"Nombre: {name}\n"
        f"Email: {email}\n\n"
        f"Mensaje:\n{message}"
    )

    try:
        send_mail(
            subject="Nuevo mensaje desde el portafolio",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            reply_to=[email],
            fail_silently=False,
        )
    except Exception as e:
        return Response(
            {"error": "Error al enviar el correo"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return Response(
        {"success": "Mensaje enviado correctamente"},
        status=status.HTTP_200_OK,
    )
