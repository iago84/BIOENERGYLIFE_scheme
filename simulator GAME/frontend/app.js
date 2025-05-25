const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

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
            dibujarMapa(data.celulas);
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
    celulas.forEach((cel, i) => {
        const x = 100 + (i % 10) * 70;
        const y = 100 + Math.floor(i / 10) * 100;
        ctx.beginPath();
        ctx.arc(x, y, 25, 0, Math.PI * 2);
        ctx.fillStyle = cel.tipo === "G" ? "lime" : "cyan";
        ctx.fill();
        ctx.strokeStyle = "white";
        ctx.stroke();
        ctx.fillStyle = "black";
        ctx.fillText(cel.tipo, x - 5, y + 5);
    });
}

// Auto-cargar estado al inicio
cargarEstado();
cargarLogs();
