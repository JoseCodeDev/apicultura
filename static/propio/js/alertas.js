export const mostrarAlertaPredeterminada = (titulo, mensaje, icono) => {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: icono,
        confirmButtonText: "Aceptar"
    });
}

export function mostrarMensajeToast(messages) {
    messages.forEach(function (message) {
        if (message.tag === 'error') {
            mostrarAlertaPredeterminada("¡Error!", message.text, "error");
        } else {
            const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.onmouseenter = Swal.stopTimer;
                    toast.onmouseleave = Swal.resumeTimer;
                }
            });
            Toast.fire({
                icon: 'success',
                title: message.text
            });
        }
    });
}