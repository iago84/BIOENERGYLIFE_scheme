// CRUD JS autogenerado


// CRUD básico organulos
async function cargarOrganulos() {
    const res = await fetch('/api/organulos');
    const orgs = await res.json();
    // TODO: pintar en tablaOrganulos
}
function nuevoOrganulo() {
    // TODO: abrir modal creación
}
