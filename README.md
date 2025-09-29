# Landing Page - Curso de Desarrollo No-Code con IA

## Descripción
Landing page moderna y responsive para promocionar un curso de 8 horas sobre desarrollo no-code, automatizaciones y deploy con IA. Diseñada con un enfoque minimalista y profesional.

## Características

### 🎨 Diseño
- **Minimalista y moderno**: Diseño limpio con gradientes y efectos visuales
- **Responsive**: Optimizado para dispositivos móviles, tablets y desktop
- **Animaciones suaves**: Efectos de scroll, hover y transiciones
- **Tipografía moderna**: Uso de la fuente Inter para mejor legibilidad

### 📱 Funcionalidades
- **Navegación suave**: Scroll automático entre secciones
- **Formulario de inscripción**: Con validación en tiempo real
- **Notificaciones**: Sistema de alertas para feedback del usuario
- **Efectos parallax**: Animaciones visuales en el hero
- **Contador animado**: Para estadísticas del curso
- **Efecto de escritura**: En el título principal
- **Descarga de recursos**: Sistema de lead capture para recursos descargables

### 🛠️ Tecnologías Utilizadas
- **HTML5**: Estructura semántica
- **CSS3**: Flexbox, Grid, animaciones y efectos visuales
- **JavaScript ES6+**: Interactividad y funcionalidades dinámicas
- **Font Awesome**: Iconografía
- **Google Fonts**: Tipografía Inter
- **Python Flask**: Backend para formularios y emails
- **Docker**: Containerización para deploy

## Estructura del Curso

### Clase 1: Fundamentos del Desarrollo No-Code (2 horas)
1. **Introducción al No-Code** (30 min)
   - Qué es el desarrollo no-code
   - Ventajas y casos de uso
   - Herramientas principales: Webflow, Bubble, Glide

2. **Plataformas No-Code Principales** (30 min)
   - Webflow para sitios web
   - Bubble para aplicaciones complejas
   - Glide para apps móviles

3. **Desarrollo con IA** (30 min)
   - Cursor como editor de código
   - GitHub Copilot para asistencia
   - ChatGPT y Claude para desarrollo

4. **Primer Proyecto** (30 min)
   - Crear una landing page simple
   - Configurar formularios
   - Deploy básico

### Clase 2: Automatizaciones y Bots (2 horas)
1. **Herramientas de Automatización** (30 min)
   - Zapier para conexiones simples
   - Make (Integromat) para flujos complejos
   - n8n para automatizaciones avanzadas

2. **Creación de Chatbots** (30 min)
   - Typebot para bots conversacionales
   - Diseño de flujos de conversación
   - Integración con APIs

3. **Automatizaciones de Negocio** (30 min)
   - Flujos de marketing
   - Procesos de ventas
   - Gestión de clientes

4. **Proyecto Práctico** (30 min)
   - Crear un bot de atención al cliente
   - Automatizar proceso de leads
   - Testing y optimización

### Clase 3: Deploy y VPS (2 horas)
1. **Configuración de VPS** (30 min)
   - Ubuntu Server
   - Configuración inicial
   - Seguridad básica

2. **Docker y Containerización** (30 min)
   - Conceptos de Docker
   - Dockerfile y Docker Compose
   - Mejores prácticas

3. **Deploy con EasyPanel** (30 min)
   - Configuración de EasyPanel
   - Deploy automático
   - SSL y dominios

4. **Proyecto Completo** (30 min)
   - Deploy de aplicación no-code
   - Configuración de dominio
   - Monitoreo y mantenimiento

### Clase 4: Proyectos Avanzados y Optimización (2 horas)
1. **Integración de IA Avanzada** (30 min)
   - APIs de OpenAI
   - Procesamiento de lenguaje natural
   - Generación de contenido automático

2. **Optimización y Performance** (30 min)
   - Métricas de rendimiento
   - Optimización de carga
   - Caché y CDN

3. **Escalabilidad** (30 min)
   - Preparación para crecimiento
   - Load balancing
   - Monitoreo avanzado

4. **Proyecto Final** (30 min)
   - Aplicación completa no-code
   - Deploy en producción
   - Presentación de proyectos

## Secciones de la Landing Page

### 🏠 Hero Section
- Título impactante con efecto de escritura
- Estadísticas del curso con animaciones
- Botones de acción (Inscribirse, Ver Temario)
- Tarjetas flotantes con iconos representativos

### 📚 Sección del Curso
- Grid de características principales
- Iconos y descripciones de cada módulo
- Efectos hover para mejor interactividad

### 📋 Temario Detallado
- Diseño de tarjetas para cada clase
- Cronograma detallado con tiempos
- Lista de temas con iconos
- Diseño visual atractivo

### 🛠️ Herramientas No-Code
- Grid de herramientas que se aprenderán
- Logos y descripciones de cada plataforma
- Efectos de hover y animaciones

### ✅ Beneficios
- Razones para elegir el curso
- Iconos representativos
- Diseño centrado en el usuario

### 📥 Recursos Descargables
- Sistema de lead capture
- Recursos exclusivos del curso
- Modal de descarga con validación

### 📝 Formulario de Inscripción
- Formulario completo con validación
- Información de precios
- Características del curso
- Notificaciones de éxito/error

## Instalación y Uso

1. **Clonar o descargar** los archivos del proyecto
2. **Configurar variables de entorno** en `config.env`
3. **Instalar dependencias** de Python: `pip install -r backend/requirements.txt`
4. **Ejecutar** el servidor: `python3 server.py`
5. **Abrir** `http://localhost:8008` en un navegador web

### Archivos del Proyecto
```
curso_desarrollo_nocode/
├── index.html              # Estructura principal
├── styles.css              # Estilos y diseño
├── script.js               # Funcionalidades JavaScript
├── config.js               # Configuración del sitio
├── ejemplos.html           # Página de ejemplos
├── backend/
│   ├── app.py              # Servidor Flask
│   └── requirements.txt    # Dependencias Python
├── assets/
│   ├── guia-desarrollo-nocode.md
│   ├── checklist-deploy.md
│   └── templates-automatizacion.md
├── Dockerfile.easypanel-optimized
└── README.md               # Documentación
```

## Personalización

### Colores
Los colores principales se pueden modificar en el archivo CSS:
- **Primario**: `#6366f1` (azul)
- **Secundario**: `#8b5cf6` (púrpura)
- **Éxito**: `#10b981` (verde)
- **Error**: `#ef4444` (rojo)
- **Naranja**: `#f97316` (para elementos de descarga)

### Contenido
- Modificar textos en `index.html`
- Actualizar precios y fechas
- Cambiar información de contacto
- Personalizar formulario de inscripción
- Configurar enlaces de pago de Stripe

### Funcionalidades
- Integrar con backend para formularios
- Agregar Google Analytics
- Implementar sistema de pagos
- Conectar con CRM
- Configurar SMTP para emails

## Características Técnicas

### Performance
- **Carga rápida**: Código optimizado y minificado
- **Lazy loading**: Imágenes y contenido se cargan según necesidad
- **Animaciones CSS**: Mejor rendimiento que JavaScript

### Accesibilidad
- **Navegación por teclado**: Soporte completo
- **Contraste**: Colores accesibles
- **Semántica HTML**: Estructura correcta
- **Alt text**: Para imágenes (cuando se agreguen)

### SEO
- **Meta tags**: Configuración básica
- **Estructura semántica**: HTML5 semántico
- **Títulos jerárquicos**: H1, H2, H3 correctamente utilizados

## Navegadores Soportados
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Responsive Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## Deploy con Docker

### Construcción de la imagen
```bash
docker build -f Dockerfile.easypanel-optimized -t nocode-ia-landing .
```

### Ejecución del contenedor
```bash
docker run -d -p 80:80 --name nocode-ia-landing nocode-ia-landing
```

### Deploy en EasyPanel
1. Conectar repositorio GitHub
2. Configurar variables de entorno
3. Deploy automático con Docker

## Próximas Mejoras
- [ ] Integración con más plataformas no-code
- [ ] Sistema de pagos avanzado
- [ ] Panel de administración
- [ ] Múltiples idiomas
- [ ] PWA (Progressive Web App)
- [ ] Chat en vivo
- [ ] Testimonios de estudiantes
- [ ] Certificados digitales

## Licencia
Este proyecto está bajo licencia MIT. Puedes usarlo libremente para proyectos personales y comerciales.

## Contacto
Para consultas o sugerencias sobre este proyecto:
- **Email**: marketing@ideasdevops.com
- **WhatsApp**: +54 9 261 315-1000
- **Horario**: Lunes a Viernes, 9:00 - 18:00