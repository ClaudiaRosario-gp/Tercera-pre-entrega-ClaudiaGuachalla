Acceso a Admin:
Username: clau_ros_gp

Password: J8WZKUZG7UAkHz

Contenidos del Proyecto

Inicio: Página principal de la aplicación que ofrece enlaces a las distintas secciones del sitio.
Servicios: Sección donde se muestran los servicios disponibles y permite agregar nuevos servicios.
Clientes: Sección donde se muestran los clientes registrados y permite agregar nuevos clientes.
Consultas: Sección donde se muestran las consultas realizadas y permite agregar nuevas consultas.
Buscar: Permite buscar en la base de datos por servicio.

**Para ejecutar el Proyecto:**

Instalar Dependencias y activar el entorno virtual

Luego, instala las dependencias necesarias:
pip install -r requirements.txt

Aplica las migraciones para configurar la base de datos:
python manage.py migrate

Inicia el servidor de desarrollo de Django:
python manage.py runserver

Acceder a la Aplicación:

http://127.0.0.1:8000/inicio/
