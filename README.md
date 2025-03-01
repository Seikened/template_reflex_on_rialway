# Template for deploying a Reflex project in Rialway

## Advices 🚧

El proyecto descargalo y copiarlo, puedes clonarlo con el siguiente comando:

```bash
git clone 
```

# Create a Rialway project

Use Github repository to deploy it in Rialway

 Eelije la rama de despligue y comenzamos, antes que despliegues asgurate de crear una variable en rialway asi:

![[./doc/variables.png]]


```env
ENV="prod"
```

<div align="center">
<img src="https://github.com/Seikened/template_reflex_on_rialway/blob/main/doc/variables.png" alt="A frontend wrapper for DALL·E, shown in the process of generating an image." width="550" />
</div>

## Installation





```python
import reflex as rx
import os
"""
public_domain  use the public domain of Railway or your own domain but you must have a domain and configure it in Railway
"""

public_domain = "www.change-me.com"


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

```
<div align="center">
<img src="https://github.com/Seikened/template_reflex_on_rialway/blob/main/doc/public_domain.png" alt="A frontend wrapper for DALL·E, shown in the process of generating an image." width="550" />
</div>



```bash
pip install reflex
```




