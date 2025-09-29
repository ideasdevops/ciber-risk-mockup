#!/bin/bash

# ===============================================
# SCRIPT DE INICIO PARA TRAVEL-APP
# ===============================================
# Sistema de Deploy Automático - IdeasDevOps
# ===============================================

echo "🚀 Iniciando TravelAPP v1.0.0"
echo "========================================="
echo "Descripción: Plataforma integral para la gestión de viajes turísticos"
echo "Backend Python: FastAPI + uvicorn"
echo "Backend Node.js: Express + servicios"
echo "Frontend: HTML/CSS/JS + nginx"

# Verificar configuración de nginx
nginx -t
if [ $? -eq 0 ]; then
    echo "nginx: the configuration file /etc/nginx/nginx.conf syntax is ok"
    echo "nginx: configuration file /etc/nginx/nginx.conf test is successful"
else
    echo "❌ Error en configuración de nginx"
    exit 1
fi

echo "🌐 Iniciando servicios..."

# Iniciar supervisor
exec supervisord -c /etc/supervisor/conf.d/supervisord.conf
