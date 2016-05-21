# G-mends
Set of functions to manipulate and modify the G-code fed to a FDM 3D-printer

#How to use

### Execute it

Open the `__init__.py` file and change the `path = "test.gcode"` with the name of your G-code file. You can then execute:

```python
python __init__.py
```

### Python console

```python
from gcodeParser import *

parser = GcodeParser()
model = parser.parseFile( "test.gcode" )
```

## Stuff you can check

`model.layers` will display all the layers in the G-code as class object.
Use `model.layers[i]` to check layer _i_.

`model.layers[i].segments` will display the number of segments plotted in a layer as segment class object.

`model.layers[i].segments[j].coords` will display the G-code line corresponding to segment number _j_ of layer _i_.

`model.layers[i].segments[j].layerIdx` will display _i_.

`model.layers[i].Z` will directly who you the layer heigth _Z_ in millimiters.







