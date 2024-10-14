import { validarFormularios } from "../validarFormularios.js";

document.addEventListener("submit", e => {
    validarFormularios(e);
});