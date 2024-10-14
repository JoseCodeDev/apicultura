import { mostrarMensajeToast } from "./alertas.js";

export function verificarMensajes() {
    const mensajesElement = document.getElementById("mensajes");

    if (mensajesElement) {
        const mensajes = JSON.parse(mensajesElement.getAttribute("data-mensajes"));
        mostrarMensajeToast(mensajes);
    }
}
