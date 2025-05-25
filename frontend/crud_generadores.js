// CRUD JS autogenerado


// CRUD básico generadores
async function cargarGeneradores() {
    const res = await fetch('/api/generadores');
    const gens = await res.json();
    // TODO: pintar en tablaGeneradores
}
function nuevoGenerador() {
    // TODO: abrir modal creación
}
