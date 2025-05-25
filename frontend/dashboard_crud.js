// ===============================
// dashboard_crud.js
// CRUD universal con modal único para células, orgánulos, generadores, conexiones
// ===============================

const entidades = {
    celulas: {
        nombre: "Células",
        campos: [
            { id: "id", label: "ID", tipo: "text", requerido: true },
            { id: "tipo", label: "Tipo", tipo: "text", requerido: true },
            { id: "energia_actual", label: "Energía", tipo: "number", requerido: true },
            { id: "energia_maxima", label: "Energía máxima", tipo: "number", requerido: true },
            { id: "estado", label: "Estado", tipo: "text", requerido: true }
        ],
        endpoint: "/api/celulas"
    },
    organulos: {
        nombre: "Orgánulos",
        campos: [
            { id: "id", label: "ID", tipo: "text", requerido: true },
            { id: "tipo", label: "Tipo", tipo: "text", requerido: true },
            { id: "potencia", label: "Potencia", tipo: "number", requerido: true },
            { id: "estado", label: "Estado", tipo: "text", requerido: true },
            { id: "celula_asociada", label: "Célula asociada", tipo: "text", requerido: true }
        ],
        endpoint: "/api/organulos"
    },
    generadores: {
        nombre: "Generadores",
        campos: [
            { id: "id", label: "ID", tipo: "text", requerido: true },
            { id: "tipo", label: "Tipo", tipo: "text", requerido: true },
            { id: "potencia_kw", label: "Potencia (kW)", tipo: "number", requerido: true },
            { id: "eficiencia", label: "Eficiencia", tipo: "number", requerido: true },
            { id: "voltaje_salida_v", label: "Voltaje salida", tipo: "number", requerido: true }
        ],
        endpoint: "/api/generadores"
    },
    conexiones: {
        nombre: "Conexiones",
        campos: [
            { id: "id", label: "ID", tipo: "text", requerido: true },
            { id: "origen", label: "Origen", tipo: "text", requerido: true },
            { id: "destino", label: "Destino", tipo: "text", requerido: true },
            { id: "tipo", label: "Tipo", tipo: "text", requerido: true }
        ],
        endpoint: "/api/conexiones"
    }
};

let entidadActual = "celulas";

// Renderiza la tabla CRUD de la entidad seleccionada
async function mostrarTablaCrud(entidad) {
    entidadActual = entidad;
    const ent = entidades[entidad];
    const res = await fetch(ent.endpoint);
    const datos = await res.json();
    let html = `<h4>${ent.nombre}</h4><button onclick="abrirCrudModal('crear')">Nuevo</button>`;
    html += `<table style="width:99%; margin-top:1em;"><thead><tr>`;
    for (const campo of ent.campos) html += `<th>${campo.label}</th>`;
    html += `<th>Acciones</th></tr></thead><tbody>`;
    for (const d of datos) {
        html += `<tr>`;
        for (const campo of ent.campos) html += `<td>${d[campo.id] ?? ""}</td>`;
        html += `<td>
            <button onclick="abrirCrudModal('editar', '${d.id}')">Editar</button>
            <button onclick="borrarEntidad('${d.id}')">Borrar</button>
        </td></tr>`;
    }
    html += "</tbody></table>";
    document.getElementById("tablaCrudContainer").innerHTML = html;
}

// Abre el modal universal en modo "crear" o "editar"
async function abrirCrudModal(modo, id=null) {
    const ent = entidades[entidadActual];
    document.getElementById("crudTitle").innerText = (modo === "crear" ? "Nuevo " : "Editar ") + ent.nombre.slice(0, -1);
    document.getElementById("crudSubmit").onclick = guardarEntidad;
    const form = document.getElementById("crudForm");
    form.innerHTML = "";
    let valores = {};
    if (modo === "editar" && id) {
        const res = await fetch(ent.endpoint + "/" + id);
        valores = await res.json();
    }
    for (const campo of ent.campos) {
        form.innerHTML += `<label>${campo.label}: <input name="${campo.id}" type="${campo.tipo}" value="${valores[campo.id] ?? ''}" ${campo.requerido ? "required" : ""}/></label><br/>`;
    }
    form.setAttribute("data-modo", modo);
    form.setAttribute("data-id", id ?? "");
    document.getElementById("crudModal").style.display = "flex";
}

function cerrarCrudModal() {
    document.getElementById("crudModal").style.display = "none";
}

// Guarda entidad (crea o edita)
async function guardarEntidad(e) {
    e.preventDefault && e.preventDefault();
    const ent = entidades[entidadActual];
    const form = document.getElementById("crudForm");
    const modo = form.getAttribute("data-modo");
    const id = form.getAttribute("data-id");
    const data = {};
    for (const campo of ent.campos) {
        const val = form.elements[campo.id].value;
        data[campo.id] = campo.tipo === "number" ? Number(val) : val;
    }
    let res;
    if (modo === "crear") {
        res = await fetch(ent.endpoint, {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    } else {
        res = await fetch(ent.endpoint + "/" + id, {
            method: "PATCH",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }
    if (res.ok) {
        cerrarCrudModal();
        mostrarTablaCrud(entidadActual);
    } else {
        const d = await res.json();
        alert("Error: " + (d.error || res.statusText));
    }
}

// Borra entidad
async function borrarEntidad(id) {
    if (!confirm("¿Seguro que quieres borrar el registro " + id + "?")) return;
    const ent = entidades[entidadActual];
    const res = await fetch(ent.endpoint + "/" + id, { method: "DELETE" });
    if (res.ok) mostrarTablaCrud(entidadActual);
    else {
        const d = await res.json();
        alert("Error: " + (d.error || res.statusText));
    }
}

// Cierra el modal con la X
document.getElementById("closeCrud").onclick = cerrarCrudModal;

// Arranque: muestra por defecto la tabla de células
mostrarTablaCrud("celulas");


async function cargarEstadisticas() {
    // Puedes adaptar el endpoint si tienes uno específico, o combinar varias llamadas
    const resCelulas = await fetch('/api/celulas');
    const celulas = await resCelulas.json();
    const resGeneradores = await fetch('/api/generadores');
    const generadores = await resGeneradores.json();
    const resOrganulos = await fetch('/api/organulos');
    const organulos = await resOrganulos.json();

    // Ejemplo de métricas
    const energiaTotal = celulas.reduce((s, c) => s + (c.energia_actual || 0), 0);
    const energiaMaxima = celulas.reduce((s, c) => s + (c.energia_maxima || 0), 0);
    const potenciaGeneradores = generadores.reduce((s, g) => s + (g.potencia_kw || 0), 0);

    document.getElementById("stats").innerHTML = `
        <strong>Células:</strong> ${celulas.length}<br>
        <strong>Orgánulos:</strong> ${organulos.length}<br>
        <strong>Generadores:</strong> ${generadores.length}<br>
        <strong>Energía total acumulada:</strong> ${energiaTotal} kW<br>
        <strong>Energía máxima posible:</strong> ${energiaMaxima} kW<br>
        <strong>Potencia total generadores:</strong> ${potenciaGeneradores} kW
    `;
}

// Llama a cargarEstadisticas() cada vez que cambie algo relevante
setInterval(cargarEstadisticas, 3000); // Actualiza cada 3 segundos
// También llama después de crear/borrar entidades, si quieres feedback inmediato
