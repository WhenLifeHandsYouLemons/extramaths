# extramaths 0.1.0

A Python package that simplifies equations. Right now it only does quadratics and 2D shape areas, soon I'll add more.

Go to https://pypi.org/project/extramaths/ to install the package.


## Help Page

This help page shows examples of how all the functions work, for a more in-depth help page, please refer to https://github.com/WhenLifeHandsYouLemons/extramaths/wiki/Help.

### For Quadratics

~~~
from extramaths import quadsolver
~~~

~~~
value1, value2 = quadsolver.quadraticsolver(a, b, c)

print(value1)
print(value2)
~~~

### For Areas of 2D Shapes

~~~
from extramaths import areasolver
~~~

#### Square

~~~
area_of_square = areasolver.area_square(length)

print(area_of_square)
~~~

#### Rectangle

~~~
area_of_rectangle = areasolver.area_rect(height, width)

print(area_of_rectangle)
~~~

#### Right-Angled Triangle

~~~
area_of_right_angled_triangle = areasolver.area_right_angle_tri(base, height)

print(area_of_right_angled_triangle)
~~~

#### Non Right-Angled Triangle

~~~
area_of_non_right_angled_triangle = areasolver.area_non_right_angle_tri(a, b, C)

print(area_of_non_right_angled_triangle)
~~~

#### Rhombus

~~~
area_of_rhombus = areasolver.area_rhombus(D, d)

print(area_of_rhombus)
~~~

#### Trapezoid

~~~
area_of_trapezoid = areasolver.area_trapezoid(a, b, height)

print(area_of_trapezoid)
~~~

#### Circle

~~~
area_of_circle = areasolver.area_circle(r)

print(area_of_circle)
~~~
