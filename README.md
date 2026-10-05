# Infraestructura de Monitoreo Distribuido Local (C2 Framework)

Este repositorio contiene el desarrollo práctico de un laboratorio de seguridad informática enfocado en la auditoría de sistemas, la evaluación de vectores de persistencia y el análisis de técnicas de ingeniería social mediante instaladores troyanizados. 

La suite se compone de dos módulos independientes que interactúan de forma asíncrona dentro de un entorno de red de área local (LAN) controlado.

## Requisitos del Entorno de Pruebas

Para realizar la demostración de forma exitosa, se requiere la siguiente infraestructura:
1. **Máquina Atacante (Host Real):** Sistema operativo Windows con Python 3.10+ instalado.
2. **Máquina Víctima (Entorno Virtual):** Máquina virtual en VMware con Windows 10/11.
3. **Configuración de Red (Crítico):** La tarjeta de red de la máquina virtual en VMware debe estar configurada obligatoriamente en modo **Bridged (Adaptador puente)** para permitir la visibilidad de sockets en la LAN.

---

## Guía de Despliegue y Ejecución

### Paso 1: Preparación en la Máquina Atacante

1. Clone este repositorio o descargue los archivos fuentes en su máquina física.
2. Abra una terminal de comandos (CMD) en la carpeta del proyecto e instale las dependencias requeridas:
   ```cmd
   pip install flask pynput pyinstaller
   ```
3. Ejecute el servidor de control centralizado (C2) utilizando el intérprete de Python:
   ```cmd
   python Keylogger_Parcial.py
   ```
   *Nota: El script abrirá de forma automática el navegador web predeterminado en la interfaz gráfica del panel local (`http://localhost:8080`) e iniciará la escucha de sockets en el puerto `60000`.*

### Paso 2: Compilación del Artefacto (Opcional / Desarrollo)

Si desea generar el ejecutable independiente para la máquina de pruebas desde el código fuente `SystemUpdate.py`, ejecute el siguiente comando de PyInstaller en su máquina real:
```cmd
pyinstaller --onefile --noconsole --clean --hidden-import="pynput.keyboard._win32" --name="SystemUpdate" SystemUpdate.py
```
El archivo binario final compilado se depositará de forma automática dentro de la subcarpeta `dist/SystemUpdate.exe`.

*Nota: El argumento `--hidden-import="pynput.keyboard._win32"` es necesario porque PyInstaller no detecta automáticamente ese módulo interno de pynput; sin él, el ejecutable falla al iniciar en segundo plano.*

### Paso 3: Ejecución en la Máquina Víctima (Simulación)

1. Traslade el archivo empaquetado unificado (generado previamente mediante el ejecutable autoextraíble SFX de WinRAR) al Escritorio de la máquina virtual. El SFX se construye empaquetando el ejecutable `SystemUpdate.exe` junto con un instalador legítimo de Microsoft Office, de forma que al ejecutarse se muestre el instalador como distracción mientras el proceso real se lanza en segundo plano.(Este archivo esta incluido en el repositorio, se llama Instalador_Office_2024.exe).
2. Ejecute el instalador con privilegios de administrador.
3. **Comportamiento esperado:**
   * En primer plano, se desplegará de forma legítima el asistente de instalación de software como elemento de distracción para el usuario.
   * En segundo plano, de manera invisible, el proceso `SystemUpdate.exe` se inicializará en memoria, configurará su persistencia autónoma en la colmena `Run` del Registro de Windows y lanzará el escáner dinámico multihilo en la LAN.
4. Interactúe con el teclado o realice pruebas de inicio de sesión dentro de la máquina virtual. Los caracteres y bloques filtrados se renderizarán en tiempo real dentro del Dashboard de la Máquina Atacante (`http://localhost:8080`).

---

## Flujo de la Información

El cliente realiza tres acciones simultáneas cada vez que se produce actividad:
* **Guardado local:** Escribe los eventos en `%LOCALAPPDATA%\SystemUpdate\SystemUpdate.txt`.
* **Vía TCP:** Envía los registros al receptor por el puerto `60000` si está disponible en la LAN.
* **Vía HTTPS:** Envía reportes consolidados a un webhook externo cuando se cierra un bloque de texto.

El receptor, al aceptar cada conexión, genera un archivo por sesión con un nombre basado en la IP y el puerto de origen, por ejemplo:
```text
Keylogger_('192.168.234.133', 64068).txt
```

---

## Guía de Desinstalación Limpia (Post-Evaluación)

Una vez finalizado el laboratorio, ejecute los siguientes comandos en un CMD como Administrador dentro de la máquina virtual para remover por completo los componentes de persistencia del sistema:

```cmd
taskkill /F /IM SystemUpdate.exe
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v "WindowsSystemUpdateAutomation" /f
rmdir /s /q "%localappdata%\SystemUpdate"
```

---

## Declaración de Uso Académico
Este proyecto ha sido desarrollado exclusivamente con fines educativos, de investigación y auditoría de seguridad bajo un entorno controlado. El autor no se hace responsable del uso indebido o fuera del marco ético y legal de los componentes aquí descritos.
