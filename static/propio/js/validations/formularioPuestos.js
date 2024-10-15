import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";

export function validarFormularioPuestos(e) {
    let nombre = document.getElementById("nombrePuesto").value.trim();

    if (nombre === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
        return;
    }

    if (!regex.letrasConEspacios.test(nombre)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El nombre puede contener solo letras y espacios en blanco", "error");
        return;
    } 
}
