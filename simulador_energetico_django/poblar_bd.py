import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simulador_energetico.settings')
django.setup()

from generadores.models import Generador, TipoGenerador, Arranque, Rack
from motores.models import Motor, TipoMotor
from sensores.models import Sensor, Medidor, TipoSensor
from almacenamiento.models import ReservaEnergetica, TipoReserva
from cargas.models import Carga, TipoCarga
from conexiones.models import Conexion, TipoConexion
from celulas.models import Celula
from organulos.models import Organulo
from tejidos.models import Tejido
from simulacion.models import Simulacion, ResultadoSimulacion
from usuarios.models import Usuario

# TIPOS BÁSICOS
TipoGenerador.objects.create(nombre="Trifásico Inducción", descripcion="Uso industrial", tecnologia="induccion_trifasico")
TipoGenerador.objects.create(nombre="Imán Permanente", descripcion="Alta eficiencia", tecnologia="iman_fijo")

TipoMotor.objects.create(nombre="Motor DC", descripcion="Motor corriente continua")
TipoSensor.objects.create(nombre="Voltaje", descripcion="Mide voltaje", tecnologia="electrico")
TipoReserva.objects.create(nombre="Batería de Litio", descripcion="Almacenamiento litio")
TipoCarga.objects.create(nombre="Resistiva", descripcion="Carga básica")
TipoConexion.objects.create(nombre="Energética", descripcion="Flujo de energía")
# GENERADORES
Generador.objects.create(nombre="Generador 5kW Trifásico", tipo="induccion_trifasico", potencia_nominal_kw=5.0, eficiencia=0.9, rpm_min=350, rpm_max=700, voltaje_entrada_v=220, voltaje_salida_v=400, aplicacion="industrial", estado_funcional="operativo", puede_arrancar=True, consumo_arranque_kw=0.5, tension_minima=200, firmware_version="1.2.3")
Generador.objects.create(nombre="Generador Imán Permanente 2kW", tipo="iman_fijo", potencia_nominal_kw=2.0, eficiencia=0.94, rpm_min=200, rpm_max=500, voltaje_entrada_v=0, voltaje_salida_v=220, aplicacion="residencial", estado_funcional="operativo", puede_arrancar=True, consumo_arranque_kw=0.2, tension_minima=0, firmware_version="2.0.0")

# MOTORES
Motor.objects.create(nombre="Motor AC 3HP", tipo="ac", rpm_nominal=1500, corriente_nominal=10.5, potencia_nominal_kw=2.2, consumo_arranque_kw=0.3, ciclos_vida=15000)

# SENSORES Y MEDIDORES
Sensor.objects.create(nombre="Sensor Voltaje Principal", tipo="voltaje", umbral_alerta=230.0, intervalo_medicion=60, estado="ok")
Medidor.objects.create(tipo="kWh", precision=0.01, intervalo_lectura=60, valor_actual=0.0, unidad="kWh")

# ALMACENAMIENTO
ReservaEnergetica.objects.create(nombre="Batería Central", tipo="litio", capacidad_actual_kw=12.0, capacidad_max_kw=20.0, ciclos_vida=2000, estado="disponible")

# CARGAS
Carga.objects.create(tipo_carga="resistiva", potencia_nominal_kw=1.5, consumo_instantaneo_kw=1.2, estado="conectada")

# CELULAS Y ORGANULOS
Celula.objects.create(nombre="Célula Germinadora", tipo="G", energia_actual=5.0, energia_maxima=10.0, nivel_evolucion=1, estado_funcional="activa", consumo_kw=0.2, produccion_kw=1.0)
Organulo.objects.create(nombre="Secuenciador A", tipo="O1", potencia=0.5, estado="operativo", es_secuenciador=True, celula_asociada="Célula Germinadora")

# CONEXIONES
Conexion.objects.create(origen="Célula Germinadora", destino="Generador 5kW Trifásico", tipo_conexion="energética", estado="activa")

# TEJIDOS
Tejido.objects.create(nombre="Tejido Inicial", descripcion="Primera conexión energética", celulas=["Célula Germinadora"], estado="activo")

# SIMULACIÓN
sim = Simulacion.objects.create(estado="en_progreso")
ResultadoSimulacion.objects.create(simulacion=sim, resultados={"status": "ok"}, resumen="Prueba inicial")

print("🟢 Base de datos poblada exitosamente con dispositivos, células y simulaciones.")