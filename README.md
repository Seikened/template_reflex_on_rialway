# Template para Desplegar un Proyecto Reflex en Railway

> **Aviso ⚠️**  
> **Este proyecto no es de mi autoría.** Lo encontré en un tutorial (del cual no recuerdo todos los detalles) y lo adapté para facilitar el despliegue. Existe otro template similar en Railway. Utilízalo como punto de partida y, si encuentras algún problema, contribuye con mejoras.

---

## 1. Requisitos Previos 🚀

- **Cuenta en Railway:** Asegúrate de tener una cuenta activa en Railway.  
- **Configuración Local:** Tu proyecto Reflex debe ejecutarse correctamente en local.  
- **Repositorio en GitHub:** Tu proyecto debe estar alojado en GitHub para poder desplegarlo en Railway.

---

## 2. Configuración del Proyecto 🛠️

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/Seikened/template_reflex_on_rialway
   ```

2. **Renombrar y Organizar:**  
   Una vez descargado, renombra la carpeta de la aplicación para que coincida con el nombre de tu proyecto. Por ejemplo, si la carpeta actual se llama `plantilla`, cámbiala por el nombre deseado. Actualiza también el archivo principal (por ejemplo, `plantilla.py`) según corresponda.

3. **Integrar Tu Aplicación:**  
   Si tu proyecto ya tiene estructura (assets, configuraciones personalizadas, etc.), reemplaza la carpeta `plantilla` por la carpeta de tu proyecto. Asegúrate de migrar cualquier configuración de tu `rxconfig.py` a esta plantilla de configuración.

---

## 3. Configuración 📄

A continuación, se muestra un ejemplo de configuración utilizando Reflex:

```python
import reflex as rx
import os

"""
Utiliza el dominio público proporcionado por Railway o tu propio dominio (configurado en Railway)
"""
public_domain = "www.change-me.com"

class ReflextemplateConfig(rx.Config):
    pass

config = ReflextemplateConfig(
    app_name="plantilla",  # Cambia 'plantilla' por el nombre de tu proyecto
    show_built_with_reflex=True,
    telemetry_enabled=False,
    frontend_port=3000,  # Puerto frontend por defecto
    backend_port=8000,   # Puerto backend por defecto
    # Utiliza el dominio público en producción
    api_url=f'https://{public_domain}/backend' if os.getenv("RAILWAY_ENVIRONMENT") == "production" else "http://127.0.0.1:8000"
)
```

> **Consejo 💡:**  
> Actualiza **app_name** y **public_domain** para que reflejen tu proyecto y asegúrate de que la configuración coincida con la estructura de tu aplicación.

---

## 4. Variables de Entorno y Configuración en Railway 🌐

1. **Configurar Variables de Entorno:**  
   Antes de desplegar, crea una variable en Railway:

   ```env
   ENV="prod"
   ```

<div align="center">
  <img src="https://github.com/Seikened/template_reflex_on_rialway/blob/main/doc/variables.png" alt="Configuración de variables en Railway" width="550" />
</div>

2. **Configurar el Dominio Público:**  
   Una vez creado el proyecto en Railway, ve a la sección "Public Networking". Copia el dominio que se te proporciona y reemplaza `public_domain` en tu configuración con ese valor (a menos que tengas un dominio personalizado).

<div align="center">
  <img src="https://github.com/Seikened/template_reflex_on_rialway/blob/main/doc/public_domain.png" alt="Configuración del dominio público en Railway" width="550" />
</div>

> **Consejo 💡:**  
> El primer dominio **example.up.rialway.app** lo brinda Railway, pero puedes configurar tu propio dominio, como **www.example.com**. Sea cual sea la opción, asegúrate de cambiarlo en el `rxconfig.py`.

---

## 5. Instalación 🔧

1. **Instalar Reflex:**  
   Asegúrate de instalar Reflex y cualquier otra librería necesaria:

   ```bash
   pip install reflex
   ```

2. **Actualizar Requerimientos:**  
   Verifica que tu archivo `requirements.txt` (o similar) incluya la última versión de Reflex y las dependencias de tu proyecto.

> **Nota 📝:**  
> **No modifiques** el `caddyfile` y `nixpackage.toml` si vienen con el template; están configurados para un despliegue sin complicaciones.

---

## 6. Despliegue en Railway 🚂

1. **Crear un Proyecto en Railway:**  
   - Inicia sesión en Railway y haz clic en **Create New Project**.
   - Selecciona **GitHub Repo** como método de despliegue.
   - Elige el repositorio y la rama correcta (la rama debe contener tu template actualizado).

2. **Commit y Push de Cambios:**  
   Una vez actualizada tu aplicación (nombre, estructura, dominio, etc.), realiza commit y push de tus cambios a GitHub. Railway redeplegará tu proyecto automáticamente.

3. **Verificar el Despliegue:**  
   - Revisa los logs en Railway para confirmar que tanto el backend como el frontend se están ejecutando correctamente.
   - Prueba tu aplicación mediante la URL pública proporcionada.

---

## 7. Resolución de Problemas y Contribuciones 🐞🤝

- **Resolución de Problemas:**  
  Si encuentras algún inconveniente:
  - Verifica que el despliegue local (`reflex run`) funcione sin errores.
  - Revisa que todas las variables de entorno y configuraciones estén correctamente establecidas.
  - Confirma que los nombres de las carpetas y archivos en el repositorio coinciden con la configuración.

- **Contribuciones:**  
  Si encuentras errores o mejoras:
  - Abre un issue o envía un pull request en el repositorio.
  - **Dale estrella al repositorio** si te resulta útil; es un recurso comunitario y tus aportes son bienvenidos.  
  **¡Si te sirvió, no olvides dejar una ⭐ al repo!**

---

## 8. Reflexiones Finales 💬

Este template está diseñado como un **punto de partida sencillo** para desplegar proyectos Reflex en Railway. Los pasos anteriores te guiarán desde la configuración local hasta un despliegue en vivo. Personalízalo según las necesidades de tu proyecto y comparte tus mejoras con la comunidad.
