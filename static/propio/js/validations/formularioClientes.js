import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";

export function validarFormularioClientes(e) {
    let nombres = document.getElementById("nombresCliente").value.trim();
    let apellidos = document.getElementById("apellidosCliente").value.trim();
    let genero = document.getElementById("generoCliente").value.trim();
    let telefono = document.getElementById("telefonoCliente").value.trim();
    let email = document.getElementById("emailCliente").value.trim();

    if (nombres === "" || apellidos === "" || genero === "" || telefono === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
        return;
    }

    if (!regex.letrasConEspacios.test(nombres)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El nombre solo debe contener letras y espacios en blanco", "error");
        return;
    } 
    
    if (!regex.letrasConEspacios.test(apellidos)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Los apellidos solo deben contener letras y espacios en blanco", "error");
        return;
    } 

    if (!regex.genero.test(genero)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El género solo puede ser masculino o femenino", "error");
        return;
    } 
    
    if (email !== "" && !regex.email.test(email)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El email ingresado no es válido", "error");
        return;
    }
}
