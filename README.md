# Trabajo Parcial - Hacking Ético

## Descripción
Repositorio correspondiente al Trabajo Parcial de la asignatura. Contiene el 
desarrollo de un prototipo de keylogger implementado con fines exclusivamente 
académicos, dentro de un entorno controlado de laboratorio, con el objetivo de 
estudiar su funcionamiento y los mecanismos de detección asociados.

## Componentes
- `Keylogger_Parcial.py`: código fuente del cliente (captura de teclado, 
  identificación de la ventana activa, marcas de tiempo, registro local y envío 
  de datos al receptor).
- `SystemUpdate.py`: componente asociado al mecanismo de persistencia.

## Requisitos
- Python 3.x
- Librerías: `pynput`, `flask`, `urllib`, `winreg` (Windows)

## Advertencia de uso
Este proyecto se realizó **únicamente con fines educativos y de investigación 
en seguridad**, sobre máquinas propias o expresamente autorizadas y aisladas 
del entorno de producción. **No debe utilizarse sobre sistemas de terceros sin 
consentimiento explícito.** El uso indebido de este código puede constituir un 
delito según la legislación vigente.
