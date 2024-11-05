export function esMayorDeEdad(fechaNacimiento) {
    let fechaNacimientoEmpleado = new Date(fechaNacimiento);

    let fechaActual = new Date();

    let edad = fechaActual.getFullYear() - fechaNacimientoEmpleado.getFullYear();

    let mesActual = fechaActual.getMonth();
    let diaActual = fechaActual.getDate();
    let mesNacimiento = fechaNacimientoEmpleado.getMonth();
    let diaNacimiento = fechaNacimientoEmpleado.getDate();

    if (mesActual < mesNacimiento || (mesActual === mesNacimiento && diaActual < diaNacimiento)) {
        edad--;
    }

    return edad >= 18;
}
