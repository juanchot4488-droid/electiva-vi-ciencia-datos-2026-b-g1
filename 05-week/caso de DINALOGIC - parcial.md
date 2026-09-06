# Desarrollo de Actividad: Conceptos Basicos de Analitica
**Presentado por:** Juan Diego Ramirez Reyes
**Area de Formacion:** Mantenimiento Electromecanico Industrial

## Caso de Estudio Seleccionado
Para el desarrollo de esta actividad, he seleccionado como caso de estudio mi propia empresa: **DINA SOLUTIONS SERVICES S.A.S.**, enfocada en la prestacion de servicios de instrumentacion industrial, *sandblasting*, y mantenimiento de equipos electromecanicos para el sector de hidrocarburos.

### 1. Identificacion y Clasificacion de Datos
Durante la ejecucion de nuestros proyectos en campo y la gestion administrativa, interactuamos con multiples fuentes de informacion. A continuacion, presento 4 ejemplos claros:

1. **Planillas de mantenimiento y facturacion de clientes:**
   * **Clasificacion:** Datos Estructurados.
   * *Justificacion:* Toda esta informacion reposa en tablas (como Excel o bases de datos relacionales) organizadas estrictamente por columnas (Fecha, NIT del cliente, Valor, Tipo de Servicio).

2. **Registros de telemetria (temperatura y vibracion) exportados de los PLC de las maquinas:**
   * **Clasificacion:** Datos Semiestructurados.
   * *Justificacion:* Los datos suelen extraerse en formatos como JSON o XML. Contienen etiquetas que organizan la informacion de las variables, pero no siguen el formato rigido de una tabla tradicional.

3. **Reportes de novedades y bitacoras de campo redactadas por los tecnicos:**
   * **Clasificacion:** Datos No Estructurados.
   * *Justificacion:* Es texto completamente libre. Cada operario describe las fallas o el estado de los compresores de tornillo y bombas de engranaje usando su propio vocabulario, sin un formato fijo.

4. **Planos, esquemas electricos y manuales de fabricantes en formato PDF:**
   * **Clasificacion:** Datos No Estructurados.
   * *Justificacion:* Son documentos compuestos por imagenes, diagramas y bloques de texto que carecen de una base de datos interna que organice su contenido.

---

### 2. Preguntas de Analitica

Aplicando el analisis a nuestras operaciones diarias de mantenimiento, planteo las siguientes preguntas:

* **Analitica Descriptiva (Evaluacion del pasado):**
  ¿Cual fue el porcentaje de paradas imprevistas por fallas en las bombas de engranajes durante los mantenimientos ejecutados en el ultimo trimestre?

* **Analitica Predictiva (Proyeccion a futuro):**
  Basandonos en el historial de horas de uso y el aumento gradual de las vibraciones, ¿cual es la probabilidad de que un motor trifasico especifico sufra una falla critica en los proximos 30 dias si no se adelanta su mantenimiento preventivo?

---

### 3. Diagrama Sencillo del Flujo de Datos

Para que las lecturas de los sensores lleguen a ser utiles en la toma de decisiones, el proceso sigue esta cadena:

**Fuente** *(Sensores de instrumentacion instalados en los equipos)* 
**➔Almacenamiento** *(Base de datos historica en un servidor local o en la nube)* 
**➔ Analisis** *(Procesamiento de los registros historicos mediante software estadistico)* 
**➔ Visualizacion** *(Dashboard de mantenimiento con indicadores clave de rendimiento)*

---

### 4. Descriptive Analytics vs. Predictive Analytics

To clarify the difference between these two approaches in our daily operations:

1. **Descriptive analytics** focuses on summarizing historical equipment data to help us understand what exactly happened during past maintenance routines.
2. **Predictive analytics** uses statistical models and past machine behaviors to forecast what mechanical failures are most likely to happen in the future.