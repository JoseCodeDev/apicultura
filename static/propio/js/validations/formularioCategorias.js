import { mostrarAlertaPredeterminada } from "../alertas.js";

export function validarFormularioCategorias(e) {
    let nombre = document.getElementById("nombreCategoria").value.trim();
    let tipo = document.getElementById("tipoCategoria").value.trim();

    const tiposValidos = ["producto", "insumo"];

    if (nombre === "" || tipo === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
    }

    if (!tiposValidos.includes(tipo)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe seleccionar un tipo válido de categoría", "error");
        return;
    }
}
