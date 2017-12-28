# Spirographs in Python

This module allows you to draw spirographs using python's built-in
turtle graphics module.

This is currently very preliminary - let me know if you find it fun and what features might be useful!

## Usage
```python
from turtle import *
from spiro import Spiro

s = Spiro()
s.draw()
s.r1 = 200
s.r2 = 40
s.offset = 15
s.color = 'red'
s.draw()
```