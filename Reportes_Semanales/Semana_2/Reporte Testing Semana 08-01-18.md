# Reporte QA QServus

## Viernes, 12 de Enero de 2018

## Introducción:

En el siguiente  documento  se  detallan  las  actividades  realizadas  por  el 
equipo de QA.  
El  equipo  se  ha  dedicado  a  la  revisión  de  tickets  en  qservus,  además  de 
reportar  cualquier  error  que  se  haya  podido  encontrar  en  la  plataforma,  los  cuales 
son  registrados  en  un  documento  para  luego  ser  revisados,  validados  y  reportados 
por Francisco Cuadra. 
Adicionalmente,  un  documento  de  Historias  de  Usuario1  se  encuentra 
actualmente  en  progreso,  el  cual  será  utilizado  como  guía  para  todas  las  futuras 
pruebas. 
Finalmente,  el  equipo  está  usando  la  herramienta  Katalon2  para  grabar  y 
automatizar pruebas según el ya mencionado documento de Historias de Usuario. 

## Semana: 08/01/18 - 12/01/18 
 
### Lunes 8/1/2018: 
- Confección  y  avance  de  historias  de  usuario,  relativo  a  creación  de 
campañas, opciones avanzadas, manejo de sensores 

- Revisión  de  tickets,  relativos  a  Errores  con  Reportes  web  asociados  a  Pautas 
con  sensores  donde  la  información  de  checklist  no  se  ven  de  forma  correcta 
en  el  reporte,  Errores  en  resultados  de  campaña  para  distintas 
matrices,pintados  las  barras  de  las  preguntas  de  tipo  de  escala  de  caras  y  a 
la aparición de campañas eliminadas en indicadores. 

- Reporte  de  errores  tales como: Errores en visualización de matrices de 0 a 10 
y matrices de 1 a 10, mediante reporte PDF. 

- Configurar  la  herramienta  “gdocs2md”  en  el  Drive  de  QServus-Testing  para 
poder  transformar  documentos  de  Google  Docs  a  Markdown.  De  esta 
manera  se  pueden  mantener  los  reportes  semanales  como  documentación 
en el repo de GitLab de QServus-Testing. 

- Hacer los preparativos para automatizar las pruebas de QA.  

### Martes 9/1/2018:  
- Confección  y  avance  de  historias  de  usuario,  relativo  a  Manejo  de  campaña 
(estadisticas de correos, estadisticas de campaña, historial de campañas) 

- Revisión  de  tickets,  relativos  a  Errores  en  resultados  de  campaña  para 
preguntas  de  matriz,  reportes  PDF  desde  campaña,  y  reportes  web  desde 
Pauta.  Errores  en  detalles  de  respuesta  con  preguntas  del  tipo  5 caras. Error 
de  cálculo  de  promedios  en  situaciones  de  respuestas  extremas  (Muy 
Insatisfecho-Muy Satisfecho). 

- Reporte  de  errores  tales  como:  Errores  en  detalle  de  respuestas  de  tipo 
matrices  de  5  caras  donde  las  figuras  de  las  caras  no se mostraban de forma 
correcta  repitiendo  la  imagen  de  satisfaccion  3  veces.  Errores  en  campañas, 
indicadores,  estadisticas  de  campaña,  falta  de  simbolo  de  “%”  y  calculo  de 
promedio. 

### Miércoles 10/1/2018: 
- Revisión  de  Ticket,  relativo  a  un  error  al  re-ordenar  las  alternativas  de  una 
pregunta  de  selección,  el  cambio  no  se  ve  en  la  pauta  de  edición,  y  se 
agrego  el  botón  de  guardar  y  de  cómo  los  cambios  solo  se  guardan  si  se 
hace clic sobre este botón.

- Revisión  de Ticket, respecto al error ocurrido en Indicadores de una campaña 
sin invitaciones, donde la tasa de apertura no era un reflejo de la realidad 

- Reporte  de  error  donde  las  opciones  avanzadas  de  una  campaña  vuelven  a 
estado por defecto luego de finalizar e iniciarla. 

- Continuación  de  preparativos  para  automatizar  pruebas  de  QA,  con 
herramientas como Selenium, python, katalon Automation recorder. 

- Dar  inicio  al  desarrollo  del  Script  en  Python  que  se  especializa  en  correr  las 
pruebas de Selenium en QA. 

### Jueves 11/1/2018: 
- Revisión  de  ticket  relacionado  a  la  creacion  y  edicion  de  preguntas  de  tipo 
Terminos  y condiciones en donde al seleccionar un archivo de tipo incorrecto 
y  apretar  la  opcion  de  Guardar  la  pregunta  el  boton  de  Examinar  se 
desconfigura,  alargando  y  no  se  despliega  el  error  “Por  favor  seleccionar  un 
archivo PDF.” 

- Revision  de  error  sobre  preguntas  de  tipo  Terminos  y  condiciones  donde 
luego  de  rellenar  el  campo  de  enunciado y seleccionar la alternativa de Vista 
previa de los PDF seleccionados, la pregunta se crea de forma automática. 

- Reporte  de  errores  al  borrar  pautas  que  tienen  asociados  sensores  y 
campañas que no están necesariamente finalizadas. 

- Avance  en  historias  de  usuarios,  sección  de  manejo  de  campañas, 
modificaciones en creación de campaña, sección reportes avanzados. 

- Continuación con tareas para la automatización de test 

- Avance en el Script de automatización de QA. 

### Viernes 12/1/2018: 
- Revisión  de  ticket  relacionado  a  la  edición  de  preguntas  de  tipo  Terminos  y 
condiciones,  donde  el  boton  de  “examinar”  y  el  mensaje  de error indicando 
el  formato  (“Por  favor  adjuntar  un  archivo  en  formato  PDF”)  se 
desconfiguraron  bajo  ciertas  condiciones  (Presionar  agregar  sin  enunciado, 
presionar  agregar  sin  archivo,  presionar  agregar  con  archivo  en  formato  no 
deseado, entre otros). 

- Reporte  de  error  sobre  preguntas  de  tipo  Terminos  y  condiciones  donde  al 
realizar  un  pauta  con  más  de  una  pregunta  de  este  tipo  y otra persona edita 
la  pauta  modificando  una  pregunta  de  Términos  y  condiciones,  el  acceso  al 
PDF de la primera pregunta falla. 

- Reporte  de  error  sobre  la  sección  de  indicadores,  donde  no  se  ven  las 
estadisticas de preguntas agregadas post publicación de una pauta.. 

- Avance en el Script de automatización de QA. 

- Se realizan pruebas en el funcionamiento de la API.