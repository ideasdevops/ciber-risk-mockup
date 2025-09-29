#!/bin/bash

# Script para iniciar el servidor de la landing page de Marketing IA
# Puerto: 8008

echo "============================================================"
echo "🚀 INICIANDO SERVIDOR DE MARKETING IA"
echo "============================================================"

# Verificar que estamos en el directorio correcto
if [ ! -f "index.html" ]; then
    echo "❌ Error: No se encontró index.html"
    echo "   Asegúrate de ejecutar este script desde el directorio del proyecto"
    exit 1
fi

# Verificar si Python está disponible
if command -v python3 &> /dev/null; then
    echo "🐍 Usando Python 3..."
    python3 -m http.server 8008
elif command -v python &> /dev/null; then
    echo "🐍 Usando Python..."
    python -m http.server 8008
elif command -v node &> /dev/null; then
    echo "🟢 Usando Node.js..."
    node start-server.js
else
    echo "❌ Error: No se encontró Python ni Node.js"
    echo "   Instala Python 3 o Node.js para ejecutar el servidor"
    exit 1
fi
