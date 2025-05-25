// === app.js moderno para diseño y simulación celular ===

class Celula {
    constructor(data) {
        Object.assign(this, data);
        this.x = data.ubicacion?.x ?? 100;
        this.y = data.ubicacion?.y ?? 100;
    }

    color() {
        if (this.energia_actual >= 5) return "lime";
        if (this.energia_actual >= 2) return "yellow";
        return "red";
    }

    draw(ctx, selected = false) {
        // Aura por energía alta
        if (this.energia_actual >= 5) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, 36, 0, 2 * Math.PI);
            ctx.fillStyle = "rgba(100,255,100,0.2)";
            ctx.fill();
        }
        // Cuerpo de la célula
        ctx.beginPath();
        ctx.arc(this.x, this.y, 30, 0, 2 * Math.PI);
        ctx.fillStyle = this.color();
        ctx.fill();
        ctx.lineWidth = selected ? 4 : 1.5;
        ctx.strokeStyle = selected ? "#0af" : "#fff";
        ctx.stroke();

        // Texto
        ctx.fillStyle = "#000";
        ctx.font = "12px monospace";
        ctx.fillText(`${this.id} (${this.energia_actual?.toFixed(1) ?? "?"})`, this.x - 30, this.y - 35);
    }
}

class Relacion {
    constructor(from, to) {
        this.from = from;
        this.to = to;
    }

    draw(ctx, celulasMap) {
        const c1 = celulasMap.get(this.from);
        const c2 = celulasMap.get(this.to);
        if (!c1 || !c2) return;
        ctx.beginPath();
        ctx.moveTo(c1.x, c1.y);
        ctx.lineTo(c2.x, c2.y);
        ctx.strokeStyle = "#999";
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}

class SimuladorCelular {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext("2d");
        this.celulas = [];
        this.relaciones = [];
        this.selectedCell = null;

        // Zoom & Pan
        this.scale = 1;
        this.offsetX = 0;
        this.offsetY = 0;
        this.dragging = false;
        this.dragStart = { x: 0, y: 0 };

        this._bindEvents();
        this.loadEstado();
    }


    _bindEvents() {
        // ... dentro de _bindEvents
        this.canvas.addEventListener("mousedown", e => {
            const [x, y] = this.getCanvasCoords(e.offsetX, e.offsetY);
            const clicked = this.celulas.find(c => Math.hypot(c.x - x, c.y - y) < 32);
            if (clicked) {
                this.selectedCell = clicked;
                this.isDraggingCell = true;
                this.dragOffset = { dx: x - clicked.x, dy: y - clicked.y };
                this.draw();
                this.updateSidebar();
            } else {
                this.isDraggingCanvas = true;
                this.dragStart = { x: e.offsetX, y: e.offsetY };
            }
        });
        this.canvas.addEventListener("mousemove", e => {
            const [x, y] = this.getCanvasCoords(e.offsetX, e.offsetY);
            if (this.isDraggingCell && this.selectedCell) {
                this.selectedCell.x = x - this.dragOffset.dx;
                this.selectedCell.y = y - this.dragOffset.dy;
                this.draw();
            } else if (this.isDraggingCanvas) {
                this.offsetX += (e.offsetX - this.dragStart.x) / this.scale;
                this.offsetY += (e.offsetY - this.dragStart.y) / this.scale;
                this.dragStart = { x: e.offsetX, y: e.offsetY };
                this.draw();
            }
        });
        this.canvas.addEventListener("mouseup", e => {
            if (this.isDraggingCell && this.selectedCell) {
                // Guarda nueva posición en backend si quieres
                fetch("/mover_celula", {
                    method: "POST",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({ id: this.selectedCell.id, x: this.selectedCell.x, y: this.selectedCell.y })
                });
            }
            this.isDraggingCell = false;
            this.isDraggingCanvas = false;
        });
        this.canvas.addEventListener("mousedown", e => {
            this.dragging = true;
            this.dragStart = { x: e.offsetX, y: e.offsetY };
        });

        this.canvas.addEventListener("mouseup", () => this.dragging = false);

        this.canvas.addEventListener("mousemove", e => {
            if (this.dragging) {
                this.offsetX += (e.offsetX - this.dragStart.x) / this.scale;
                this.offsetY += (e.offsetY - this.dragStart.y) / this.scale;
                this.dragStart = { x: e.offsetX, y: e.offsetY };
                this.draw();
            }
        });

        this.canvas.addEventListener("wheel", e => {
            e.preventDefault();
            const zoom = e.deltaY < 0 ? 1.1 : 0.9;
            this.scale *= zoom;
            this.draw();
        }, { passive: false });

        this.canvas.addEventListener("click", e => {
            const [x, y] = this.getCanvasCoords(e.offsetX, e.offsetY);
            const cel = this.celulas.find(c =>
                Math.hypot(c.x - x, c.y - y) < 32
            );
            this.selectedCell = cel ?? null;
            this.draw();
            this.updateSidebar();
        });

        // Responsive canvas
        window.addEventListener("resize", () => this.resizeCanvas());
        this.resizeCanvas();
    }

    resizeCanvas() {
        this.canvas.width = window.innerWidth * 0.8;
        this.canvas.height = window.innerHeight * 0.7;
        this.draw();
    }

    getCanvasCoords(x, y) {
        return [
            (x - this.offsetX) / this.scale,
            (y - this.offsetY) / this.scale
        ];
    }

    setDatos({ celulas, relaciones }) {
        this.celulas = celulas.map(c => new Celula(c));
        this.celulasMap = new Map(this.celulas.map(c => [c.id, c]));
        this.relaciones = relaciones.map(r => new Relacion(r.from, r.to));
        this.draw();
    }

    draw() {
        const ctx = this.ctx;
        ctx.setTransform(this.scale, 0, 0, this.scale, this.offsetX, this.offsetY);
        ctx.clearRect(-this.offsetX / this.scale, -this.offsetY / this.scale, this.canvas.width / this.scale, this.canvas.height / this.scale);

        // Dibuja relaciones primero
        for (const r of this.relaciones) r.draw(ctx, this.celulasMap);

        // Dibuja células
        for (const c of this.celulas)
            c.draw(ctx, this.selectedCell?.id === c.id);

        ctx.setTransform(1, 0, 0, 1, 0, 0);
    }

    loadEstado() {
        fetch("/estado")
            .then(res => res.json())
            .then(data => {
                // Crea relaciones desde enlaces
                const relaciones = [];
                for (const c of data.celulas) {
                    if (c.enlaces?.length)
                        for (const t of c.enlaces)
                            relaciones.push({ from: c.id, to: t });
                }
                this.setDatos({ celulas: data.celulas, relaciones });
                this.updateStats();
            });
    }

    updateSidebar() {
        const infoDiv = document.getElementById("infoCelula");
        if (!this.selectedCell) {
            infoDiv.innerHTML = "<em>Selecciona una célula para ver detalles</em>";
            return;
        }
        const c = this.selectedCell;
        infoDiv.innerHTML = `
            <h3>${c.id}</h3>
            <b>Tipo:</b> ${c.tipo}<br>
            <b>Energía:</b> ${c.energia_actual} / ${c.energia_maxima}<br>
            <b>Estado:</b> ${c.estado || "-"}<br>
            <b>Nivel Evolución:</b> ${c.nivel_evolucion ?? "-"}<br>
            <b>Organulos:</b> ${c.organulos ? c.organulos.join(", ") : "-"}<br>
            <b>Enlaces:</b> ${c.enlaces ? c.enlaces.join(", ") : "-"}<br>
            <button onclick="impulsarCelula('${c.id}')">Impulsar</button>
        `;
    }

    updateStats() {
        const total = this.celulas.reduce((sum, c) => sum + (c.energia_actual || 0), 0);
        document.getElementById("stats").innerText =
            `⚡ Energía total: ${total.toFixed(2)} | Células: ${this.celulas.length}`;
    }
}

// --- Inicialización ---
const simulador = new SimuladorCelular(document.getElementById("energyCanvas"));

// Exponer funciones globales (para botones HTML)
window.evolucionar = function () {
    fetch("/evolucionar")
        .then(() => simulador.loadEstado());
};

window.exportarJSON = function () {
    const dataStr = "data:text/json;charset=utf-8," +
        encodeURIComponent(JSON.stringify(simulador.celulas, null, 2));
    const dlAnchor = document.createElement("a");
    dlAnchor.setAttribute("href", dataStr);
    dlAnchor.setAttribute("download", "estado_simulador.json");
    dlAnchor.click();
};

window.impulsarCelula = function (id) {
    fetch("/impulsar/" + id).then(() => simulador.loadEstado());
};

// Para randomizar: implementa aquí tu lógica, llamando a una función en el backend
window.randomizarOrganismo = function () {
    fetch("/randomizar", { method: "POST" })
        .then(() => simulador.loadEstado());
};

// Llama a simulador.loadEstado() al cargar, ¡y todo estará enlazado!



// Renderizado básico de tabla de células para frontend
function renderTablaCelulas(celulas) {
    const tbody = document.getElementById('tablaCelulas');
    tbody.innerHTML = "";
    celulas.forEach(cel => {
        let tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${cel.id}</td>
            <td>${cel.tipo}</td>
            <td>${cel.energia_actual}</td>
            <td>
                <button onclick="mostrarDetallesCelula('${cel.id}')">Detalles</button>
                <button onclick="editarCelulaModal('${cel.id}')">Editar</button>
                <button onclick="eliminarCelula('${cel.id}')">Eliminar</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}


// Utilidades para mostrar/hide modal
function showCrudModal(title, entity, data={}, onSubmit) {
  document.getElementById('crudModal').style.display = 'block';
  document.getElementById('crudTitle').innerText = title;
  let form = document.getElementById('crudForm');
  form.innerHTML = ''; // Limpia
  for (let key in data) {
    if (key === "id") continue;
    form.innerHTML += `<label>${key}: <input name="${key}" value="${data[key] ?? ""}"></label><br>`;
  }
  document.getElementById('crudSubmit').onclick = (e) => {
    e.preventDefault();
    let out = {};
    Array.from(form.elements).forEach(inp => { if(inp.name) out[inp.name] = inp.value; });
    onSubmit(out);
    document.getElementById('crudModal').style.display = 'none';
  };
}
document.getElementById('closeCrud').onclick = () => {
  document.getElementById('crudModal').style.display = 'none';
};

// CRUD dinámico (tabla básica) para cada entidad
function mostrarTablaCrud(entidad) {
  fetch(`/api/${entidad}`).then(r=>r.json()).then(datos => {
    let table = `<table><tr>`;
    if (!Array.isArray(datos)) datos = datos[entidad] || [];
    if (!datos.length) { document.getElementById('tablaCrudContainer').innerHTML = "Nada para mostrar"; return; }
    Object.keys(datos[0]).forEach(k => table += `<th>${k}</th>`);
    table += `<th>Acciones</th></tr>`;
    datos.forEach(row => {
      table += `<tr>`;
      Object.values(row).forEach(v => table += `<td>${v}</td>`);
      table += `<td>
        <button onclick="editarEntidad('${entidad}', '${row.id}')">Editar</button>
        <button onclick="eliminarEntidad('${entidad}', '${row.id}')">Borrar</button>
      </td></tr>`;
    });
    table += `</table>
    <button onclick="crearEntidad('${entidad}')">Nueva ${entidad.slice(0, -1)}</button>`;
    document.getElementById('tablaCrudContainer').innerHTML = table;
  });
}

// CRUD helpers
function editarEntidad(entidad, id) {
  fetch(`/api/${entidad}/${id}`).then(r=>r.json()).then(obj => {
    showCrudModal("Editar " + entidad.slice(0,-1), entidad, obj, cambios => {
      fetch(`/api/${entidad}/${id}`, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(cambios)
      }).then(()=>mostrarTablaCrud(entidad));
    });
  });
}
function eliminarEntidad(entidad, id) {
  if (confirm("¿Seguro?")) {
    fetch(`/api/${entidad}/${id}`, {method:"DELETE"}).then(()=>mostrarTablaCrud(entidad));
  }
}
function crearEntidad(entidad) {
  showCrudModal("Nueva " + entidad.slice(0,-1), entidad, {nombre:""}, cambios => {
    fetch(`/api/${entidad}`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(cambios)
    }).then(()=>mostrarTablaCrud(entidad));
  });
}
