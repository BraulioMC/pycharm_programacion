# Ventana de Login

## Descripción

> Ventana de tamaño predifinido y estático que mostrá la posibilidad de registrarte y/o logearte

## Implementación
- Usará una base de datos en MariaDB para la gestión de usuarios.

- Las contraseñas se encriptarán con SHA256


## Distribución

> Se usarán los paquetes de Python para exportar un paquete instalable por `pip`

## Installation

`pip install PyLogin-0.1.tar.gz`

## Ejecución

`python pylogin.py`

## Consideraciones

- Se requiere un DB funcional

## Librerías

- `hashlib` - Encriptación de contraseñas
- `tkinter` - Lanzar las ventanas
- `pymysql` - Establece la conexión a la DB

### Capturas
![Login](/img/login.png?raw=true "Pantalla de Login")
![DB](/img/db.png?raw=true "Entrada en DB")