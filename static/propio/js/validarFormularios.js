import { validarFormularioCategorias } from './validations/formularioCategorias.js';
import { validarFormularioProductos } from './validations/formularioProductos.js';

export function validarFormularios(e) {
    if ((e.target.matches("#frmAgregarCategoria")) || e.target.matches("#frmEditarCategoria")) {
        validarFormularioCategorias(e);
        return;
    }
    
    if ((e.target.matches("#frmAgregarProducto")) || e.target.matches("#frmEditarProducto")) {
        validarFormularioProductos(e);
        return;
    }
}