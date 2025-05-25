// CRUD JS autogenerado


// CRUD básico conexiones
async function cargarConexiones() {
    const res = await fetch('/api/conexiones');
    const conns = await res.json();
    // TODO: pintar en tablaConexiones
}
function nuevaConexion() {
    // TODO: abrir modal creación
}
