export function esFechaAnteriorOIgual(fecha1, fecha2) {
    // Convertir ambas fechas a objetos Date si son cadenas
    const fecha1Obj = typeof fecha1 === 'string' ? new Date(fecha1) : fecha1;
    const fecha2Obj = typeof fecha2 === 'string' ? new Date(fecha2) : fecha2;

    // Comparar las fechas
    return fecha1Obj <= fecha2Obj;
}