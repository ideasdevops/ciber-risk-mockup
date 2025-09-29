# 🚀 Deploy de Landing Page Marketing IA

## 📋 Información del Proyecto

- **Nombre:** marketing-ia-landing
- **Versión:** 1.0.0
- **Descripción:** Landing page para el curso de Ventas, Redes Sociales e Inteligencia Artificial
- **Tipo:** Sitio web estático
- **Servidor:** nginx (Alpine Linux)

## 🛠️ Archivos de Deploy

### Archivos Principales
- `Dockerfile.easypanel-optimized` - Dockerfile optimizado para EasyPanel
- `.dockerignore` - Archivos a ignorar en el build
- `validate-deploy.sh` - Script de validación pre-deploy
- `frontend/` - Directorio con todos los archivos de la landing page

### Estructura del Frontend
```
frontend/
├── index.html          # Página principal
├── ejemplos.html       # Página de ejemplos
├── styles.css          # Estilos CSS
├── script.js           # JavaScript
├── assets/             # Recursos estáticos
│   ├── IdeasDevops_largo_negro.png
│   └── ideas_devops_3.png
└── ... (otros archivos)
```

## 🚀 Configuración en EasyPanel

### 1. Crear Aplicación
- **Tipo:** SSH Git
- **Repositorio:** `git@github.com:tu-usuario/marketing-ia-landing.git`
- **Dockerfile:** `Dockerfile.easypanel-optimized`

### 2. Configurar Volúmenes
| Tipo | Nombre | Ruta de Montaje | Descripción |
|------|--------|-----------------|-------------|
| VOLUME | nginx-logs | /data/logs/nginx | Logs de nginx |
| VOLUME | nginx-cache | /var/cache/nginx | Caché de nginx |

### 3. Variables de Entorno
```bash
APP_NAME=marketing-ia-landing
APP_VERSION=1.0.0
APP_ENV=production
```

### 4. Configuración de Red
- **Puerto:** 80
- **Protocolo:** HTTP
- **Dominio:** Tu dominio personalizado

## 🔧 Comandos de Deploy

### Validación Pre-Deploy
```bash
./validate-deploy.sh
```

### Build Local (Opcional)
```bash
docker build -f Dockerfile.easypanel-optimized -t marketing-ia-landing .
docker run -p 8080:80 marketing-ia-landing
```

### Verificar Healthcheck
```bash
curl http://localhost:8080/health
```

## 📊 Monitoreo

### Endpoints Disponibles
- **`/`** - Landing page principal
- **`/ejemplos.html`** - Página de ejemplos
- **`/health`** - Health check
- **`/assets/`** - Recursos estáticos

### Logs
Los logs se almacenan en:
- **Nginx Access:** `/data/logs/nginx/access.log`
- **Nginx Error:** `/data/logs/nginx/error.log`

### Healthcheck
- **Endpoint:** `/health`
- **Intervalo:** 30 segundos
- **Timeout:** 10 segundos
- **Retries:** 3

## 🎯 Características de la Landing Page

### Contenido Principal
- ✅ Página de inicio con información del curso
- ✅ Página de ejemplos
- ✅ Diseño responsive
- ✅ Logo de IdeasDevOps
- ✅ Estilos CSS optimizados
- ✅ JavaScript funcional

### Optimizaciones
- ✅ Caché de assets (1 año)
- ✅ Compresión gzip
- ✅ Headers de seguridad
- ✅ Configuración nginx optimizada
- ✅ Healthcheck integrado

## 🔍 Troubleshooting

### Problemas Comunes

#### 1. Contenedor no inicia
```bash
# Verificar logs
docker logs <container_id>

# Verificar configuración nginx
docker exec <container_id> nginx -t
```

#### 2. Assets no cargan
- Verificar que los archivos estén en `frontend/assets/`
- Verificar permisos de archivos
- Verificar configuración de nginx

#### 3. Healthcheck falla
```bash
# Verificar endpoint
curl http://localhost/health

# Verificar logs de nginx
docker exec <container_id> cat /data/logs/nginx/error.log
```

### Comandos de Diagnóstico

```bash
# Verificar estructura de archivos
ls -la frontend/

# Verificar contenido del index.html
head -20 frontend/index.html

# Verificar configuración de nginx
docker exec <container_id> cat /etc/nginx/conf.d/default.conf
```

## 📈 Métricas de Rendimiento

### Tamaño de la Imagen
- **Base:** nginx:alpine (~23MB)
- **Total estimado:** ~25-30MB

### Tiempo de Carga
- **HTML:** < 100ms
- **CSS:** < 50ms
- **Assets:** < 200ms

### Recursos
- **CPU:** Mínimo
- **RAM:** ~10-20MB
- **Almacenamiento:** ~30MB

## 🔄 Actualizaciones

### Proceso de Actualización
1. Modificar archivos en `frontend/`
2. Ejecutar `./validate-deploy.sh`
3. Hacer commit y push
4. EasyPanel detectará cambios automáticamente
5. Rebuild y redeploy automático

### Versionado
- Usar tags de Git para versiones
- Actualizar `APP_VERSION` en el Dockerfile
- Documentar cambios en este archivo

## 📞 Soporte

Para problemas o dudas:
- Revisar logs del contenedor
- Ejecutar script de validación
- Verificar configuración en EasyPanel
- Consultar documentación de nginx

---

**Desarrollado con ❤️ por IdeasDevOps**

*Sistema de deploy optimizado para EasyPanel*
