#!/usr/bin/env python3
"""
Backend para Landing Page Marketing IA
Maneja el envío de correos electrónicos para inscripciones
"""

import os
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuración SMTP
SMTP_CONFIG = {
    'server': 'c1682311.ferozo.com',
    'port': 465,  # Puerto SMTP con SSL
    'username': 'marketing@ideasdevops.com',
    'password': 'Market1ng2k24@',
    'from_email': 'marketing@ideasdevops.com',
    'to_email': 'marketing@ideasdevops.com'
}

# Configuración del curso
COURSE_INFO = {
    'name': 'Curso de Ventas, Redes Sociales e Inteligencia Artificial',
    'price': '$69 USD',
    'duration': '8 horas total (4 clases de 2hs)',
    'sessions': '4 clases online en vivo',
    'frequency': '1 clase por semana',
    'format': 'Cupos reducidos para aprendizaje personalizado',
    'certificate': 'Certificado incluido'
}

def send_email(to_email, subject, html_content, text_content=None):
    """Envía un correo electrónico usando SMTP"""
    try:
        # Crear mensaje
        msg = MIMEMultipart('alternative')
        msg['From'] = SMTP_CONFIG['from_email']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Agregar contenido
        if text_content:
            part1 = MIMEText(text_content, 'plain', 'utf-8')
            msg.attach(part1)
        
        part2 = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(part2)
        
        # Crear conexión segura
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_CONFIG['server'], SMTP_CONFIG['port'], context=context) as server:
            server.login(SMTP_CONFIG['username'], SMTP_CONFIG['password'])
            server.send_message(msg)
        
        return True, "Correo enviado exitosamente"
    
    except Exception as e:
        return False, f"Error al enviar correo: {str(e)}"

def generate_admin_email_html(form_data):
    """Genera el HTML para el correo del administrador"""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nueva Inscripción - Marketing IA</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #4f46e5; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ background: #f9fafb; padding: 20px; border-radius: 0 0 8px 8px; }}
            .info-box {{ background: white; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #4f46e5; }}
            .label {{ font-weight: bold; color: #4f46e5; }}
            .value {{ margin-left: 10px; }}
            .course-info {{ background: #e0e7ff; padding: 15px; margin: 15px 0; border-radius: 5px; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎯 Nueva Inscripción al Curso</h1>
                <p>Marketing IA - IdeasDevOps</p>
            </div>
            
            <div class="content">
                <div class="course-info">
                    <h3>📚 Información del Curso</h3>
                    <p><strong>Nombre:</strong> {COURSE_INFO['name']}</p>
                    <p><strong>Precio:</strong> {COURSE_INFO['price']}</p>
                    <p><strong>Duración:</strong> {COURSE_INFO['duration']}</p>
                    <p><strong>Sesiones:</strong> {COURSE_INFO['sessions']}</p>
                    <p><strong>Frecuencia:</strong> {COURSE_INFO['frequency']}</p>
                    <p><strong>Formato:</strong> {COURSE_INFO['format']}</p>
                    <p><strong>Certificado:</strong> {COURSE_INFO['certificate']}</p>
                </div>
                
                <h3>👤 Datos del Estudiante</h3>
                
                <div class="info-box">
                    <span class="label">Nombre:</span>
                    <span class="value">{form_data.get('nombre', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Email:</span>
                    <span class="value">{form_data.get('email', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Teléfono:</span>
                    <span class="value">{form_data.get('telefono', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Nivel de experiencia:</span>
                    <span class="value">{form_data.get('experiencia', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Objetivos:</span>
                    <span class="value">{form_data.get('objetivos', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Fecha de inscripción:</span>
                    <span class="value">{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">IP del cliente:</span>
                    <span class="value">{request.remote_addr if request else 'N/A'}</span>
                </div>
            </div>
            
            <div class="footer">
                <p>Este correo fue generado automáticamente por el sistema de inscripciones de IdeasDevOps</p>
                <p>Marketing IA - Transformando negocios con estrategias digitales efectivas</p>
            </div>
        </div>
    </body>
    </html>
    """

def generate_student_email_html(form_data, payment_links=None):
    """Genera el HTML para el correo del estudiante"""
    payment_section = ""
    if payment_links:
        payment_section = f"""
        <div class="payment-section">
            <h3>💳 Opciones de Pago</h3>
            <p>Puedes realizar el pago de <strong>{COURSE_INFO['price']}</strong> usando cualquiera de estas opciones:</p>
            <div class="payment-buttons">
                {payment_links.get('stripe', '')}
                {payment_links.get('mercadopago', '')}
            </div>
        </div>
        """
    else:
        payment_section = """
        <div class="payment-section">
            <h3>💳 Información de Pago</h3>
            <p>El pago de <strong>$69 USD</strong> se procesará próximamente. Te enviaremos los enlaces de pago en breve.</p>
        </div>
        """
    
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>¡Bienvenido al Curso Marketing IA!</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #4f46e5; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ background: #f9fafb; padding: 20px; border-radius: 0 0 8px 8px; }}
            .welcome {{ text-align: center; margin: 20px 0; }}
            .course-details {{ background: white; padding: 20px; margin: 15px 0; border-radius: 5px; border: 1px solid #e5e7eb; }}
            .payment-section {{ background: #f0f9ff; padding: 20px; margin: 15px 0; border-radius: 5px; border: 1px solid #0ea5e9; }}
            .payment-buttons {{ text-align: center; margin: 15px 0; }}
            .payment-btn {{ display: inline-block; background: #10b981; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; margin: 5px; font-weight: bold; }}
            .payment-btn:hover {{ background: #059669; }}
            .next-steps {{ background: #fef3c7; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #f59e0b; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎉 ¡Bienvenido al Curso!</h1>
                <p>Marketing IA - IdeasDevOps</p>
            </div>
            
            <div class="content">
                <div class="welcome">
                    <h2>¡Hola {form_data.get('nombre', 'Estudiante')}!</h2>
                    <p>Gracias por inscribirte en nuestro curso. Estamos emocionados de tenerte con nosotros.</p>
                </div>
                
                <div class="course-details">
                    <h3>📚 Detalles de tu Curso</h3>
                    <p><strong>Curso:</strong> {COURSE_INFO['name']}</p>
                    <p><strong>Duración:</strong> {COURSE_INFO['duration']}</p>
                    <p><strong>Sesiones:</strong> {COURSE_INFO['sessions']}</p>
                    <p><strong>Frecuencia:</strong> {COURSE_INFO['frequency']}</p>
                    <p><strong>Formato:</strong> {COURSE_INFO['format']}</p>
                    <p><strong>Certificado:</strong> {COURSE_INFO['certificate']}</p>
                    <p><strong>Precio:</strong> {COURSE_INFO['price']}</p>
                </div>
                
                {payment_section}
                
                <div class="next-steps">
                    <h3>📋 Próximos Pasos</h3>
                    <ol>
                        <li>Completa el pago usando una de las opciones disponibles</li>
                        <li>Recibirás un correo de confirmación con los detalles de acceso</li>
                        <li>Te enviaremos el enlace de la clase 24 horas antes del inicio</li>
                        <li>¡Prepárate para transformar tu negocio!</li>
                    </ol>
                </div>
                
                <div class="course-details">
                    <h3>📞 Contacto</h3>
                    <p>Si tienes alguna pregunta, no dudes en contactarnos:</p>
                    <p>📧 Email: marketing@ideasdevops.com</p>
                    <p>🌐 Web: www.ideasdevops.com</p>
                </div>
            </div>
            
            <div class="footer">
                <p>Este correo fue enviado automáticamente por IdeasDevOps</p>
                <p>Marketing IA - Transformando negocios con estrategias digitales efectivas</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/')
def index():
    """Página principal - redirige al frontend"""
    return jsonify({
        'message': 'Backend de Marketing IA funcionando',
        'status': 'ok',
        'endpoints': {
            'health': '/health',
            'register': '/api/register'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'marketing-ia-backend'
    })

@app.route('/api/register', methods=['POST'])
def register():
    """Endpoint para procesar inscripciones"""
    try:
        # Obtener datos del formulario
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({
                'success': False,
                'message': 'No se recibieron datos del formulario'
            }), 400
        
        # Validar campos requeridos
        required_fields = ['nombre', 'email', 'telefono']
        missing_fields = [field for field in required_fields if not form_data.get(field)]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Faltan campos requeridos: {", ".join(missing_fields)}'
            }), 400
        
        # Generar contenido de correos
        admin_subject = f"🎯 Nueva Inscripción - {form_data.get('nombre', 'Estudiante')}"
        student_subject = "🎉 ¡Bienvenido al Curso Marketing IA!"
        
        admin_html = generate_admin_email_html(form_data)
        student_html = generate_student_email_html(form_data)
        
        # Enviar correo al administrador
        admin_success, admin_message = send_email(
            SMTP_CONFIG['to_email'],
            admin_subject,
            admin_html
        )
        
        # Enviar correo al estudiante
        student_success, student_message = send_email(
            form_data['email'],
            student_subject,
            student_html
        )
        
        # Respuesta
        if admin_success and student_success:
            return jsonify({
                'success': True,
                'message': 'Inscripción procesada exitosamente. Revisa tu correo electrónico.',
                'data': {
                    'nombre': form_data.get('nombre'),
                    'email': form_data.get('email'),
                    'timestamp': datetime.now().isoformat()
                }
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Error al enviar correos electrónicos',
                'details': {
                    'admin_email': admin_message,
                    'student_email': student_message
                }
            }), 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error interno del servidor: {str(e)}'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 Iniciando servidor Marketing IA Backend")
    print(f"📍 Puerto: {port}")
    print(f"🔧 Debug: {debug}")
    print(f"📧 SMTP: {SMTP_CONFIG['server']}:{SMTP_CONFIG['port']}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
