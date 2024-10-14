import { validarFormularioCategorias } from './validations/formularioCategorias.js';
import { validarFormularioProductos } from './validations/formularioProductos.js';
import { validarFormularioClientes } from './validations/formularioClientes.js';

export function validarFormularios(e) {
    if ((e.target.matches("#frmAgregarCategoria")) || e.target.matches("#frmEditarCategoria")) {
        validarFormularioCategorias(e);
        return;
    }
    
    if ((e.target.matches("#frmAgregarProducto")) || e.target.matches("#frmEditarProducto")) {
        validarFormularioProductos(e);
        return;
    }

    if ((e.target.matches("#frmAgregarCliente")) || e.target.matches("#frmEditarCliente")) {
        validarFormularioClientes(e);
        return;
    }
}