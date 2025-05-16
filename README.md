# FigurasGeometricas3D_Practica_5_Python
Figuras 3D en OpenGL: Implementación y manipulación
# Figuras Tridimensionales con OpenGL

Programa que renderiza figuras tridimensionales segun las elija el usuario, ademas de permitirle modificar sus valores de tamaño, posicion, iluminación, textura y rotación.
Las figuras disponibles son: Cubo, Piramide, Esfera, Cilíndro y Superelipsoide.

## Requerimientos

1. Python (descargar desde [python.org](https://www.python.org/downloads/))
- Puedes verificar si tienes Python instalado ejecutando:

```bash
python --version
```

2.pygame & PyOpenGL

- Instala con los siguientes comandos en la terminal:

```bash
pip install pygame PyOpenGL
pip install pygame pygame
```

- Verifica si se instaló correctamente ejecutando:

```bash
pip list
```
3.Asegurarse que ´textura.jpg´y ´menu.jpg´ se encuentren en el mismo folder que se encuentra el .py 

## Uso
1. Corra el programa
2. Seleccione la figura que desea renderizar mediante la tecla correspondiente a la figura, o salga del programa presionando la tecla 6.
```bash
 1 | Cubo
 2 | Piramide
 3 | Esfera
 4 | Cilíndro
 5 | Superelipsoide
 6 | Terminar Programa
```
3. Despues de elegir una figura, se mostrará esta misma y se podra modificar mediante las siguientes teclas.
```bash
 ESC              | Regresar a menu principal
 W                | Aumentar Tamaño
 S                | Disminuir Tamaño
 A                | Mover a la izquierda
 D                | Mover a la derecha
 T                | Alternar visualización de la textura
 I                | Alternar visualización de la iluminacion
 Flecha Arriba    | Girar hacia arriba
 Flecha Abajo     | Girar hacia abajo
 Flecha Derecha   | Girar hacia la derecha
 Flecha Izquierda | Girar girar hacia la izquierda
```


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
