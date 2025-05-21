document.addEventListener('DOMContentLoaded', function() {
    // Elementos del formulario de registro
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        const passwordInput = document.getElementById('password');
        const passwordConfirmInput = document.getElementById('password2');
        const usernameInput = document.getElementById('username');
        const emailInput = document.getElementById('email');
        
        // Validar email en tiempo real
        emailInput.addEventListener('input', function() {
            validateEmail(this.value);
        });
        
        // Validar contraseña en tiempo real
        passwordInput.addEventListener('input', function() {
            validatePassword(this.value, 'Contraseña');
        });
        
        // Validar coincidencia de contraseñas
        passwordConfirmInput.addEventListener('input', function() {
            const password = passwordInput.value;
            const confirmPassword = this.value;
            
            if (password !== confirmPassword) {
                showAlert('Las contraseñas no coinciden', 'error', 'Confirmar Contraseña');
            } else {
                hideAlert();
            }
        });
        
        // Validar formulario al enviar
        registrationForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Validar campos vacíos
            if (!usernameInput.value) {
                showAlert('El campo Usuario es requerido', 'error', 'Usuario');
                return;
            }
            if (!emailInput.value) {
                showAlert('El campo Email es requerido', 'error', 'Email');
                return;
            }
            if (!validateEmail(emailInput.value)) {
                return;
            }
            if (!passwordInput.value) {
                showAlert('El campo Contraseña es requerido', 'error', 'Contraseña');
                return;
            }
            if (!passwordConfirmInput.value) {
                showAlert('El campo Confirmar Contraseña es requerido', 'error', 'Confirmar Contraseña');
                return;
            }
            
            const password = passwordInput.value;
            const confirmPassword = passwordConfirmInput.value;
            const isValidPassword = validatePassword(password, true, 'Contraseña');
            
            if (password !== confirmPassword) {
                showAlert('Las contraseñas no coinciden', 'error', 'Confirmar Contraseña');
                return;
            }
            
            if (isValidPassword) {
                showAlert('Registro exitoso! Redirigiendo...', 'success');
                setTimeout(() => {
                    window.location.href = "/";
                }, 3000);
            }
        });
    }

    // Elementos del formulario de inicio de sesión
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            if (!username) {
                showAlert('El campo Usuario es requerido', 'error', 'Usuario');
                return;
            }
            if (!password) {
                showAlert('El campo Contraseña es requerido', 'error', 'Contraseña');
                return;
            }

            // Aquí iría la lógica de autenticación
            showAlert('Iniciando sesión...', 'success');
        });
    }

    // Elementos del formulario de restablecer contraseña
    const resetForm = document.getElementById('resetForm');
    if (resetForm) {
        resetForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;

            if (!username) {
                showAlert('El campo Usuario es requerido', 'error', 'Usuario');
                return;
            }

            showAlert('Se ha enviado un correo a su cuenta asociada', 'success');
            setTimeout(() => {
                window.location.href = "/";
            }, 3000);
        });
    }
});

// Función para validar la contraseña
function validatePassword(password, showAllErrors = false, fieldName = 'Contraseña') {
    let isValid = true;
    const requirements = {
        length: { valid: password.length >= 8, message: 'Mínimo 8 caracteres' },
        uppercase: { valid: /[A-Z]/.test(password), message: 'Al menos una mayúscula' },
        number: { valid: /[0-9]/.test(password), message: 'Al menos un número' },
        special: { valid: /[.,!)(#]/.test(password), message: 'Al menos un carácter especial (.,!)(#)' },
        repeat: { valid: !/(.)\1{4,}/.test(password), message: 'No más de 4 repeticiones del mismo carácter' },
        sequence: { valid: !/(?:abc|bcd|cde|def|efg|123|234|345|456|789|987|876|765|654|543|432|321)/i.test(password), 
                   message: 'Sin secuencias consecutivas' }
    };

    for (const [key, req] of Object.entries(requirements)) {
        if (!req.valid) {
            if (showAllErrors) {
                showAlert(`${fieldName}: ${req.message}`, 'error', fieldName);
            }
            isValid = false;
        }
    }

    return isValid;
}

// Función para validar el email
function validateEmail(email) {
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    
    if (!email) {
        showAlert('El campo Email es requerido', 'error', 'Email');
        return false;
    }
    
    if (!emailRegex.test(email)) {
        showAlert('Por favor, ingrese un email válido', 'error', 'Email');
        return false;
    }
    
    // Validar longitud máxima
    if (email.length > 100) {
        showAlert('El email no puede tener más de 100 caracteres', 'error', 'Email');
        return false;
    }
    
    // Validar dominio común o institucional
    const commonDomains = ['gmail.com', 'hotmail.com', 'outlook.com', 'yahoo.com'];
    const institutionalDomains = ['alumno.ipn.mx', 'ipn.mx'];
    const domain = email.split('@')[1];
    
    if (!commonDomains.includes(domain) && !institutionalDomains.includes(domain)) {
        showAlert('Por favor, use un dominio de correo válido (Gmail, Hotmail, Outlook, Yahoo o correo institucional IPN)', 'error', 'Email');
        return false;
    }
    
    // Validación específica para correos institucionales del IPN
    if (domain === 'alumno.ipn.mx') {
        const username = email.split('@')[0];
        // Validar formato de correo institucional: primera letra del nombre + apellido + matrícula
        const institutionalRegex = /^[a-z][a-z]+[0-9]{8}$/;
        if (!institutionalRegex.test(username)) {
            showAlert('El formato del correo institucional debe ser: primera letra del nombre + apellido + matrícula (8 dígitos)', 'error', 'Email');
            return false;
        }
    }
    
    return true;
}

// Función para mostrar alertas estilizadas
function showAlert(message, type, fieldName = '') {
    // Eliminar alerta anterior si existe
    hideAlert();

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    
    // Crear el contenido de la alerta con el campo específico
    const alertContent = document.createElement('div');
    alertContent.className = 'alert-content';
    
    if (fieldName) {
        const fieldLabel = document.createElement('strong');
        fieldLabel.textContent = `${fieldName}: `;
        alertContent.appendChild(fieldLabel);
    }
    
    const messageText = document.createTextNode(message);
    alertContent.appendChild(messageText);
    
    alert.appendChild(alertContent);
    
    // Insertar después del formulario
    const form = document.querySelector('form');
    form.parentNode.insertBefore(alert, form.nextSibling);

    // Auto-ocultar después de 3 segundos
    setTimeout(() => {
        hideAlert();
    }, 3000);
}

// Función para ocultar alertas
function hideAlert() {
    const existingAlert = document.querySelector('.alert');
    if (existingAlert) {
        existingAlert.remove();
    }
} 