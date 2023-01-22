# extramaths 0.1.1

A Python package that simplifies equations. Right now it only does quadratics and 2D shape areas, soon I'll add more.

Go to [https://pypi.org/project/extramaths/](https://pypi.org/project/extramaths/ "Download page") to install the package.

[![Upload Python Package](https://github.com/WhenLifeHandsYouLemons/extramaths/actions/workflows/python-publish.yml/badge.svg)](https://github.com/WhenLifeHandsYouLemons/extramaths/actions/workflows/python-publish.yml)

## Help Page

This help page shows examples of how all the functions work, for a more in-depth help page, please refer to [https://github.com/WhenLifeHandsYouLemons/extramaths/wiki/Help](https://github.com/WhenLifeHandsYouLemons/extramaths/wiki/Help "Help page").

### For Quadratics

```python
from extramaths import quadsolver
```

```python
value1, value2 = quadsolver.quadraticsolver(a, b, c)

print(value1)
print(value2)
```

### For Areas of 2D Shapes

```python
from extramaths import areasolver
```

#### Square

```python
area_of_square = areasolver.area_square(length)

print(area_of_square)
```

#### Rectangle

```python
area_of_rectangle = areasolver.area_rect(height, width)

print(area_of_rectangle)
```

#### Right-Angled Triangle

```python
area_of_right_angled_triangle = areasolver.area_right_angle_tri(base, height)

print(area_of_right_angled_triangle)
```

#### Non Right-Angled Triangle

```python
area_of_non_right_angled_triangle = areasolver.area_non_right_angle_tri(a, b, C)

print(area_of_non_right_angled_triangle)
```

#### Rhombus

```python
area_of_rhombus = areasolver.area_rhombus(D, d)

print(area_of_rhombus)
```

#### Trapezoid

```python
area_of_trapezoid = areasolver.area_trapezoid(a, b, height)

print(area_of_trapezoid)
```

#### Circle

```python
area_of_circle = areasolver.area_circle(r)

print(area_of_circle)
```
