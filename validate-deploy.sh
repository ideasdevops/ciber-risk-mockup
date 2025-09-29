#!/bin/bash

# ===============================================
# SCRIPT DE VALIDACIÓN PARA LANDING PAGE MARKETING IA
# ===============================================
# Valida que todos los archivos necesarios estén presentes
# ===============================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
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

# Contador de errores
ERRORS=0

echo "==============================================="
echo "VALIDACIÓN DE DEPLOY - LANDING PAGE MARKETING IA"
echo "==============================================="
echo ""

# Verificar archivos principales
print_message "Verificando archivos principales..."

REQUIRED_FILES=(
    "frontend/index.html"
    "frontend/styles.css"
    "frontend/script.js"
    "frontend/assets/IdeasDevops_largo_negro.png"
    "Dockerfile.easypanel-optimized"
    ".dockerignore"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        print_success "✓ $file"
    else
        print_error "✗ $file - FALTANTE"
        ((ERRORS++))
    fi
done

# Verificar estructura de directorios
print_message "Verificando estructura de directorios..."

REQUIRED_DIRS=(
    "frontend"
    "frontend/assets"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        print_success "✓ $dir/"
    else
        print_error "✗ $dir/ - FALTANTE"
        ((ERRORS++))
    fi
done

# Verificar contenido del index.html
print_message "Verificando contenido del index.html..."

if [ -f "frontend/index.html" ]; then
    if grep -q "Curso de Ventas, Redes Sociales e Inteligencia Artificial" "frontend/index.html"; then
        print_success "✓ Título del curso encontrado"
    else
        print_warning "⚠ Título del curso no encontrado en index.html"
    fi
    
    if grep -q "IdeasDevops_largo_negro.png" "frontend/index.html"; then
        print_success "✓ Logo de IdeasDevOps encontrado"
    else
        print_warning "⚠ Logo de IdeasDevOps no encontrado en index.html"
    fi
else
    print_error "✗ frontend/index.html no encontrado"
    ((ERRORS++))
fi

# Verificar Dockerfile
print_message "Verificando Dockerfile..."

if [ -f "Dockerfile.easypanel-optimized" ]; then
    if grep -q "FROM nginx:alpine" "Dockerfile.easypanel-optimized"; then
        print_success "✓ Base image nginx:alpine"
    else
        print_error "✗ Base image incorrecta"
        ((ERRORS++))
    fi
    
    if grep -q "COPY frontend/" "Dockerfile.easypanel-optimized"; then
        print_success "✓ Copia de frontend configurada"
    else
        print_error "✗ Copia de frontend no configurada"
        ((ERRORS++))
    fi
    
    if grep -q "HEALTHCHECK" "Dockerfile.easypanel-optimized"; then
        print_success "✓ Healthcheck configurado"
    else
        print_error "✗ Healthcheck no configurado"
        ((ERRORS++))
    fi
else
    print_error "✗ Dockerfile.easypanel-optimized no encontrado"
    ((ERRORS++))
fi

# Verificar .dockerignore
print_message "Verificando .dockerignore..."

if [ -f ".dockerignore" ]; then
    print_success "✓ .dockerignore presente"
else
    print_warning "⚠ .dockerignore no encontrado (opcional)"
fi

# Verificar tamaño de la imagen
print_message "Verificando tamaño de archivos..."

TOTAL_SIZE=$(du -sh frontend/ 2>/dev/null | cut -f1)
print_message "Tamaño del frontend: $TOTAL_SIZE"

if [ -d "frontend/assets" ]; then
    ASSETS_SIZE=$(du -sh frontend/assets/ 2>/dev/null | cut -f1)
    print_message "Tamaño de assets: $ASSETS_SIZE"
fi

# Resumen final
echo ""
echo "==============================================="
if [ $ERRORS -eq 0 ]; then
    print_success "✅ VALIDACIÓN EXITOSA"
    print_success "La landing page está lista para deploy en EasyPanel"
    echo ""
    print_message "Próximos pasos:"
    echo "1. Hacer commit y push del código"
    echo "2. Configurar la aplicación en EasyPanel"
    echo "3. Usar Dockerfile: Dockerfile.easypanel-optimized"
    echo "4. Configurar puerto: 80"
    echo "5. Configurar volúmenes: /data/logs/nginx"
    echo ""
    exit 0
else
    print_error "❌ VALIDACIÓN FALLIDA"
    print_error "Se encontraron $ERRORS errores"
    echo ""
    print_message "Corrige los errores antes de continuar"
    echo ""
    exit 1
fi
