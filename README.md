# Django Portfolio

## Desarrollo local

En una terminal Git Bash de Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Sin variables de producción, el proyecto usa `DEBUG=True`, SQLite y guarda las
imágenes en `media/`. No hace falta configurar una clave secreta ni Cloudinary
para iniciar el sitio localmente.

Para usar en local las mismas imágenes de Cloudinary que en producción, define
`CLOUDINARY_URL` antes de iniciar el servidor, usando las credenciales de la
misma cuenta:

```bash
export CLOUDINARY_URL='cloudinary://API_KEY:API_SECRET@CLOUD_NAME'
```

Sin Cloudinary, los archivos de `media/` son locales y no se sincronizan con
producción.

## Producción

Configura estas variables en el servicio de despliegue; no las guardes en el
código ni en Git:

- `DEBUG=False`
- `DJANGO_SECRET_KEY`: una clave secreta única para producción.
- `DATABASE_URL`: URL de conexión a PostgreSQL.
- `ALLOWED_HOSTS`: dominios separados por comas, sin `https://`. En Render se
  admite automáticamente el valor de `RENDER_EXTERNAL_HOSTNAME`.
- `CLOUDINARY_URL`: credenciales de Cloudinary para almacenamiento persistente
  de imágenes.
- `CSRF_TRUSTED_ORIGINS`: orígenes HTTPS separados por comas, por ejemplo
  `https://example.com`.

El despliegue debe ejecutar:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

Comando de inicio para Gunicorn:

```bash
gunicorn django_portfolio.wsgi:application
```

Si se configura `DATABASE_URL` o `RENDER_EXTERNAL_HOSTNAME` y no se define
`DEBUG`, Django selecciona el modo de producción de forma segura. Para usar una
base de datos remota desde desarrollo local, establece explícitamente
`DEBUG=True`.
