// Función para mostrar alertas
function showAlert(message, type = 'success', field = null) {
    // Crear el elemento de alerta
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    
    // Crear el contenido de la alerta
    const alertContent = document.createElement('div');
    alertContent.className = 'alert-content';
    
    // Agregar el mensaje
    const messageText = document.createElement('span');
    messageText.textContent = message;
    
    // Si hay un campo específico, agregarlo
    if (field) {
        const fieldText = document.createElement('strong');
        fieldText.textContent = `[${field}]`;
        alertContent.appendChild(fieldText);
    }
    
    alertContent.appendChild(messageText);
    alert.appendChild(alertContent);
    
    // Agregar la alerta al documento
    document.body.appendChild(alert);
    
    // Remover la alerta después de 3 segundos
    setTimeout(() => {
        alert.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(alert);
        }, 300);
    }, 3000);
}

// Función para manejar el envío del formulario
function handleSubmit(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    
    // Validar campos
    let isValid = true;
    let firstInvalidField = null;
    
    formData.forEach((value, key) => {
        if (!value.trim()) {
            isValid = false;
            if (!firstInvalidField) {
                firstInvalidField = key;
            }
        }
    });
    
    if (!isValid) {
        showAlert('Por favor, complete todos los campos', 'error', firstInvalidField);
        return;
    }
    
    // Enviar el formulario
    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert(data.message, 'success');
            setTimeout(() => {
                window.location.href = data.redirect;
            }, 1000);
        } else {
            showAlert(data.message, 'error', data.field);
        }
    })
    .catch(error => {
        showAlert('Error al procesar la solicitud', 'error');
    });
}

// Agregar el manejador de eventos al formulario
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', handleSubmit);
    }
}); 