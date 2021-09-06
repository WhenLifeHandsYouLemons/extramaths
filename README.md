# How To Create & Upload A Package

## Installation

~~~bash
python -m pip install --user --upgrade setuptools wheel
~~~

~~~bash
python -m pip install --user --upgrade twine
~~~

## Upload

~~~bash
cd [insert full path to where the setup.py file is located]
~~~

~~~bash
python setup.py sdist bdist_wheel
~~~

This previous step should have created a dist folder.

~~~bash
python -m twine upload dist/*
~~~

Type in your PyPi username and password at this point.

Done!
