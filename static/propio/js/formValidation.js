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
            let stock = document.getElementById("stockProducto").value.trim();
            let categoria = document.getElementById("categoriaProducto").value.trim();

            // Expresión regular para validar solo números
            const regex = /^[0-9]+$/;
            const stockMinimo = 0;

            if (!regex.test(stock)) {
                e.preventDefault();
                mostrarAlerta("¡Error!", "El stock debe contener solo números", "error");
            }else if (stock <= stockMinimo) {
                e.preventDefault();
                mostrarAlerta("¡Error!", `El stock debe ser mayor a ${stockMinimo}`, "error");
            } else if (nombre == "" || stock =="" || categoria == "") {
                e.preventDefault();
                mostrarAlerta("¡Error!", "Debe llenar todos los campos obligatorios", "error");
            }
        }
    });
});