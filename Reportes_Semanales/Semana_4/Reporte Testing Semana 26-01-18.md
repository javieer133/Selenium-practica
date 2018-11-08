**Reporte QA QServus**

Viernes, 26 de Enero de 2018

**Introducción:**

En el siguiente documento se resumen los resultados de las actividades realizadas por el equipo de QA.

El equipo se ha dedicado a la revisión de tickets en qservus, además de reportar cualquier error que se haya podido encontrar en la plataforma, los cuales son registrados en un Documento de Errores, para luego ser revisados, validados y, los más relevantes entre ellos,  reportados por Francisco Cuadra.

Adicionalmente, un documento de Historias de Usuario (NOTE:  http://www.methodsandtools.com/archive/archive.php?id=72p2) se encuentra actualmente en progreso, el cual será utilizado como guía para todas las futuras pruebas.

El equipo está usando la herramienta Katalon (NOTE:  https://www.katalon.com/) para grabar y automatizar pruebas según el ya mencionado documento de Historias de Usuario.

A continuación se presentan cinco métricas derivadas del trabajo realizado desde el inicio del año 2018 hasta la fecha. Las métricas presentadas son:

1. **Incidencias Encontradas por Componente**: Refleja el número de incidencias halladas según el componente de la aplicación que afecta, como son pautas, sensores, campañas, etc. Este reporte incluye las incidencias escritas en el adjunto Reporte de Errores.

2. **Incidencias Encontradas según Actor:** Refleja la cantidad de incidencias encontradas en Qservus según el actor del sistema que las encontró, tales como equipo de QA, Desarrolladores, Equipo Comercial, Clientes. Este reporte incluye las incidencias escritas en el adjunto Reporte de Errores.

3. **Incidencias Reportadas por Tipo:** Refleja el tipo de incidencias que se reporta (no que se resuelve), tal como Bug, Task y Feature. Este reporte se limita a lo encontrado en Redmine, sin incluír el reporte de errores del equipo de QA.

4. **Tasa de Incidencias Resueltas:** Ilustra el flujo de trabajo realizado, calculado como el número de Incidencias Resueltas dividido por el número total de incidencias. Se cuentan todas las incidencias presentes a la fecha de 2 de Enero y posterior.

5. **Incidencias Resueltas por Tipo:** Número de incidencias resueltas dividido en Task, Bug y Feature.

**Semana****: 22/01/18 - 26/01/18**

1.- **Incidencias Encontradas por Componente**

<table>
  <tr>
    <td>Componentes</td>
    <td>Hasta 19/01/2018</td>
    <td>Hasta 26/01/2018</td>
  </tr>
  <tr>
    <td>Pauta</td>
    <td>7</td>
    <td>16</td>
  </tr>
  <tr>
    <td>Sensor</td>
    <td>1</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Campaña</td>
    <td>18</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Reportes</td>
    <td>13</td>
    <td>16</td>
  </tr>
  <tr>
    <td>Tareas</td>
    <td>4</td>
    <td>8</td>
  </tr>
  <tr>
    <td>API</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Newsfeed</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Indicadores</td>
    <td>4</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Navegador</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Usuario</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>51</td>
    <td>75</td>
  </tr>
</table>


![image alt text](image_0.png)

2.- **Incidencias Encontradas Reportadas según Actor**

<table>
  <tr>
    <td>Nombre de Actor</td>
    <td>Hasta el 19.01.2018</td>
    <td>Hasta el 26.01.2018</td>
  </tr>
  <tr>
    <td>equipo QA</td>
    <td>38</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Devs</td>
    <td>5</td>
    <td>8</td>
  </tr>
  <tr>
    <td>Comercial</td>
    <td>15</td>
    <td>17</td>
  </tr>
  <tr>
    <td>Clientes</td>
    <td>17</td>
    <td>25</td>
  </tr>
  <tr>
    <td>TOTAL</td>
    <td>75</td>
    <td>100</td>
  </tr>
</table>


![image alt text](image_1.png)

3.- **Incidencias Reportadas por Tipo**

<table>
  <tr>
    <td>TIPO</td>
    <td>Hasta el 19.01.2018</td>
    <td>Hasta el 26.01.2018</td>
  </tr>
  <tr>
    <td>Bug</td>
    <td>12</td>
    <td>21</td>
  </tr>
  <tr>
    <td>Feature</td>
    <td>18</td>
    <td>23</td>
  </tr>
  <tr>
    <td>Task</td>
    <td>10</td>
    <td>12</td>
  </tr>
  <tr>
    <td>Total</td>
    <td>40</td>
    <td>56</td>
  </tr>
</table>


![image alt text](image_2.png)

4.- **Tasa de Incidencias Resueltas**



<table>
  <tr>
    <td>Item</td>
    <td>Hasta el 19/01</td>
    <td>Hasta el 26/01</td>
  </tr>
  <tr>
    <td>N° Total Tickets Resueltos</td>
    <td>32</td>
    <td>47</td>
  </tr>
  <tr>
    <td>N° incidencias Totales</td>
    <td>64</td>
    <td>80</td>
  </tr>
  <tr>
    <td>Tasa</td>
    <td>50,00%</td>
    <td>58,75%</td>
  </tr>
</table>


**N° Total de Tickets Resueltos:** Corresponde a la totalidad de ticket que se revisó por el equipo de QA.

**N° Incidencias Totales:** Corresponde a la cantidad total de tickets que han existido en la columna New e In Progress, además de las incidencias cerradas o resueltas desde el 02/01/2018.

5.- **Incidencias Resueltas por Tipo**

<table>
  <tr>
    <td>Item</td>
    <td>Hasta el 19/01</td>
    <td>Hasta el 26/01</td>
  </tr>
  <tr>
    <td>N° Revisiones Totales</td>
    <td>52</td>
    <td>76</td>
  </tr>
  <tr>
    <td>Bugs</td>
    <td>26</td>
    <td>37</td>
  </tr>
  <tr>
    <td>Task</td>
    <td>3</td>
    <td>7</td>
  </tr>
  <tr>
    <td>Feature</td>
    <td>3</td>
    <td>3</td>
  </tr>
</table>


**N° de Revisiones Totales**: Corresponde a la cantidad de revisiones que se realizaron para la totalidad de ticket trabajados por el equipo de QA.

