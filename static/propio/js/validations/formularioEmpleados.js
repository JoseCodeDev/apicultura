import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";
import { esMayorDeEdad } from "./mayorDeEdad.js";
import { esFechaAnteriorOIgual } from "./esFechaAnteriorOIgual.js";

export function validarFormularioEmpleados(e) {
    let nombres = document.getElementById("nombresEmpleado").value.trim();
    let apellidos = document.getElementById("apellidosEmpleado").value.trim();
    let fechaNacimiento = document.getElementById("fechaNacimientoEmpleado").value.trim();
    let sexo = document.getElementById("sexoEmpleado").value.trim();
    let direccion = document.getElementById("direccionEmpleado").value.trim();
    let telefono = document.getElementById("telefonoEmpleado").value.trim();
    let grupoSanguineo = document.getElementById("grupoSanguineoEmpleado").value.trim();
    let fechaContratacion = document.getElementById("fechaContratacionEmpleado").value.trim();
    let puesto = document.getElementById("puestoEmpleado").value.trim();
    let departamento = document.getElementById("departamentoEmpleado").value.trim();
    let fechaAltaSS = document.getElementById("fechaAltaSSEmpleado").value.trim();
    let nss = document.getElementById("nssEmpleado").value.trim();
    let clabeInterbancaria = document.getElementById("clabeInterbancariaEmpleado").value.trim();
    let contactoEmergenciaNombres = document.getElementById("contactoEmergenciaNombresEmpleado").value.trim();
    let contactoEmergenciaApellidos = document.getElementById("contactoEmergenciaApellidosEmpleado").value.trim();
    let contactoEmergenciaTelefono = document.getElementById("contactoEmergenciaTelefonoEmpleado").value.trim();
    let contactoEmergenciaParentesco = document.getElementById("contactoEmergenciaParentescoEmpleado").value.trim();
    // let activo = document.getElementById("activoEmpleado").checked;

    const camposObligatorios = [
        nombres, apellidos, fechaNacimiento, sexo, direccion, telefono,
        grupoSanguineo, fechaContratacion, puesto, departamento, fechaAltaSS,
        nss, clabeInterbancaria, contactoEmergenciaNombres, contactoEmergenciaApellidos,
        contactoEmergenciaTelefono, contactoEmergenciaParentesco
    ];

    if (camposObligatorios.some(campo => campo === "")) {
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

    if (!esMayorDeEdad(fechaNacimiento)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El empleado debe tener al menos 18 años para poder trabajar", "error");
        return;
    }

    if (!regex.genero.test(sexo)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El sexo solo puede ser masculino o femenino", "error");
        return;
    }

    if (!regex.telefono10Digitos.test(telefono)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El número de teléfono solo debe números y tener exactamente 10 dígitos", "error");
        return;
    }

    if (!regex.grupoSanguineo.test(grupoSanguineo)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El grupo sanguíneo no es válido", "error");
        return;
    }

    if (!esFechaAnteriorOIgual(fechaContratacion, new Date())) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "La fecha de contratación no puede ser posterior a la fecha actual", "error");
        return;
    }

    if (!esFechaAnteriorOIgual(fechaAltaSS, new Date())) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "La fecha de alta en el SS no puede ser posterior a la fecha actual", "error");
        return;
    }

    if (!regex.soloNumeros.test(nss) || nss.length != 11) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El NSS solo debe contener números y tener exactamente 11 dígitos", "error");
        return;
    }

    if (!regex.soloNumeros.test(clabeInterbancaria) || clabeInterbancaria.length != 18) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "La CLABLE solo debe contener números y tener exactamente 18 dígitos", "error");
        return;
    }

    if (!regex.letrasConEspacios.test(contactoEmergenciaNombres)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El nombre del contacto de emergencia solo debe contener letras y espacios en blanco", "error");
        return;
    }

    if (!regex.letrasConEspacios.test(contactoEmergenciaApellidos)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Los apellidos del contacto de emergencia solo deben contener letras y espacios en blanco", "error");
        return;
    }

    if (!regex.telefono10Digitos.test(contactoEmergenciaTelefono)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El número de teléfono del contacto de emergencia solo debe números y tener exactamente 10 dígitos", "error");
        return;
    }
}
