import { mostrarAlerta } from './alertas.js';

document.addEventListener("DOMContentLoaded", () => {
    document.addEventListener("submit", e => {
        // Formulario de categorias
        if ((e.target.matches("#frmAgregarCategoria")) || e.target.matches("#frmEditarCategoria")) {
            let nombre = document.getElementById("id_nombre").value.trim();

            if (nombre == "") {
                e.preventDefault();
                mostrarAlerta("¡Error!", "Debe llenar todos los campos obligatorios", "error");
            }
        }

        // Formulario de productos
        if ((e.target.matches("#frmAgregarProducto")) || e.target.matches("#frmEditarProducto")) {
            let nombre = document.getElementById("nombreProducto").value.trim();
            let precioVenta = document.getElementById("precioVentaProducto").value.trim();
            let categoria = document.getElementById("categoriaProducto").value.trim();
            let stock = document.getElementById("stockProducto").value.trim();
            let stock_minimo = document.getElementById("stockMinimoProducto").value.trim();
            let stock_maximo = document.getElementById("stockMaximoProducto").value.trim();

            // Expresión regular para validar solo números
            const regex = /^[0-9.]+$/;
            const stockMinimo = 1;
            const precioMinimo = 10;

            if (nombre == "" || stock ==""  || stock_minimo ==""  || stock_maximo =="" || precioVenta == "" || categoria == "") {
                e.preventDefault();
                mostrarAlerta("¡Error!", "Debe llenar todos los campos obligatorios", "error");
            }
            else if (!regex.test(stock) || !regex.test(stock_minimo) || !regex.test(stock_maximo)) {
                e.preventDefault();
                mostrarAlerta("¡Error!", "Los stocks debe contener solo números", "error");
            }else if (!regex.test(precioVenta)) {
                e.preventDefault();
                mostrarAlerta("¡Error!", "El precio de venta debe contener solo números", "error");
            }else if (stock < stockMinimo) {
                e.preventDefault();
                mostrarAlerta("¡Error!", `El stock debe ser igula o mayor a ${stockMinimo}`, "error");
            }else if (precioVenta < precioMinimo) {
                e.preventDefault();
                mostrarAlerta("¡Error!", `El precio de venta debe ser igual o mayor a ${precioMinimo}`, "error");
            }
        }
    });
});