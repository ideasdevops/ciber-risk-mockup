#!/bin/bash

# ===============================================
# SCRIPT DE DEPLOY PARA TRAVEL-APP
# ===============================================
# Sistema de Deploy Automático - IdeasDevOps
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
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Verificar que estamos en el directorio correcto
if [ ! -f "Dockerfile.travel-app-fixed" ]; then
    print_error "No se encontró Dockerfile.travel-app-fixed. Ejecuta desde /home/administrator/deploy-system-for-easypanel"
    exit 1
fi

print_message "🚀 Iniciando deploy de TravelAPP..."

# 1. Copiar el Dockerfile corregido al proyecto
print_message "📋 Copiando Dockerfile corregido..."
cp Dockerfile.travel-app-fixed /home/administrator/travel-app/Dockerfile.easypanel-optimized
print_success "Dockerfile copiado correctamente"

# 2. Copiar el script de inicio
print_message "📋 Copiando script de inicio..."
cp start.sh /home/administrator/travel-app/start.sh
chmod +x /home/administrator/travel-app/start.sh
print_success "Script de inicio copiado correctamente"

# 3. Ir al directorio del proyecto
cd /home/administrator/travel-app

# 4. Hacer commit de los cambios
print_message "📝 Haciendo commit de los cambios..."
git add Dockerfile.easypanel-optimized start.sh
git commit -m "🔧 Fix Dependencies Installation in Dockerfile

✅ Problemas Solucionados:
- Actualizado pip antes de instalar dependencias
- Corregidas versiones de pydantic para compatibilidad
- Mejorada instalación de dependencias del sistema
- Variables de entorno configuradas correctamente

🔧 Cambios:
- pip3 upgrade antes de instalar dependencias
- pydantic>=2.7.0 para compatibilidad con pydantic-settings
- Dependencias del sistema optimizadas
- Script de inicio mejorado

El build ahora debería completarse exitosamente." || print_warning "No hay cambios para commitear"

# 5. Push al repositorio
print_message "📤 Haciendo push al repositorio..."
git push origin main
print_success "Push completado"

print_success "🎉 Deploy preparado exitosamente!"
print_message "📋 Próximos pasos:"
print_message "   1. Ve a EasyPanel y redepleya el proyecto"
print_message "   2. Las dependencias se instalarán correctamente"
print_message "   3. El backend debería funcionar sin errores"
print_message ""
print_message "🔑 Credenciales de acceso:"
print_message "   Email: admin@travelapp.com"
print_message "   Contraseña: admin123"
