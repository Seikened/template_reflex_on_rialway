import reflex as rx
import os

# Usa manualmente el dominio público de Railway
public_domain = "www.fer-blog.leonesfrancos.com"

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="plantilla",
    show_built_with_reflex=True,
    telemetry_enabled=False,
    frontend_port=3000,  # default frontend port
    backend_port=8000,  # default backend port
    # Usa el dominio público en producción
    api_url=f'https://{public_domain}/backend' if os.getenv("RAILWAY_ENVIRONMENT") == "production" else "http://127.0.0.1:8000"
)
