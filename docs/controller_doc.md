# Documentación de `controller.py`

---

## Funciones principales

- **crear_celula(data)**: Crear celula.
- **editar_celula(id, cambios)**: Editar celula.
- **eliminar_celula(id)**: Eliminar celula.
- **crear_organulo(data)**: Crear organulo.
- **editar_organulo(id, cambios)**: Editar organulo.
- **eliminar_organulo(id)**: Eliminar organulo.
- **obtener_conexiones()**: Obtener conexiones.
- **crear_conexion(data)**: Crear conexion.
- **eliminar_conexion(cid)**: Eliminar conexion.
- **cargar_inicial()**: Cargar inicial.
- **evolucionar(ciclos)**: Evolucionar.
- **impulsar_celula(celula_id)**: Impulsar celula.
- **obtener_estado_red()**: Obtener estado red.
- **instanciar_celula_tipo(tipo, posicion, madre, sufijo_id, estado)**: Instanciar celula tipo.
- **conectar_celulas(origen_id, destino_id)**: Conectar celulas.
- **obtener_historial_celula(celula_id)**: Obtener historial celula.
- **listar_celulas_por_tipo(tipo)**: Listar celulas por tipo.
- **obtener_energia_total_red()**: Obtener energia total red.
- **reiniciar_red()**: Reiniciar red.
- **clonar_celula(celula_id, nueva_posicion)**: Clonar celula.
- **estado_celula(celula_id)**: Estado celula.
- **info_para_canvas()**: Info para canvas.
- **desconectar_celulas(origen, destino)**: Desconectar celulas.
- **randomizar_organismo_param(params)**: Randomizar organismo param.
- **editar_celula(id, cambios)**: Editar celula.
- **eliminar_celula(id)**: Eliminar celula.
- **crear_generador(data)**: Crear generador.
- **editar_generador(id, cambios)**: Editar generador.
- **eliminar_generador(id)**: Eliminar generador.
- **editar_conexion(origen_id, destino_id, nueva_info)**: Editar conexion.
- **puede_crear_celula(nueva_celula, generadores, celulas_existentes)**: Puede crear celula.
- **crear_celula_validada(data)**: Crear celula validada.
- **puede_expandir_rack(nuevo_rack, racks, generadores, celulas)**: Puede expandir rack.
- **puede_arrancar_celula(celula)**: Puede arrancar celula.