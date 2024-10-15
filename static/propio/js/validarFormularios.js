import { validarFormularioCategorias } from './validations/formularioCategorias.js';
import { validarFormularioProductos } from './validations/formularioProductos.js';
import { validarFormularioClientes } from './validations/formularioClientes.js';
import { validarFormularioInsumos } from './validations/formularioInsumos.js';
import { validarFormularioPuestos } from './validations/formularioPuestos.js';
import { validarFormularioDepartamentos } from './validations/formularioDepartamentos.js';

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

    if ((e.target.matches("#frmAgregarinsumo")) || e.target.matches("#frmEditarInsumo")) {
        validarFormularioInsumos(e);
        return;
    }

    if ((e.target.matches("#frmAgregarPuesto")) || e.target.matches("#frmEditarPuesto")) {
        validarFormularioPuestos(e);
        return;
    }

    if ((e.target.matches("#frmAgregarDepartamento")) || e.target.matches("#frmEditarDepartamento")) {
        validarFormularioDepartamentos(e);
        return;
    }
}