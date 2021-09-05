# extramaths

A custom Python package that simplifies equations. Right now it only does quadratics and 2D shape areas, soon I'll add more.

Go to https://pypi.org/project/extramaths/ to install the package.


## Help Page


### For Quadratics

~~~
from extramaths import quadsolver

value1, value2 = quadsolver.quadraticsolver(a, b, c)

print(value1)
print(value2)
~~~

For the equation: 6x^2 + 11x - 35 = 0

a = 6

b = 11

c = -35

The output would be:
~~~
1.6666666666666667
-3.5
~~~

### For Areas of 2D Shapes

~~~
from extramaths import areasolver
~~~

#### Square

~~~
areasolver.area_square(length)
~~~
If the length of the sides are 2, then

length = 2

The output would be:
~~~
4
~~~
