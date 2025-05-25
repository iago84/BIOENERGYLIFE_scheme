<p align="center">
  <img src="https://tu-url-o-ruta/logo-naira-studio-ltd.png" alt="Naira Studio LTD" width="180"/>
</p>

<h1 align="center">⚡️ Simulador Orgánico de Redes Energéticas</h1>
<p align="center">
  <em>Desarrollado por <b>Naira Studio LTD</b></em>
</p>

---

### ¿Qué es este proyecto?

Este simulador permite modelar, visualizar y analizar redes energéticas como si fueran organismos vivos:

- **Células energéticas** (nodos de consumo/producción)
- **Orgánulos** (componentes internos funcionales)
- **Generadores** (fuentes físicas con potencia realista, eficiencia y lógica de arranque)
- **Racks** y **órganos** (agregaciones y jerarquías energéticas)
- **Tejidos y conexiones** que representan la topología

Todo gestionado desde una **API RESTful en Python (Flask)** y visualizado en tiempo real con frontend interactivo.

---

### Características principales

- **Backend Python + Flask**
    - API REST para toda la lógica: células, generadores, racks, conexiones y más
    - Validación física realista (pérdidas, eficiencia, sobrecarga, balanceo automático)
    - Log de eventos, historial y control total del ecosistema energético

- **Frontend interactivo (HTML/JS/CSS)**
    - Visualización en canvas de toda la red
    - Zoom, pan, menús contextuales y visualización de flujos energéticos

- **Modelo inspirado en biología y energía**
    - Entidades modulares y ampliables (células, órganos, racks, etc.)
    - Lógica evolutiva, validaciones y simulación de crecimiento “natural”

---

### ¿Para qué sirve?

- Prototipar, analizar y enseñar **redes energéticas distribuidas** (microgrids, smart grids, sistemas “orgánicos”, etc.)
- Simulación avanzada para **docencia, divulgación y formación** en energía, electrónica y biología artificial
- Probar lógicas de balanceo, validación, escalabilidad y sostenibilidad

---

### ¿Por qué usarlo?

- **Realismo:** bloquea expansiones inviables, simula pérdidas y eficiencia reales
- **Flexibilidad:** diseña desde una microred simple hasta un “organismo” energético complejo
- **Interactividad:** experimenta en tiempo real con la red y visualiza el resultado
- **Documentado y preparado para ampliar**

---

### 🚀 Cómo empezar

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
pip install -r requirements.txt
python server.py
