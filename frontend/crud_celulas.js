// CRUD JS autogenerado


// CRUD básico celulas
async function cargarCelulas() {
    const res = await fetch('/api/celulas');
    const cels = await res.json();
    // TODO: pintar en tablaCelulas
}
function nuevaCelula() {
    // TODO: abrir modal creación
}
