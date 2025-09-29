# 🚀 INICIO RÁPIDO - Marketing IA Landing Page

## ✅ SERVIDOR YA INICIADO

El servidor está ejecutándose en el puerto 8008. Puedes acceder al sitio en:

**🌐 URL Principal:** http://localhost:8008

## 📋 Archivos del Proyecto

```
clase_marketing_ia/
├── 📄 index.html              # Página principal
├── 📄 ejemplos.html           # Página de ejemplos y herramientas
├── 🎨 styles.css              # Estilos CSS
├── ⚡ script.js               # JavaScript interactivo
├── ⚙️  config.js               # Configuración personalizable
├── 📁 assets/                 # Recursos (logo IdeasDevOps)
│   ├── IdeasDevops_largo_negro.png
│   └── ideas_devops_3.png
├── 🐍 server.py               # Servidor Python personalizado
├── 🟢 start-server.js         # Servidor Node.js
├── 🚀 start-server.sh         # Script de inicio automático
├── 📦 package.json            # Configuración Node.js
├── ⚙️  config.env.example      # Variables de entorno
├── 📖 README.md               # Documentación completa
├── 📖 SERVIDOR.md             # Guía del servidor
└── 📖 INICIO_RAPIDO.md        # Este archivo
```

## 🎯 Características Principales

### ✨ **Landing Page Completa**
- Logo de IdeasDevOps integrado
- Diseño moderno y responsive
- Animaciones suaves y efectos visuales
- Formulario de inscripción funcional

### 🛠️ **Herramientas GRATUITAS Detalladas**
- **E-commerce:** WooCommerce, PrestaShop, OpenCart
- **Diseño:** Canva, GIMP, Inkscape, DaVinci Resolve
- **Marketing:** Google Analytics, Meta Business Suite, Mailchimp
- **Búsqueda de Clientes:** Google My Business, LinkedIn, Google Trends

### 📚 **Curso de 4 Horas**
- **Clase 1:** Fundamentos de E-commerce y Marketing Digital (2h)
- **Clase 2:** Publicidad Digital, Analítica y Open Source (2h)
- Temario detallado con herramientas específicas
- Ejemplos prácticos y casos de uso

## 🚀 Comandos de Inicio

### Opción 1: Script Automático
```bash
./start-server.sh
```

### Opción 2: Python
```bash
python3 -m http.server 8008
```

### Opción 3: Node.js
```bash
node start-server.js
```

### Opción 4: Python Personalizado
```bash
python3 server.py
```

## 🌐 URLs Disponibles

- **Página Principal:** http://localhost:8008
- **Ejemplos y Herramientas:** http://localhost:8008/ejemplos.html
- **Logo IdeasDevOps:** http://localhost:8008/assets/IdeasDevops_largo_negro.png

## 🛑 Detener el Servidor

Presiona `Ctrl+C` en la terminal donde está ejecutándose.

## 🔄 Reiniciar el Servidor

1. Detén el servidor (`Ctrl+C`)
2. Ejecuta uno de los comandos de inicio

## 📱 Acceso desde Otros Dispositivos

Para acceder desde otros dispositivos en la misma red:

1. Encuentra tu IP local:
```bash
hostname -I
```

2. Accede desde otros dispositivos:
```
http://TU_IP_LOCAL:8008
```

## ⚙️ Personalización

### Cambiar Configuración
Edita el archivo `config.js` para personalizar:
- Colores del sitio
- Información de contacto
- Precio del curso
- Redes sociales

### Cambiar Puerto
Si el puerto 8008 está ocupado, puedes usar otro:
```bash
python3 -m http.server 8080
```

## 🆘 Solución de Problemas

### Puerto Ocupado
```bash
# Encontrar proceso
lsof -i :8008
# Matar proceso
kill -9 <PID>
```

### Error de Permisos
```bash
chmod +x start-server.sh
```

### Python no Encontrado
```bash
sudo apt update
sudo apt install python3
```

## 📊 Estado Actual

✅ **Servidor:** Ejecutándose en puerto 8008  
✅ **Sitio:** Accesible en http://localhost:8008  
✅ **Logo IdeasDevOps:** Integrado  
✅ **Herramientas Gratuitas:** Detalladas  
✅ **Responsive:** Optimizado para móviles  
✅ **Formulario:** Funcional con validación  

## 🎉 ¡Listo para Usar!

El sitio está completamente funcional y listo para presentar el curso de Marketing IA. Todas las herramientas mostradas son 100% gratuitas o tienen planes gratuitos robustos.
