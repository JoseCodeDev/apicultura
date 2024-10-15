import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";

export function validarFormularioInsumos(e) {
    let nombre = document.getElementById("nombreInsumo").value.trim();
    let stock = document.getElementById("stockInsumo").value.trim();
    let categoria = document.getElementById("categoriaInsumo").value.trim();
    
    const stockMinimo = 1;

    if (nombre === "" || stock === "" || categoria === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
        return;
    }

    if (!regex.soloNumeros.test(stock)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El stock debe contener solo números", "error");
        return;
    } 
    
    if (parseInt(stock) < stockMinimo) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", `El stock debe ser igula o mayor a ${stockMinimo}`, "error");
        return;
    } 
}
