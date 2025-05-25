// === app.js FULL STACK MODERNO ===

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

        // Texto identificador
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
        this.celulaAEnlazar = null;

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
        this.canvas.addEventListener("mousedown", e => {
            const [x, y] = this.getCanvasCoords(e.offsetX, e.offsetY);
            const clicked = this.celulas.find(c => Math.hypot(c.x - x, c.y - y) < 32);
            if (clicked) {
                this.selectedCell = clicked;
                this.isDraggingCell = true;
                this.dragOffset = { dx: x - clicked.x, dy: y - clicked.y };
                this.updateSidebar();
                this.draw();
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
                // Actualiza posición en backend
                fetch("/mover_celula", {
                    method: "POST",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({ id: this.selectedCell.id, x: this.selectedCell.x, y: this.selectedCell.y })
                });
            }
            this.isDraggingCell = false;
            this.isDraggingCanvas = false;
        });

        // Zoom
        this.canvas.addEventListener("wheel", e => {
            e.preventDefault();
            const zoom = e.deltaY < 0 ? 1.1 : 0.9;
            this.scale *= zoom;
            this.draw();
        }, { passive: false });

        // Selección para enlazado manual
        this.canvas.addEventListener("dblclick", e => {
            const [x, y] = this.getCanvasCoords(e.offsetX, e.offsetY);
            const cel = this.celulas.find(c => Math.hypot(c.x - x, c.y - y) < 32);
            if (!cel) return;
            if (this.celulaAEnlazar) {
                if (this.celulaAEnlazar.id !== cel.id) {
                    conectarCelulas(this.celulaAEnlazar.id, cel.id);
                }
                this.celulaAEnlazar = null;
                this.draw();
            } else {
                this.celulaAEnlazar = cel;
                this.draw();
            }
        });

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
        for (const c of this.celulas) {
            let sel = this.selectedCell?.id === c.id;
            c.draw(ctx, sel);
            // Marca visual de enlazado
            if (this.celulaAEnlazar?.id === c.id) {
                ctx.beginPath();
                ctx.arc(c.x, c.y, 38, 0, 2 * Math.PI);
                ctx.strokeStyle = "#ff0";
                ctx.lineWidth = 3;
                ctx.stroke();
            }
        }
        ctx.setTransform(1, 0, 0, 1, 0, 0);
    }

    loadEstado() {
        fetch("/estado")
            .then(res => res.json())
            .then(data => {
                // Relaciona enlaces
                const relaciones = [];
                for (const c of data.celulas) {
                    if (c.enlaces?.length)
                        for (const t of c.enlaces)
                            relaciones.push({ from: c.id, to: t });
                }
                this.setDatos({ celulas: data.celulas, relaciones });
                this.updateStats();
                this.updateSidebar();
            });
    }

    updateSidebar() {
        const infoDiv = document.getElementById("celulaDetalles");
        if (!this.selectedCell) {
            infoDiv.innerHTML = "<em>Selecciona una célula para ver detalles</em>";
            document.getElementById("enlazarBtn").style.display = "none";
            document.getElementById("editarBtn").style.display = "none";
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
        `;
        document.getElementById("enlazarBtn").style.display = "inline-block";
        document.getElementById("editarBtn").style.display = "inline-block";
    }

    updateStats() {
        const total = this.celulas.reduce((sum, c) => sum + (c.energia_actual || 0), 0);
        document.getElementById("stats").innerText =
            `⚡ Energía total: ${total.toFixed(2)} | Células: ${this.celulas.length}`;
    }
}

const simulador = new SimuladorCelular(document.getElementById("canvas"));

// Funciones globales

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

// Conexión manual
window.enlazarCelula = function () {
    if (simulador.selectedCell) {
        simulador.celulaAEnlazar = simulador.selectedCell;
    }
};

function conectarCelulas(origen, destino) {
    fetch("/api/conectar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ origen, destino })
    }).then(() => simulador.loadEstado());
}

// Edición modal
window.editarCelula = function () {
    if (!simulador.selectedCell) return;
    mostrarCrudCelula(simulador.selectedCell, datos => {
        fetch(`/api/celula/${simulador.selectedCell.id}`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos)
        }).then(() => simulador.loadEstado());
    });
};

window.crearCelulaManual = function () {
    mostrarCrudCelula({}, datos => {
        fetch(`/api/celula`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos)
        }).then(() => simulador.loadEstado());
    });
};

function mostrarCrudCelula(data, onSave) {
    const modal = document.getElementById("crudModal");
    modal.style.display = "block";
    document.getElementById("crudTitle").innerText = data.id ? "Editar célula" : "Nueva célula";
    let form = document.getElementById("crudForm");
    form.innerHTML = "";
    // Edita todos los campos relevantes de la célula
    let campos = ["tipo", "energia_actual", "energia_maxima", "estado", "nivel_evolucion"];
    campos.forEach(k => {
        form.innerHTML += `<label>${k}: <input name="${k}" value="${data[k] ?? ""}"></label><br>`;
    });
    form.onsubmit = e => {
        e.preventDefault();
        let out = {};
        for (let inp of form.elements) if (inp.name) out[inp.name] = inp.value;
        modal.style.display = "none";
        onSave(out);
    };
}
document.getElementById('closeCrud').onclick = () =>
    document.getElementById('crudModal').style.display = 'none';

// Random
window.randomizarOrganismo = function () {
    fetch("/randomizar", { method: "POST" })
        .then(() => simulador.loadEstado());
};
let menuCellId = null;

canvas.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    // Detecta célula bajo mouse
    const celula = getCelulaFromCoords(e.offsetX, e.offsetY);
    if (celula) {
        menuCellId = celula.id;
        const menu = document.getElementById("context-menu");
        menu.style.display = 'block';
        menu.style.left = e.pageX + "px";
        menu.style.top = e.pageY + "px";
    }
});

document.addEventListener('click', () => {
    document.getElementById("context-menu").style.display = 'none';
});

document.getElementById("context-menu").addEventListener('click', function(e) {
    if (e.target.tagName === "LI") {
        const action = e.target.getAttribute('data-action');
        handleContextMenuAction(action, menuCellId);
        document.getElementById("context-menu").style.display = 'none';
    }
});


function handleContextMenuAction(action, cellId) {
    if (!cellId) return;
    switch (action) {
        case "arrancar": arrancarCelula(cellId); break;
        case "evolucionar": evolucionarCelula(cellId); break;
        case "add-organulo": abrirModalAddOrganulo(cellId); break;
        case "eliminar": eliminarCelula(cellId); break;
        // ...lo que necesites
    }
}
let celulaOrigen = null, enlazando = false;
document.getElementById("btn-enlazar").onclick = () => {
    enlazando = true;
    alert("Selecciona primero la célula origen y después la destino en el canvas.");
};

canvas.addEventListener("click", function(e) {
    if (!enlazando) return;
    const celula = getCelulaFromCoords(e.offsetX, e.offsetY);
    if (celula && !celulaOrigen) {
        celulaOrigen = celula.id;
        // Resalta célula origen visualmente
        resaltarCelula(celulaOrigen);
        return;
    }
    if (celula && celulaOrigen) {
        // Crear conexión
        crearConexion(celulaOrigen, celula.id);
        enlazando = false;
        celulaOrigen = null;
        limpiarResaltado();
    }
});
let celulaSeleccionada = null;
function seleccionarCelula(id) {
    celulaSeleccionada = id;
    document.getElementById("btn-add-organulo").disabled = !id;
}

document.getElementById("btn-add-organulo").onclick = function() {
    if (!celulaSeleccionada) return;
    abrirModalAddOrganulo(celulaSeleccionada);
};
function cargarLogs() {
    fetch("/api/logs?limit=10")
      .then(res => res.json())
      .then(data => {
          const logs = data.map(log => `<div><span style="color:#8aff8a;">${log.tipo}:</span> ${log.mensaje}</div>`);
          document.getElementById("logs-panel").innerHTML = logs.join('');
      });
}
setInterval(cargarLogs, 3000);


let zoom = 1, panX = 0, panY = 0;
let isDragging = false, dragStartX = 0, dragStartY = 0, lastPanX = 0, lastPanY = 0;
canvas.addEventListener('wheel', function(e) {
    e.preventDefault();
    // Zoom centrado en el mouse (opcional, muy pro)
    const rect = canvas.getBoundingClientRect();
    const mx = (e.clientX - rect.left - panX) / zoom;
    const my = (e.clientY - rect.top - panY) / zoom;
    const oldZoom = zoom;

    zoom += e.deltaY < 0 ? 0.1 : -0.1;
    zoom = Math.max(0.2, Math.min(3, zoom)); // Puedes ajustar los límites

    // Para que el zoom sea relativo al punto bajo el ratón:
    panX -= (mx * (zoom - oldZoom));
    panY -= (my * (zoom - oldZoom));

    drawCanvas();
}, { passive: false });


canvas.addEventListener('mousedown', function(e) {
    isDragging = true;
    dragStartX = e.clientX;
    dragStartY = e.clientY;
    lastPanX = panX;
    lastPanY = panY;
});

canvas.addEventListener('mousemove', function(e) {
    if (isDragging) {
        panX = lastPanX + (e.clientX - dragStartX);
        panY = lastPanY + (e.clientY - dragStartY);
        drawCanvas();
    }
});

canvas.addEventListener('mouseup', function(e) {
    isDragging = false;
});
canvas.addEventListener('mouseleave', function(e) {
    isDragging = false;
});

function resetView() {
    zoom = 1; panX = 0; panY = 0; drawCanvas();
}


// Arrays de ejemplo para la demo:
const celulas = [
    { id: "C1", x: 150, y: 180, tipo: "G", color: "#57e", radio: 28 },
    { id: "C2", x: 340, y: 300, tipo: "A", color: "#3c8", radio: 30 }
];

const conexiones = [
    { origen: "C1", destino: "C2", tipo: "energética" }
];

const organulos = [
    { id: "O1", celula: "C1", dx: -15, dy: 15, color: "#f93", radio: 8 },
    { id: "O2", celula: "C2", dx: 20, dy: -15, color: "#fc3", radio: 10 }
];

function drawCanvas() {
    ctx.save();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.setTransform(zoom, 0, 0, zoom, panX, panY);

    drawAllConexiones();
    drawAllCelulas();
    drawOrganulos();

    ctx.restore();
}


function drawAllConexiones() {
    ctx.strokeStyle = "#999";
    ctx.lineWidth = 3;
    conexiones.forEach(conn => {
        const c1 = celulas.find(c => c.id === conn.origen);
        const c2 = celulas.find(c => c.id === conn.destino);
        if (c1 && c2) {
            ctx.beginPath();
            ctx.moveTo(c1.x, c1.y);
            ctx.lineTo(c2.x, c2.y);
            ctx.stroke();
        }
    });
}


function drawAllCelulas() {
    celulas.forEach(cel => {
        // Dibuja círculo principal
        ctx.beginPath();
        ctx.arc(cel.x, cel.y, cel.radio, 0, 2 * Math.PI);
        ctx.fillStyle = cel.color;
        ctx.shadowColor = "#0008";
        ctx.shadowBlur = 6;
        ctx.fill();
        ctx.shadowBlur = 0;

        // Dibuja borde y texto (ID)
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#222";
        ctx.stroke();

        ctx.fillStyle = "#fff";
        ctx.font = "bold 15px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(cel.id, cel.x, cel.y + 5);
    });
}


function drawOrganulos() {
    organulos.forEach(org => {
        const cel = celulas.find(c => c.id === org.celula);
        if (cel) {
            ctx.beginPath();
            ctx.arc(cel.x + org.dx, cel.y + org.dy, org.radio, 0, 2 * Math.PI);
            ctx.fillStyle = org.color;
            ctx.fill();
            ctx.lineWidth = 1.5;
            ctx.strokeStyle = "#444";
            ctx.stroke();
        }
    });
}


function generarCelulasRandom() {
    // Recoge los parámetros del formulario
    const tipos = Array.from(document.getElementById("randomTipos").selectedOptions).map(opt => opt.value);
    const cantidad = parseInt(document.getElementById("randomCantidad").value) || 1;
    const energiaMin = parseFloat(document.getElementById("randomEnergiaMin").value) || 0.5;
    const energiaMax = parseFloat(document.getElementById("randomEnergiaMax").value) || 5;
    const areaAncho = parseInt(document.getElementById("randomAreaAncho").value) || 800;
    const areaAlto = parseInt(document.getElementById("randomAreaAlto").value) || 600;

    if (tipos.length === 0) {
        alert("Selecciona al menos un tipo de célula");
        return;
    }

    for (let i = 0; i < cantidad; i++) {
        const tipo = tipos[Math.floor(Math.random() * tipos.length)];
        const x = Math.floor(Math.random() * (areaAncho - 80)) + 40;
        const y = Math.floor(Math.random() * (areaAlto - 80)) + 40;
        const energia = +(Math.random() * (energiaMax - energiaMin) + energiaMin).toFixed(2);

        // Aquí integra con tu función real de creación:
        // Por ejemplo:
        // instanciarCelulaDesdePlantilla(tipo, {x, y}, energia, ...);
        // Aquí solo añade a tu array de demo:
        celulas.push({
            id: "C" + (celulas.length + 1),
            x, y,
            tipo,
            color: "#"+Math.floor(Math.random()*16777215).toString(16),
            radio: 25,
            energia_actual: energia
        });
    }

    drawCanvas();
    toggleParametros();
}
function toggleParametros() {
    const panel = document.getElementById("parametrosRandom");
    panel.style.display = (panel.style.display === "none" ? "block" : "none");
}


// --- Actualización automática inicial ---
window.onload = () => simulador.loadEstado();
