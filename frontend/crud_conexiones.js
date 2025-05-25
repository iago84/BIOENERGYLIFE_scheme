// ===============================
// Archivo: crud_conexiones.js
// Descripción: CRUD de conexiones, enlazado con conexiones.html
// ===============================

async function cargarConexiones() {
    const res = await fetch('/api/conexiones');
    const conns = await res.json();
    const tbody = document.getElementById("tbodyConexiones");
    tbody.innerHTML = '';
    for (const conn of conns) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${conn.id}</td>
            <td>${conn.origen}</td>
            <td>${conn.destino}</td>
            <td>${conn.tipo}</td>
            <td>
                <button onclick="abrirModalEditarConexion('${conn.id}')">Editar</button>
                <button onclick="borrarConexion('${conn.id}')">Borrar</button>
            </td>
        `;
        tbody.appendChild(tr);
    }
}

function abrirModalCrearConexion() {
    document.getElementById("modalTitulo").innerText = "Nueva conexión";
    document.getElementById("modalId").value = "";
    document.getElementById("inputId").value = "";
    document.getElementById("inputOrigen").value = "";
    document.getElementById("inputDestino").value = "";
    document.getElementById("inputTipo").value = "";
    document.getElementById("modalFondo").style.display = "flex";
}

async function abrirModalEditarConexion(id) {
    const res = await fetch(`/api/conexiones/${id}`);
    const conn = await res.json();
    document.getElementById("modalTitulo").innerText = "Editar conexión";
    document.getElementById("modalId").value = conn.id;
    document.getElementById("inputId").value = conn.id;
    document.getElementById("inputOrigen").value = conn.origen;
    document.getElementById("inputDestino").value = conn.destino;
    document.getElementById("inputTipo").value = conn.tipo;
    document.getElementById("modalFondo").style.display = "flex";
}

function cerrarModalConexion() {
    document.getElementById("modalFondo").style.display = "none";
}

async function guardarConexion(e) {
    e.preventDefault();
    const modalId = document.getElementById("modalId").value;
    const conn = {
        id: document.getElementById("inputId").value.trim(),
        origen: document.getElementById("inputOrigen").value.trim(),
        destino: document.getElementById("inputDestino").value.trim(),
        tipo: document.getElementById("inputTipo").value.trim(),
    };
    if (!conn.id) { alert("El ID es obligatorio"); return; }
    if (modalId) {
        // Editar
        const res = await fetch(`/api/conexiones/${conn.id}`, {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(conn)
        });
        if (res.ok) {
            cerrarModalConexion();
            cargarConexiones();
        } else {
            const data = await res.json();
            alert("Error al editar: " + (data.error || res.statusText));
        }
    } else {
        // Crear
        const res = await fetch('/api/conexiones', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(conn)
        });
        if (res.ok) {
            cerrarModalConexion();
            cargarConexiones();
        } else {
            const data = await res.json();
            alert("Error al crear: " + (data.error || res.statusText));
        }
    }
}

async function borrarConexion(id) {
    if (!confirm(`¿Seguro que quieres borrar la conexión ${id}?`)) return;
    const res = await fetch(`/api/conexiones/${id}`, { method: "DELETE" });
    if (res.ok) cargarConexiones();
    else {
        const data = await res.json();
        alert("Error al borrar: " + (data.error || res.statusText));
    }
}
