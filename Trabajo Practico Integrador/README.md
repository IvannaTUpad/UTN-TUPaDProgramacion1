# Gestión de Datos de Países en Python

## Descripción del programa


Esta aplicación de consola en Python permite gestionar información sobre países, facilitando la organización y consulta de datos como nombre, población, superficie y continente. Utiliza listas, diccionarios y funciones para filtrar, buscar, ordenar y mostrar estadísticas basadas en un archivo CSV de datos. El sistema valida entradas, maneja errores y todas las operaciones se realizan mediante un menú interactivo, integrando conceptos fundamentales de Programación 1.

---

## Instrucciones de uso

**Requisitos:**
- Python 3.x instalado.
- Archivo `paises.csv` (suministrado en este repositorio) ubicado en la misma carpeta que el programa.

**Ejecución:**
1. Abrir una terminal o línea de comandos.
2. Ejecutar el archivo principal:
   ```bash
   python tp_Integrador.py
   ```
3. Usar el menú interactivo para realizar las siguientes operaciones:
   - Agregar países
   - Actualizar datos existentes
   - Buscar por nombre (exacto o parcial)
   - Filtrar por continente, población o superficie
   - Ordenar países por nombre, población o superficie (ascendente/descendente)
   - Visualizar estadísticas (mayor/menor población, promedios, cantidad por continente)

**Notas:**
- El sistema muestra mensajes claros ante errores de entrada o formato de datos.
- Los cambios (agregado/actualización) se guardan automáticamente en el CSV.

---

## Ejemplos de entradas y salidas

### Ejemplo 1: Agregar país

**Entrada por menú:**
```
1. Agregar país
Ingrese el nombre del país (o 'salir' para cancelar): Portugal
Ingrese la población (o 'salir' para cancelar): 10300000
Ingrese la superficie en km² (o 'salir' para cancelar): 92200
Ingrese el continente (no puede estar vacío ni ser un número): Europa
```

**Salida:**
```
País 'Portugal' agregado correctamente.
``

---

### Ejemplo 2: Buscar país por nombre (parcial)

**Entrada por menú:**
```
3. Buscar país por nombre
Ingrese el nombre o parte del nombre del país (o 'salir' para cancelar): chi
```

**Salida:**
```
Se encontraron 1 coincidencia(s):
- Chile | Población: 19000000 | Superficie: 756000 km² | Continente: América
```

---

### Ejemplo 3: Filtrar países por continente

**Entrada por menú:**
```
4. Filtrar países por continente
Ingrese el nombre del continente (o 'salir' para cancelar): Asia
```

**Salida:**
```
Se encontraron 6 país(es) en Asia:
- China | Población: 1410000000 | Superficie: 9600000 km²
- India | Población: 1400000000 | Superficie: 3287000 km²
- Japón | Población: 125000000 | Superficie: 377000 km²
- Corea del Sur | Población: 521000000 | Superficie: 100000 km²
- Qatar | Población: 1000 | Superficie: 1000 km²
- Corea del Norte | Población: 1000 | Superficie: 1000 km²
```

---

### Ejemplo 4: Estadísticas

**Entrada por menú:**
```
10. Mostrar estadísticas
```

**Salida ejemplo:**
```
País con mayor población: China (1,410,000,000)
País con menor población: Qatar (1,000)
Promedio de población: [valor calculado]
Promedio de superficie: [valor calculado] km²
Cantidad de países por continente:
- América: 14
- Europa: 10
- Asia: 6
- Oceanía: 1
```

---

## Participación de los integrantes

- **Lola Tarica:** Responsable principal de la presentación y formato de la documentación, asegurando que todo el README y el informe teórico cumplan con los estándares requeridos. Además, realizó revisiones cruzadas sobre las secciones desarrolladas por Ivanna y contribuyó de forma equitativa al marco teórico.
- **Ivanna Avila:** Responsable principal de la programación y funcionalidades, así como la revisión y validación cruzada del código y documentación realizada por Lola. La elaboración del marco teórico se dividió equitativamente entre ambas.

Ambas integrantes participaron de manera activa y colaborativa, revisando y mejorando mutuamente sus aportes, para asegurar la calidad y coherencia del trabajo final.

---

## Dataset base

El archivo `paises.csv` se incluye en este repositorio como dataset inicial. Ejemplo de las primeras filas:

```
nombre,poblacion,superficie,continente
Argentina,47000000,2780000,América
Brasil,215000000,8516000,América
Chile,19000000,756000,América
...
```

El sistema modifica y actualiza este archivo automáticamente según las operaciones realizadas.

---

## Licencia

Este proyecto es realizado como Trabajo Práctico Integrador para Programación 1 (Tecnicatura Universitaria en Programación a Distancia), con fines educativos.

#Video de presentación grupal

https://youtu.be/nqtmzqDv7Fs
