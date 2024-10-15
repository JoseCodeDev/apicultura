import { mostrarAlertaPredeterminada } from "../alertas.js";
import { regex } from "./regex.js";

export function validarFormularioProductos(e) {
    let nombre = document.getElementById("nombreProducto").value.trim();
    let stock = document.getElementById("stockProducto").value.trim();
    let precioVenta = document.getElementById("precioVentaProducto").value.trim();
    let categoria = document.getElementById("categoriaProducto").value.trim();
    
    const stockMinimo = 1;
    const precioMinimo = 10;

    if (nombre === "" || stock === "" || precioVenta === "" || categoria === "") {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "Debe llenar todos los campos obligatorios", "error");
        return;
    }

    if (!regex.soloNumeros.test(stock)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El stock debe contener solo números", "error");
        return;
    } 
    
    if (!regex.numerosConPuntoDecimal.test(precioVenta)) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", "El precio de venta solo puede contener números con punto decimal", "error");
        return;
    } 
    
    if (parseInt(stock) < stockMinimo) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", `El stock debe ser igula o mayor a ${stockMinimo}`, "error");
        return;
    } 
    
    if (parseFloat(precioVenta) < precioMinimo) {
        e.preventDefault();
        mostrarAlertaPredeterminada("¡Error!", `El precio de venta debe ser igual o mayor a ${precioMinimo}`, "error");
        return;
    }
}
