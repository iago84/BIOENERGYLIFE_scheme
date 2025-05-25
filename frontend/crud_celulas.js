// ===============================
// Archivo: crud_celulas.js
// Descripción: Funciones de CRUD para células, enlazado con celulas.html
// ===============================

/**
 * Carga las células desde el backend y las pinta en la tabla HTML.
 */
async function cargarCelulas() {
    const res = await fetch('/api/celulas');
    const cels = await res.json();
    const tbody = document.getElementById("tbodyCelulas");
    tbody.innerHTML = '';
    for (const cel of cels) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${cel.id}</td>
            <td>${cel.tipo}</td>
            <td>${cel.energia_actual}</td>
            <td>${cel.energia_maxima}</td>
            <td>${cel.estado}</td>
            <td>
                <button onclick="abrirModalEditar('${cel.id}')">Editar</button>
                <button onclick="borrarCelula('${cel.id}')">Borrar</button>
            </td>
        `;
        tbody.appendChild(tr);
    }
}

/**
 * Abre el modal para crear una nueva célula.
 */
function abrirModalCrear() {
    document.getElementById("modalTitulo").innerText = "Nueva célula";
    document.getElementById("modalId").value = "";
    document.getElementById("inputId").value = "";
    document.getElementById("inputTipo").value = "G";
    document.getElementById("inputEnergia").value = 1;
    document.getElementById("inputEnergiaMax").value = 10;
    document.getElementById("inputEstado").value = "activa";
    document.getElementById("modalFondo").style.display = "flex";
}

/**
 * Abre el modal para editar una célula existente.
 * @param {string} id - ID de la célula a editar.
 */
async function abrirModalEditar(id) {
    const res = await fetch(`/api/celulas/${id}`);
    const cel = await res.json();
    document.getElementById("modalTitulo").innerText = "Editar célula";
    document.getElementById("modalId").value = cel.id;
    document.getElementById("inputId").value = cel.id;
    document.getElementById("inputTipo").value = cel.tipo;
    document.getElementById("inputEnergia").value = cel.energia_actual;
    document.getElementById("inputEnergiaMax").value = cel.energia_maxima;
    document.getElementById("inputEstado").value = cel.estado;
    document.getElementById("modalFondo").style.display = "flex";
}

/**
 * Cierra el modal de creación/edición.
 */
function cerrarModal() {
    document.getElementById("modalFondo").style.display = "none";
}

/**
 * Guarda la célula nueva o editada en el backend.
 * @param {Event} e - Evento de submit del formulario.
 */
async function guardarCelula(e) {
    e.preventDefault();
    const modalId = document.getElementById("modalId").value;
    const celula = {
        id: document.getElementById("inputId").value.trim(),
        tipo: document.getElementById("inputTipo").value.trim(),
        energia_actual: Number(document.getElementById("inputEnergia").value),
        energia_maxima: Number(document.getElementById("inputEnergiaMax").value),
        estado: document.getElementById("inputEstado").value.trim(),
    };
    if (!celula.id) {
        alert("El ID es obligatorio");
        return;
    }
    if (modalId) {
        // Editar (PATCH)
        const res = await fetch(`/api/celulas/${celula.id}`, {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(celula)
        });
        if (res.ok) {
            cerrarModal();
            cargarCelulas();
        } else {
            const data = await res.json();
            alert("Error al editar: " + (data.error || res.statusText));
        }
    } else {
        // Crear (POST)
        const res = await fetch('/api/celulas', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(celula)
        });
        if (res.ok) {
            cerrarModal();
            cargarCelulas();
        } else {
            const data = await res.json();
            alert("Error al crear: " + (data.error || res.statusText));
        }
    }
}

/**
 * Borra una célula por su ID.
 * @param {string} id - ID de la célula a borrar.
 */
async function borrarCelula(id) {
    if (!confirm(`¿Seguro que quieres borrar la célula ${id}?`)) return;
    const res = await fetch(`/api/celulas/${id}`, { method: "DELETE" });
    if (res.ok) {
        cargarCelulas();
    } else {
        const data = await res.json();
        alert("Error al borrar: " + (data.error || res.statusText));
    }
}
