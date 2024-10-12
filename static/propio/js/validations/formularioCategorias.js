import { mostrarAlertaPredeterminada } from "../alertas.js";

export function validarFormularioCategorias(e) {
    let nombre = document.getElementById("nombreCategoria").value.trim();

    if (nombre === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
    }
}
