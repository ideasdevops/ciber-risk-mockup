#!/usr/bin/env python3
"""
Backend para Landing Page de Seguros de Riesgos Cibernéticos - Del Campo Seguros
Maneja el envío de correos electrónicos para cotizaciones
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

# Configuración SMTP con las credenciales proporcionadas
SMTP_CONFIG = {
    'server': 'c1682311.ferozo.com',
    'port': 465,  # Puerto SMTP con SSL
    'username': 'cyber-risk@ideasdevops.com',
    'password': 'Cyberisk2k25@@',
    'from_email': 'cyber-risk@ideasdevops.com',
    'to_email': 'cyber-risk@ideasdevops.com'
}

# Configuración del seguro
INSURANCE_INFO = {
    'name': 'Seguro de Riesgos Cibernéticos - Del Campo Seguros',
    'company': 'Del Campo Seguros',
    'broker': 'Manuel del Campo',
    'email': 'manuelj@delcampobroker.com',
    'phone': '+54 9 2616 97-9044',
    'address': 'Piedras 267 - Chacras de Coria - Mendoza, Argentina',
    'hours': 'Lunes a Viernes de 9 a 17 hs'
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

def generate_client_email_html(form_data):
    """Genera el HTML para el correo del cliente"""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cotización de Seguro de Riesgos Cibernéticos</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #003366; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ background: #f9fafb; padding: 20px; border-radius: 0 0 8px 8px; }}
            .welcome {{ text-align: center; margin: 20px 0; }}
            .quote-info {{ background: white; padding: 20px; margin: 15px 0; border-radius: 5px; border: 1px solid #e5e7eb; }}
            .contact-info {{ background: #f0f9ff; padding: 20px; margin: 15px 0; border-radius: 5px; border: 1px solid #00BFFF; }}
            .next-steps {{ background: #fef3c7; padding: 15px; margin: 15px 0; border-radius: 5px; border-left: 4px solid #f59e0b; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
            .highlight {{ color: #003366; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🛡️ Cotización de Seguro de Riesgos Cibernéticos</h1>
                <p>Del Campo Seguros - Broker Especializado</p>
            </div>
            
            <div class="content">
                <div class="welcome">
                    <h2>¡Hola {form_data.get('nombre', 'Cliente')}!</h2>
                    <p>Gracias por tu interés en proteger tu empresa con nuestro <span class="highlight">Seguro de Riesgos Cibernéticos</span>.</p>
                </div>
                
                <div class="quote-info">
                    <h3>📋 Información de tu Cotización</h3>
                    <p><strong>Empresa:</strong> {form_data.get('empresa', 'No especificada')}</p>
                    <p><strong>Sector:</strong> {form_data.get('sector', 'No especificado')}</p>
                    <p><strong>Número de empleados:</strong> {form_data.get('empleados', 'No especificado')}</p>
                    <p><strong>Necesidades:</strong> {form_data.get('necesidades', 'No especificadas')}</p>
                    <p><strong>Fecha de solicitud:</strong> {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                </div>
                
                <div class="contact-info">
                    <h3>📞 Próximos Pasos</h3>
                    <p>Nuestro equipo de especialistas analizará tu solicitud y te contactará en las próximas <strong>24 horas</strong> con:</p>
                    <ul>
                        <li>✅ Análisis de riesgo personalizado</li>
                        <li>✅ Comparación entre múltiples aseguradoras</li>
                        <li>✅ Propuesta de cobertura adaptada a tu empresa</li>
                        <li>✅ Cotización detallada sin compromiso</li>
                    </ul>
                </div>
                
                <div class="next-steps">
                    <h3>🛡️ Coberturas Incluidas</h3>
                    <ul>
                        <li><strong>Violación de Datos Personales:</strong> Acceso no autorizado, notificaciones, monitoreo de crédito</li>
                        <li><strong>Ataques de Malware y Ransomware:</strong> Pérdidas por ransomware, recuperación de sistemas</li>
                        <li><strong>Interrupción de Negocio:</strong> Pérdida de ingresos, costos adicionales</li>
                        <li><strong>Responsabilidad Civil:</strong> Defensa legal, multas regulatorias</li>
                        <li><strong>Soporte 24/7:</strong> Centro de respuesta a incidentes</li>
                    </ul>
                </div>
                
                <div class="contact-info">
                    <h3>📧 Contacto Directo</h3>
                    <p>Si tienes alguna pregunta urgente, puedes contactarnos directamente:</p>
                    <p><strong>Manuel del Campo</strong> - Broker Especializado</p>
                    <p>📧 Email: {INSURANCE_INFO['email']}</p>
                    <p>📱 Teléfono: {INSURANCE_INFO['phone']}</p>
                    <p>📍 Dirección: {INSURANCE_INFO['address']}</p>
                    <p>🕒 Horarios: {INSURANCE_INFO['hours']}</p>
                </div>
            </div>
            
            <div class="footer">
                <p>Este correo fue enviado automáticamente por Del Campo Seguros</p>
                <p>Broker especializado en seguros de riesgos cibernéticos</p>
            </div>
        </div>
    </body>
    </html>
    """

def generate_admin_email_html(form_data):
    """Genera el HTML para el correo del administrador"""
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Nueva Solicitud de Cotización - Del Campo Seguros</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: #003366; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
            .content {{ background: #f9fafb; padding: 20px; border-radius: 0 0 8px 8px; }}
            .info-box {{ background: white; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #003366; }}
            .label {{ font-weight: bold; color: #003366; }}
            .value {{ margin-left: 10px; }}
            .urgent {{ background: #fef2f2; border-left: 4px solid #dc2626; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🛡️ Nueva Solicitud de Cotización</h1>
                <p>Seguro de Riesgos Cibernéticos - Del Campo Seguros</p>
            </div>
            
            <div class="content">
                <div class="urgent">
                    <h3>⚠️ ACCIÓN REQUERIDA</h3>
                    <p>Un cliente potencial ha solicitado una cotización de seguro de riesgos cibernéticos. Contactar en las próximas 24 horas.</p>
                </div>
                
                <h3>👤 Datos del Cliente</h3>
                
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
                    <span class="label">Empresa:</span>
                    <span class="value">{form_data.get('empresa', 'No especificada')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Sector:</span>
                    <span class="value">{form_data.get('sector', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Número de empleados:</span>
                    <span class="value">{form_data.get('empleados', 'No especificado')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Necesidades de ciberseguridad:</span>
                    <span class="value">{form_data.get('necesidades', 'No especificadas')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">Fecha de solicitud:</span>
                    <span class="value">{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</span>
                </div>
                
                <div class="info-box">
                    <span class="label">IP del cliente:</span>
                    <span class="value">{request.remote_addr if request else 'N/A'}</span>
                </div>
                
                <div class="urgent">
                    <h3>📋 Próximos Pasos</h3>
                    <ol>
                        <li>Contactar al cliente en las próximas 24 horas</li>
                        <li>Realizar análisis de riesgo personalizado</li>
                        <li>Comparar opciones entre aseguradoras</li>
                        <li>Enviar propuesta de cobertura detallada</li>
                        <li>Seguimiento para cerrar la venta</li>
                    </ol>
                </div>
            </div>
            
            <div class="footer">
                <p>Este correo fue generado automáticamente por el sistema de cotizaciones</p>
                <p>Del Campo Seguros - Broker especializado en seguros de riesgos cibernéticos</p>
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
            <p>Puedes realizar el pago de <strong>$69 USD</strong> usando el siguiente enlace seguro:</p>
            <div class="payment-buttons">
                <a href="https://buy.stripe.com/dRm4gA8Vm3RA5w39Ml1ZS06" class="payment-btn" target="_blank">
                    💳 Pagar con Stripe - $69 USD
                </a>
            </div>
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
        'message': 'Backend de Seguros de Riesgos Cibernéticos funcionando',
        'status': 'ok',
        'service': 'Del Campo Seguros - Cyber Risk Backend',
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
        'service': 'cyber-risk-insurance-backend',
        'company': 'Del Campo Seguros'
    })

@app.route('/api/register', methods=['POST'])
def register():
    """Endpoint para procesar solicitudes de cotización de seguros"""
    try:
        # Obtener datos del formulario
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({
                'success': False,
                'message': 'No se recibieron datos del formulario'
            }), 400
        
        # Validar campos requeridos
        required_fields = ['nombre', 'email', 'telefono', 'empresa', 'sector', 'empleados']
        missing_fields = [field for field in required_fields if not form_data.get(field)]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Faltan campos requeridos: {", ".join(missing_fields)}'
            }), 400
        
        # Generar contenido de correos
        client_subject = f"🛡️ Cotización de Seguro de Riesgos Cibernéticos - {form_data.get('empresa', 'Tu Empresa')}"
        admin_subject = f"🛡️ Nueva Solicitud de Cotización - {form_data.get('nombre', 'Cliente')} ({form_data.get('empresa', 'Empresa')})"
        
        client_html = generate_client_email_html(form_data)
        admin_html = generate_admin_email_html(form_data)
        
        # Lista de destinatarios para notificaciones
        recipients = [
            {'email': form_data['email'], 'subject': client_subject, 'html': client_html, 'type': 'cliente'},
            {'email': 'devops@ideasdevops.com', 'subject': admin_subject, 'html': admin_html, 'type': 'devops'},
            {'email': 'manuelj@delcampobroker.com', 'subject': admin_subject, 'html': admin_html, 'type': 'manuel'}
        ]
        
        # Enviar correos
        email_results = []
        for recipient in recipients:
            success, message = send_email(
                recipient['email'],
                recipient['subject'],
                recipient['html']
            )
            email_results.append({
                'email': recipient['email'],
                'type': recipient['type'],
                'success': success,
                'message': message
            })
        
        # Verificar si todos los correos se enviaron exitosamente
        all_success = all(result['success'] for result in email_results)
        
        if all_success:
            return jsonify({
                'success': True,
                'message': 'Solicitud de cotización procesada exitosamente. Revisa tu correo electrónico.',
                'data': {
                    'nombre': form_data.get('nombre'),
                    'email': form_data.get('email'),
                    'empresa': form_data.get('empresa'),
                    'timestamp': datetime.now().isoformat()
                },
                'notifications_sent': len(email_results)
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Error al enviar algunas notificaciones por correo electrónico',
                'details': email_results
            }), 500
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error interno del servidor: {str(e)}'
        }), 500

@app.route('/api/download', methods=['POST'])
def download():
    """Endpoint para procesar descargas de recursos"""
    try:
        # Obtener datos del formulario
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({
                'success': False,
                'message': 'No se recibieron datos del formulario'
            }), 400
        
        # Validar campos requeridos
        required_fields = ['email', 'whatsapp', 'resource']
        missing_fields = [field for field in required_fields if not form_data.get(field)]
        
        if missing_fields:
            return jsonify({
                'success': False,
                'message': f'Faltan campos requeridos: {", ".join(missing_fields)}'
            }), 400
        
        # Validar email
        if not is_valid_email(form_data['email']):
            return jsonify({
                'success': False,
                'message': 'Email inválido'
            }), 400
        
        # Enviar email de descarga
        download_message = send_download_email(form_data)
        
        if download_message:
            return jsonify({
                'success': True,
                'message': 'Descarga procesada exitosamente. Revisa tu correo electrónico.',
                'data': {
                    'email': form_data.get('email'),
                    'resource': form_data.get('resource'),
                    'timestamp': datetime.now().isoformat()
                }
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Error al enviar correo electrónico de descarga'
            }), 500
    
    except Exception as e:
        print(f"Error en el endpoint de descarga: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Error interno del servidor',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 Iniciando servidor Del Campo Seguros - Cyber Risk Backend")
    print(f"📍 Puerto: {port}")
    print(f"🔧 Debug: {debug}")
    print(f"📧 SMTP: {SMTP_CONFIG['server']}:{SMTP_CONFIG['port']}")
    print(f"🏢 Empresa: {INSURANCE_INFO['company']}")
    print(f"👤 Broker: {INSURANCE_INFO['broker']}")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
