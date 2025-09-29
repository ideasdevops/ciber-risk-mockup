#!/bin/bash

# ===============================================
# SCRIPT DE DEPLOY PARA EASYPANEL - LANDING PAGE MARKETING IA
# ===============================================
# Script final para desplegar la landing page en EasyPanel
# ===============================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_message() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}[HEADER]${NC} $1"
}

# Banner de inicio
echo "==============================================="
echo "🚀 DEPLOY LANDING PAGE MARKETING IA - EASYPANEL"
echo "==============================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "Dockerfile.easypanel-optimized" ]; then
    print_error "No se encontró Dockerfile.easypanel-optimized"
    print_error "Ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Paso 1: Validación
print_header "PASO 1: VALIDACIÓN PRE-DEPLOY"
echo "==============================================="

if [ -f "validate-deploy.sh" ]; then
    print_message "Ejecutando validación..."
    ./validate-deploy.sh
    if [ $? -eq 0 ]; then
        print_success "Validación exitosa"
    else
        print_error "Validación falló. Corrige los errores antes de continuar"
        exit 1
    fi
else
    print_warning "Script de validación no encontrado, continuando..."
fi

echo ""

# Paso 2: Verificar Git
print_header "PASO 2: CONFIGURACIÓN DE GIT"
echo "==============================================="

if [ -d ".git" ]; then
    print_success "Repositorio Git encontrado"
    
    # Verificar estado de Git
    if [ -n "$(git status --porcelain)" ]; then
        print_warning "Hay cambios sin commit:"
        git status --short
        
        echo ""
        read -p "¿Deseas hacer commit de los cambios? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_message "Haciendo commit de los cambios..."
            git add .
            git commit -m "Deploy: Landing page Marketing IA lista para EasyPanel

- Dockerfile optimizado para nginx
- Configuración de nginx con caché y seguridad
- Healthcheck integrado
- Scripts de validación
- Documentación de deploy completa

Archivos incluidos:
- frontend/ con todos los assets
- Dockerfile.easypanel-optimized
- .dockerignore
- validate-deploy.sh
- DEPLOY.md"
            print_success "Commit realizado"
        else
            print_warning "Continuando sin commit..."
        fi
    else
        print_success "No hay cambios pendientes"
    fi
    
    # Mostrar información del repositorio
    print_message "Información del repositorio:"
    echo "  - Rama actual: $(git branch --show-current)"
    echo "  - Último commit: $(git log -1 --oneline)"
    echo "  - Remoto: $(git remote get-url origin 2>/dev/null || echo 'No configurado')"
    
else
    print_warning "No se encontró repositorio Git"
    print_message "Para usar EasyPanel, necesitas un repositorio Git:"
    echo "  git init"
    echo "  git add ."
    echo "  git commit -m 'Initial commit'"
    echo "  git remote add origin <tu-repositorio>"
    echo "  git push -u origin main"
fi

echo ""

# Paso 3: Información de Deploy
print_header "PASO 3: INFORMACIÓN PARA EASYPANEL"
echo "==============================================="

print_message "Configuración requerida en EasyPanel:"
echo ""
echo "📋 CONFIGURACIÓN DE LA APLICACIÓN:"
echo "  • Tipo: SSH Git"
echo "  • Repositorio: $(git remote get-url origin 2>/dev/null || echo '<tu-repositorio-git>')"
echo "  • Dockerfile: Dockerfile.easypanel-optimized"
echo "  • Puerto: 80"
echo "  • Protocolo: HTTP"
echo ""

echo "📁 VOLÚMENES REQUERIDOS:"
echo "  • nginx-logs → /data/logs/nginx"
echo "  • nginx-cache → /var/cache/nginx"
echo ""

echo "🔧 VARIABLES DE ENTORNO:"
echo "  • APP_NAME=marketing-ia-landing"
echo "  • APP_VERSION=1.0.0"
echo "  • APP_ENV=production"
echo ""

echo "🌐 ENDPOINTS DISPONIBLES:"
echo "  • / → Landing page principal"
echo "  • /ejemplos.html → Página de ejemplos"
echo "  • /health → Health check"
echo "  • /assets/ → Recursos estáticos"
echo ""

# Paso 4: Test Local (Opcional)
print_header "PASO 4: TEST LOCAL (OPCIONAL)"
echo "==============================================="

read -p "¿Deseas hacer un test local del Docker? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_message "Construyendo imagen Docker..."
    docker build -f Dockerfile.easypanel-optimized -t marketing-ia-landing .
    
    if [ $? -eq 0 ]; then
        print_success "Imagen construida exitosamente"
        
        print_message "Iniciando contenedor en puerto 8080..."
        docker run -d --name marketing-ia-test -p 8080:80 marketing-ia-landing
        
        if [ $? -eq 0 ]; then
            print_success "Contenedor iniciado"
            print_message "Puedes probar la aplicación en: http://localhost:8080"
            print_message "Health check: http://localhost:8080/health"
            echo ""
            print_warning "Para detener el test: docker stop marketing-ia-test && docker rm marketing-ia-test"
        else
            print_error "Error al iniciar el contenedor"
        fi
    else
        print_error "Error al construir la imagen"
    fi
else
    print_message "Saltando test local..."
fi

echo ""

# Paso 5: Resumen Final
print_header "PASO 5: RESUMEN FINAL"
echo "==============================================="

print_success "✅ CONFIGURACIÓN COMPLETADA"
echo ""
print_message "Archivos creados:"
echo "  ✓ Dockerfile.easypanel-optimized"
echo "  ✓ .dockerignore"
echo "  ✓ validate-deploy.sh"
echo "  ✓ DEPLOY.md"
echo "  ✓ frontend/ (con todos los assets)"
echo ""

print_message "Próximos pasos:"
echo "1. 🔗 Configurar la aplicación en EasyPanel con la información mostrada arriba"
echo "2. 🚀 Hacer push del código al repositorio Git"
echo "3. 🌐 EasyPanel detectará los cambios y hará el deploy automáticamente"
echo "4. ✅ Verificar que la aplicación esté funcionando"
echo ""

print_message "Documentación completa disponible en: DEPLOY.md"
print_message "Para validar en cualquier momento: ./validate-deploy.sh"
echo ""

print_success "🎉 ¡La landing page está lista para deploy en EasyPanel!"
echo ""

# Mostrar información de contacto
echo "==============================================="
echo "📞 Soporte:"
echo "  • Revisar logs del contenedor en EasyPanel"
echo "  • Ejecutar ./validate-deploy.sh para diagnóstico"
echo "  • Consultar DEPLOY.md para troubleshooting"
echo "==============================================="
