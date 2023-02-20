import random
import string
from django.apps import AppConfig
from django.contrib.auth import get_user_model


class ProjetosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projetos'

    def ready(self):
        import os

        User = get_user_model()

        email= os.getenv("EMAIL_ADMIN")
        senha = os.getenv("SENHA_ADMIN")

        usuarios = User.objects.filter(email=email)

        if not usuarios:
            username = 'admin-' + ''.join(random.choices(string.ascii_lowercase, k=5))
            User.objects.create_superuser(username=username, email=email, password=senha, is_active=True, is_staff=True)
