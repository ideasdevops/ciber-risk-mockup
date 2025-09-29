#!/usr/bin/env python3
"""
Servidor HTTP simple para servir la landing page del curso de Marketing IA
Puerto: 8008
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Configuración del servidor
PORT = 8008
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Manejador personalizado para servir archivos estáticos"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Agregar headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Redirigir la raíz a index.html
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def start_server():
    """Inicia el servidor HTTP"""
    try:
        # Crear el servidor
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 60)
            print("🚀 SERVIDOR DE MARKETING IA INICIADO")
            print("=" * 60)
            print(f"📍 URL: http://{HOST}:{PORT}")
            print(f"📁 Directorio: {os.getcwd()}")
            print("=" * 60)
            print("📋 Archivos disponibles:")
            print("   • index.html - Página principal")
            print("   • ejemplos.html - Página de ejemplos")
            print("   • assets/ - Logo de IdeasDevOps")
            print("=" * 60)
            print("🛑 Para detener el servidor: Ctrl+C")
            print("=" * 60)
            
            # Abrir automáticamente en el navegador
            try:
                webbrowser.open(f'http://{HOST}:{PORT}')
                print("🌐 Abriendo en el navegador...")
            except Exception as e:
                print(f"⚠️  No se pudo abrir automáticamente: {e}")
                print(f"   Abre manualmente: http://{HOST}:{PORT}")
            
            print("\n✅ Servidor ejecutándose...")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor detenido por el usuario")
    except OSError as e:
        if e.errno == 98:  # Puerto ya en uso
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print("   Intenta con otro puerto o detén el proceso que lo usa")
        else:
            print(f"❌ Error al iniciar el servidor: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    # Verificar que estamos en el directorio correcto
    if not os.path.exists('index.html'):
        print("❌ Error: No se encontró index.html")
        print("   Asegúrate de ejecutar este script desde el directorio del proyecto")
        exit(1)
    
    start_server()
