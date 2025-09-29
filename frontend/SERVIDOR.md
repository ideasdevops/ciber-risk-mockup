# 🚀 Servidor Local - Landing Page Marketing IA

## Inicio Rápido

### Opción 1: Script Automático (Recomendado)
```bash
./start-server.sh
```

### Opción 2: Python
```bash
python3 -m http.server 8008
# o
python -m http.server 8008
```

### Opción 3: Node.js
```bash
node start-server.js
```

### Opción 4: Python Personalizado
```bash
python3 server.py
```

## 🌐 Acceso al Sitio

Una vez iniciado el servidor, accede a:
- **URL Principal**: http://localhost:8008
- **Página de Ejemplos**: http://localhost:8008/ejemplos.html

## 📁 Estructura del Proyecto

```
clase_marketing_ia/
├── index.html              # Página principal
├── ejemplos.html           # Página de ejemplos
├── styles.css              # Estilos CSS
├── script.js               # JavaScript
├── config.js               # Configuración
├── assets/                 # Recursos
│   ├── IdeasDevops_largo_negro.png
│   └── ideas_devops_3.png
├── server.py               # Servidor Python personalizado
├── start-server.js         # Servidor Node.js
├── start-server.sh         # Script de inicio automático
└── SERVIDOR.md             # Este archivo
```

## 🛠️ Requisitos del Sistema

### Mínimos
- **Python 3.x** o **Node.js** (cualquiera de los dos)
- Navegador web moderno
- 50 MB de espacio libre

### Recomendados
- **Python 3.8+** o **Node.js 14+**
- Navegador con soporte para ES6+
- Conexión a internet (para fuentes y iconos)

## 🔧 Solución de Problemas

### Puerto 8008 en Uso
```bash
# Encontrar proceso que usa el puerto
lsof -i :8008
# o
netstat -tulpn | grep :8008

# Matar el proceso
kill -9 <PID>
```

### Error de Permisos
```bash
# Hacer ejecutable el script
chmod +x start-server.sh
```

### Python no Encontrado
```bash
# Instalar Python 3
sudo apt update
sudo apt install python3 python3-pip
```

### Node.js no Encontrado
```bash
# Instalar Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## 📱 Acceso desde Otros Dispositivos

Para acceder desde otros dispositivos en la misma red:

1. Encuentra tu IP local:
```bash
hostname -I
# o
ip addr show | grep inet
```

2. Accede desde otros dispositivos:
```
http://TU_IP_LOCAL:8008
```

## 🚀 Características del Servidor

- ✅ **CORS habilitado** para desarrollo
- ✅ **MIME types** correctos para todos los archivos
- ✅ **Redirección automática** de `/` a `/index.html`
- ✅ **Manejo de errores** 404 personalizado
- ✅ **Apertura automática** en el navegador
- ✅ **Logs informativos** del servidor

## 📊 Monitoreo

El servidor muestra:
- URL de acceso
- Directorio de trabajo
- Archivos disponibles
- Estado del servidor
- Errores (si los hay)

## 🛑 Detener el Servidor

Presiona `Ctrl+C` en la terminal donde está ejecutándose el servidor.

## 🔄 Reiniciar el Servidor

1. Detén el servidor (`Ctrl+C`)
2. Ejecuta nuevamente el comando de inicio

## 📝 Notas Adicionales

- El servidor es solo para desarrollo local
- No es seguro para uso en producción
- Los archivos se sirven directamente desde el sistema de archivos
- No hay procesamiento del lado del servidor

## 🆘 Soporte

Si tienes problemas:
1. Verifica que estés en el directorio correcto
2. Asegúrate de que el puerto 8008 esté libre
3. Revisa que tengas Python o Node.js instalado
4. Consulta los logs del servidor para errores específicos
