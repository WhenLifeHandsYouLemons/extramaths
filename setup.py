import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extramaths",
    version="0.1.0",
    author="Sooraj Sannabhadti",
    author_email="developer.soorajs@gmail.com",
    description="A Python package that simplifies equations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WhenLifeHandsYouLemons/extramaths-python-package",
    project_urls={
        "Bug Tracker": "https://github.com/WhenLifeHandsYouLemons/extramaths-python-package/issues",
    },
    keywords='equations math beginner',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3",
)