// ===============================
// Archivo: crud_organulos.js
// Descripción: CRUD de orgánulos, enlazado con organulos.html
// ===============================

async function cargarOrganulos() {
    const res = await fetch('/api/organulos');
    const orgs = await res.json();
    const tbody = document.getElementById("tbodyOrganulos");
    tbody.innerHTML = '';
    for (const org of orgs) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${org.id}</td>
            <td>${org.tipo}</td>
            <td>${org.potencia}</td>
            <td>${org.estado}</td>
            <td>${org.celula_asociada}</td>
            <td>
                <button onclick="abrirModalEditarOrganulo('${org.id}')">Editar</button>
                <button onclick="borrarOrganulo('${org.id}')">Borrar</button>
            </td>
        `;
        tbody.appendChild(tr);
    }
}

function abrirModalCrearOrganulo() {
    document.getElementById("modalTitulo").innerText = "Nuevo orgánulo";
    document.getElementById("modalId").value = "";
    document.getElementById("inputId").value = "";
    document.getElementById("inputTipo").value = "";
    document.getElementById("inputPotencia").value = "";
    document.getElementById("inputEstado").value = "pasivo";
    document.getElementById("inputCelulaAsociada").value = "";
    document.getElementById("modalFondo").style.display = "flex";
}

async function abrirModalEditarOrganulo(id) {
    const res = await fetch(`/api/organulos/${id}`);
    const org = await res.json();
    document.getElementById("modalTitulo").innerText = "Editar orgánulo";
    document.getElementById("modalId").value = org.id;
    document.getElementById("inputId").value = org.id;
    document.getElementById("inputTipo").value = org.tipo;
    document.getElementById("inputPotencia").value = org.potencia;
    document.getElementById("inputEstado").value = org.estado;
    document.getElementById("inputCelulaAsociada").value = org.celula_asociada;
    document.getElementById("modalFondo").style.display = "flex";
}

function cerrarModalOrganulo() {
    document.getElementById("modalFondo").style.display = "none";
}

async function guardarOrganulo(e) {
    e.preventDefault();
    const modalId = document.getElementById("modalId").value;
    const org = {
        id: document.getElementById("inputId").value.trim(),
        tipo: document.getElementById("inputTipo").value.trim(),
        potencia: Number(document.getElementById("inputPotencia").value),
        estado: document.getElementById("inputEstado").value.trim(),
        celula_asociada: document.getElementById("inputCelulaAsociada").value.trim(),
    };
    if (!org.id) { alert("El ID es obligatorio"); return; }
    if (modalId) {
        // Editar
        const res = await fetch(`/api/organulos/${org.id}`, {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(org)
        });
        if (res.ok) {
            cerrarModalOrganulo();
            cargarOrganulos();
        } else {
            const data = await res.json();
            alert("Error al editar: " + (data.error || res.statusText));
        }
    } else {
        // Crear
        const res = await fetch('/api/organulos', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(org)
        });
        if (res.ok) {
            cerrarModalOrganulo();
            cargarOrganulos();
        } else {
            const data = await res.json();
            alert("Error al crear: " + (data.error || res.statusText));
        }
    }
}

async function borrarOrganulo(id) {
    if (!confirm(`¿Seguro que quieres borrar el orgánulo ${id}?`)) return;
    const res = await fetch(`/api/organulos/${id}`, { method: "DELETE" });
    if (res.ok) cargarOrganulos();
    else {
        const data = await res.json();
        alert("Error al borrar: " + (data.error || res.statusText));
    }
}
