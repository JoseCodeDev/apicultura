import { mostrarAlerta } from "./alertas";

function mostrarMensajes(messages) {
    messages.forEach(function (message) {
        if (message.tag === 'error') {
            mostrarAlerta("¡Error!", message.text, "error");
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
