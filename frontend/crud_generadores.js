// ===============================
// Archivo: crud_generadores.js
// Descripción: CRUD de generadores, enlazado con generadores.html
// ===============================

async function cargarGeneradores() {
    const res = await fetch('/api/generadores');
    const gens = await res.json();
    const tbody = document.getElementById("tbodyGeneradores");
    tbody.innerHTML = '';
    for (const gen of gens) {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${gen.id}</td>
            <td>${gen.tipo}</td>
            <td>${gen.potencia_kw}</td>
            <td>${gen.eficiencia}</td>
            <td>${gen.voltaje_salida_v}</td>
            <td>
                <button onclick="abrirModalEditarGenerador('${gen.id}')">Editar</button>
                <button onclick="borrarGenerador('${gen.id}')">Borrar</button>
            </td>
        `;
        tbody.appendChild(tr);
    }
}

function abrirModalCrearGenerador() {
    document.getElementById("modalTitulo").innerText = "Nuevo generador";
    document.getElementById("modalId").value = "";
    document.getElementById("inputId").value = "";
    document.getElementById("inputTipo").value = "";
    document.getElementById("inputPotencia").value = "";
    document.getElementById("inputEficiencia").value = "";
    document.getElementById("inputVoltaje").value = "";
    document.getElementById("modalFondo").style.display = "flex";
}

async function abrirModalEditarGenerador(id) {
    const res = await fetch(`/api/generadores/${id}`);
    const gen = await res.json();
    document.getElementById("modalTitulo").innerText = "Editar generador";
    document.getElementById("modalId").value = gen.id;
    document.getElementById("inputId").value = gen.id;
    document.getElementById("inputTipo").value = gen.tipo;
    document.getElementById("inputPotencia").value = gen.potencia_kw;
    document.getElementById("inputEficiencia").value = gen.eficiencia;
    document.getElementById("inputVoltaje").value = gen.voltaje_salida_v;
    document.getElementById("modalFondo").style.display = "flex";
}

function cerrarModalGenerador() {
    document.getElementById("modalFondo").style.display = "none";
}

async function guardarGenerador(e) {
    e.preventDefault();
    const modalId = document.getElementById("modalId").value;
    const gen = {
        id: document.getElementById("inputId").value.trim(),
        tipo: document.getElementById("inputTipo").value.trim(),
        potencia_kw: Number(document.getElementById("inputPotencia").value),
        eficiencia: Number(document.getElementById("inputEficiencia").value),
        voltaje_salida_v: Number(document.getElementById("inputVoltaje").value)
    };
    if (!gen.id) { alert("El ID es obligatorio"); return; }
    if (modalId) {
        // Editar
        const res = await fetch(`/api/generadores/${gen.id}`, {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(gen)
        });
        if (res.ok) {
            cerrarModalGenerador();
            cargarGeneradores();
        } else {
            const data = await res.json();
            alert("Error al editar: " + (data.error || res.statusText));
        }
    } else {
        // Crear
        const res = await fetch('/api/generadores', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(gen)
        });
        if (res.ok) {
            cerrarModalGenerador();
            cargarGeneradores();
        } else {
            const data = await res.json();
            alert("Error al crear: " + (data.error || res.statusText));
        }
    }
}

async function borrarGenerador(id) {
    if (!confirm(`¿Seguro que quieres borrar el generador ${id}?`)) return;
    const res = await fetch(`/api/generadores/${id}`, { method: "DELETE" });
    if (res.ok) cargarGeneradores();
    else {
        const data = await res.json();
        alert("Error al borrar: " + (data.error || res.statusText));
    }
}
