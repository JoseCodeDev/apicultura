import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";

export function validarFormularioDepartamentos(e) {
    let nombre = document.getElementById("nombreDepartamento").value.trim();

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
