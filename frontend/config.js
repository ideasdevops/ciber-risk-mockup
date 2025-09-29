// Configuración personalizable para la landing page del curso
const CONFIG = {
    // Información del curso
    curso: {
        titulo: "Curso de Ventas, Redes Sociales e Inteligencia Artificial",
        subtitulo: "Domina el e-commerce y el marketing digital en solo 4 horas",
        duracion: "4 horas",
        clases: "2 clases",
        precio: 199,
        moneda: "$",
        certificado: true
    },

    // Información de contacto
    contacto: {
        email: "info@marketingia.com",
        telefono: "+54 9 11 1234-5678",
        direccion: "Buenos Aires, Argentina",
        horario: "Lunes a Viernes, 9:00 - 18:00"
    },

    // Redes sociales
    redes: {
        facebook: "#",
        instagram: "#",
        linkedin: "#",
        twitter: "#",
        youtube: "#"
    },

    // Colores del tema
    colores: {
        primario: "#ff6b35",
        secundario: "#ff8c42",
        exito: "#10b981",
        error: "#ef4444",
        advertencia: "#f59e0b",
        info: "#3b82f6",
        fondo_oscuro: "#1a1a1a",
        fondo_claro: "#ffffff",
        texto_oscuro: "#1a1a1a",
        texto_claro: "#64748b"
    },

    // Configuración de animaciones
    animaciones: {
        duracion: 0.6,
        delay: 0.1,
        habilitadas: true
    },

    // Configuración del formulario
    formulario: {
        campos_requeridos: ['nombre', 'email', 'telefono', 'experiencia'],
        validacion_email: true,
        mensaje_exito: "¡Inscripción exitosa! Te contactaremos pronto.",
        mensaje_error: "Por favor completa todos los campos requeridos."
    },

    // Configuración de analytics
    analytics: {
        google_analytics_id: "", // Agregar tu ID de Google Analytics
        facebook_pixel_id: "", // Agregar tu ID de Facebook Pixel
        habilitado: false
    },

    // Configuración de notificaciones
    notificaciones: {
        duracion: 5000, // 5 segundos
        posicion: "top-right",
        sonido: false
    },

    // Configuración de scroll
    scroll: {
        suave: true,
        velocidad: 0.5,
        mostrar_progreso: true
    },

    // Configuración de carga
    carga: {
        mostrar_loader: true,
        duracion_minima: 1000 // 1 segundo
    },

    // Configuración de responsive
    responsive: {
        breakpoints: {
            mobile: 768,
            tablet: 1024,
            desktop: 1200
        }
    },

    // Configuración de SEO
    seo: {
        titulo: "Curso de Ventas, Redes Sociales e Inteligencia Artificial",
        descripcion: "Aprende e-commerce y marketing digital en 4 horas. Incluye Meta Ads, Google Analytics, redes sociales y más.",
        palabras_clave: "curso marketing digital, e-commerce, redes sociales, meta ads, google analytics",
        imagen_og: "https://ejemplo.com/imagen-og.jpg",
        url_canonica: "https://ejemplo.com"
    },

    // Configuración de contenido
    contenido: {
        mostrar_testimonios: true,
        mostrar_casos_exito: true,
        mostrar_herramientas: true,
        mostrar_beneficios: true,
        mostrar_precio: true
    },

    // Configuración de integración
    integracion: {
        webhook_formulario: "", // URL del webhook para procesar formularios
        api_key: "", // API key para servicios externos
        crm: {
            tipo: "none", // "none", "hubspot", "salesforce", "custom"
            configuracion: {}
        }
    },

    // Configuración de seguridad
    seguridad: {
        validacion_csrf: false,
        rate_limiting: false,
        captcha: false
    },

    // Configuración de desarrollo
    desarrollo: {
        modo_debug: false,
        mostrar_errores: true,
        log_consola: true
    }
};

// Función para obtener configuración
function getConfig(clave) {
    return clave ? CONFIG[clave] : CONFIG;
}

// Función para actualizar configuración
function updateConfig(clave, valor) {
    if (typeof clave === 'object') {
        Object.assign(CONFIG, clave);
    } else {
        CONFIG[clave] = valor;
    }
}

// Función para aplicar configuración al DOM
function aplicarConfiguracion() {
    // Aplicar colores
    if (CONFIG.colores) {
        const root = document.documentElement;
        root.style.setProperty('--color-primario', CONFIG.colores.primario);
        root.style.setProperty('--color-secundario', CONFIG.colores.secundario);
        root.style.setProperty('--color-exito', CONFIG.colores.exito);
        root.style.setProperty('--color-error', CONFIG.colores.error);
    }

    // Aplicar información del curso
    if (CONFIG.curso) {
        const titulo = document.querySelector('.hero h1');
        const subtitulo = document.querySelector('.hero-subtitle');
        const precio = document.querySelector('.amount');
        
        if (titulo && CONFIG.curso.titulo) titulo.textContent = CONFIG.curso.titulo;
        if (subtitulo && CONFIG.curso.subtitulo) subtitulo.textContent = CONFIG.curso.subtitulo;
        if (precio && CONFIG.curso.precio) precio.textContent = CONFIG.curso.precio;
    }

    // Aplicar información de contacto
    if (CONFIG.contacto) {
        const email = document.querySelector('.footer-section p:first-of-type');
        const telefono = document.querySelector('.footer-section p:nth-of-type(2)');
        
        if (email && CONFIG.contacto.email) {
            email.innerHTML = `<i class="fas fa-envelope"></i> ${CONFIG.contacto.email}`;
        }
        if (telefono && CONFIG.contacto.telefono) {
            telefono.innerHTML = `<i class="fas fa-phone"></i> ${CONFIG.contacto.telefono}`;
        }
    }

    // Aplicar configuración de scroll
    if (CONFIG.scroll && CONFIG.scroll.suave) {
        document.documentElement.style.scrollBehavior = 'smooth';
    }
}

// Función para validar configuración
function validarConfiguracion() {
    const errores = [];

    if (!CONFIG.curso.titulo) errores.push('Título del curso es requerido');
    if (!CONFIG.curso.precio || CONFIG.curso.precio <= 0) errores.push('Precio del curso debe ser mayor a 0');
    if (!CONFIG.contacto.email) errores.push('Email de contacto es requerido');

    if (errores.length > 0) {
        console.warn('Errores en la configuración:', errores);
        return false;
    }

    return true;
}

// Función para exportar configuración
function exportarConfiguracion() {
    return JSON.stringify(CONFIG, null, 2);
}

// Función para importar configuración
function importarConfiguracion(configJson) {
    try {
        const nuevaConfig = JSON.parse(configJson);
        Object.assign(CONFIG, nuevaConfig);
        aplicarConfiguracion();
        return true;
    } catch (error) {
        console.error('Error al importar configuración:', error);
        return false;
    }
}

// Aplicar configuración cuando se carga la página
document.addEventListener('DOMContentLoaded', function() {
    if (validarConfiguracion()) {
        aplicarConfiguracion();
    }
});

// Exportar para uso global
window.CONFIG = CONFIG;
window.getConfig = getConfig;
window.updateConfig = updateConfig;
window.aplicarConfiguracion = aplicarConfiguracion;
window.validarConfiguracion = validarConfiguracion;
window.exportarConfiguracion = exportarConfiguracion;
window.importarConfiguracion = importarConfiguracion;
