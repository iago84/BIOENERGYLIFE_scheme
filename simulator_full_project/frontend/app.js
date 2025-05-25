const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let celulas = [];

canvas.addEventListener("click", function (e) {
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    celulas.forEach(cel => {
        const x = cel.ubicacion.x;
        const y = cel.ubicacion.y;
        const dist = Math.sqrt((mouseX - x) ** 2 + (mouseY - y) ** 2);
        if (dist < 30) {
            alert(`Célula ${cel.id}\nTipo: ${cel.tipo}\nOrganulos:\n${cel.organulos.join(", ")}`);
        }
    });
});

function evolucionar() {
    fetch("http://127.0.0.1:5000/evolucionar")
        .then(res => res.json())
        .then(data => {
            console.log("Evolución:", data);
            cargarEstado();
            cargarLogs();
        });
}

function cargarEstado() {
    fetch("http://127.0.0.1:5000/estado")
        .then(res => res.json())
        .then(data => {
            celulas = data.celulas;
            dibujarMapa(celulas);
        });
}

function cargarLogs() {
    fetch("http://127.0.0.1:5000/log")
        .then(res => res.json())
        .then(data => {
            const logDiv = document.getElementById("log");
            logDiv.innerHTML = data.logs.map(log =>
                `[${log.timestamp}] (${log.tipo}) ${log.descripcion}`
            ).join("\n");
        });
}

function dibujarMapa(celulas) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Dibujar enlaces
    celulas.forEach(cel => {
        if (cel.enlaces) {
            cel.enlaces.forEach(enl => {
                const destino = celulas.find(c => c.id === enl);
                if (destino) {
                    ctx.beginPath();
                    ctx.moveTo(cel.ubicacion.x, cel.ubicacion.y);
                    ctx.lineTo(destino.ubicacion.x, destino.ubicacion.y);
                    ctx.strokeStyle = "gray";
                    ctx.stroke();
                }
            });
        }
    });

    // Dibujar nodos
    celulas.forEach(cel => {
        const x = cel.ubicacion.x;
        const y = cel.ubicacion.y;
        ctx.beginPath();
        ctx.arc(x, y, 25, 0, Math.PI * 2);
        ctx.fillStyle = cel.tipo === "G" ? "lime" : cel.tipo === "A" ? "orange" : "cyan";
        ctx.fill();
        ctx.strokeStyle = "white";
        ctx.stroke();
        ctx.fillStyle = "black";
        ctx.fillText(cel.tipo, x - 5, y + 5);
    });
}

function exportarEstadoJSON() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(celulas, null, 2));
    const dlAnchor = document.createElement('a');
    dlAnchor.setAttribute("href", dataStr);
    dlAnchor.setAttribute("download", "estado_simulador.json");
    dlAnchor.click();
}

document.getElementById("exportarJSON").addEventListener("click", exportarEstadoJSON);

// Auto-cargar estado
cargarEstado();
cargarLogs();
