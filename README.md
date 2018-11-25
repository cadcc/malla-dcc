# malla-dcc

Proyecto en python que genera una visualización de la malla del plan de estudios del DCC. La información de la malla está en el archivo "malla.json", así que si se cambian los contenidos de ese archivo, también se pueden generar mallas de otras carreras.

## Uso
Para usarla, primero se deben instalar los requisitos. En este caso, el único requisito es yattag, que se encarga de generar el archivo html con la malla. Esto se puede hacer con

```
$ pip install yattag
```

Luego, se corre el script renderer.py, y se genera el archivo out.html con la malla
