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

## Web Interface

An interactive web-based spirograph generator is available in `docs/index.html`. This is a standalone HTML file that uses JavaScript and the HTML5 Canvas to replicate the functionality of the Python module.

### Architecture

The web interface uses a dual-canvas architecture to manage animations and drawings:

*   **Persistent Layer:** This canvas holds the completed spirograph drawings. Drawings on this layer remain on the screen until the "Clear" button is clicked.
*   **Animation Layer:** This canvas is used to render the animations. It is cleared on each frame to create the illusion of motion. When an animation is complete, the final drawing is transferred to the persistent layer.

This separation of concerns allows for smooth animations while preserving the history of previous drawings.

### Drawing Mechanism

The `drawSpiro` function is the core of the drawing mechanism. When the "Draw" button is clicked, this function is called, which initiates an animation loop using `requestAnimationFrame`.

The animation loop calculates the position of the spirograph at each frame and draws it to the animation layer. Helper elements, such as the inner and outer circles, are also drawn to this layer to provide a visual guide.

Once the animation is complete, the final spirograph is drawn to the persistent layer, and the animation layer is cleared.

### Abstractions

The following JavaScript functions are used to abstract the drawing logic:

*   **`spirocoord`:** Calculates the x and y coordinates of the spirograph at a given angle.
*   **`drawCurve`:** Draws the spirograph curve to a given canvas context.
*   **`drawHelpers`:** Draws the helper elements (inner and outer circles, etc.) to a given canvas context.