document.addEventListener("DOMContentLoaded", function () {
    const mensajesElement = document.getElementById("mensajes");

    if (mensajesElement) {
        const mensajes = JSON.parse(mensajesElement.getAttribute("data-mensajes"));
        mostrarMensajes(mensajes);
    }
});

function mostrarMensajes(messages) {
    messages.forEach(function (message) {
        if (message.tag === 'error') {
            Swal.fire({
                title: "¡Error!",
                text: message.text,
                icon: "error",
                confirmButtonText: "Aceptar"
            });
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
