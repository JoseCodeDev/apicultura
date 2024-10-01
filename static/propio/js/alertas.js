export const mostrarAlerta = (titulo, mensaje, icono) => {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: icono,
        confirmButtonText: "Aceptar"
    });
}