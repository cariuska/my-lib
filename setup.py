from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lib-teste",
    version="0.0.3",
    author="Thiago Cariuska",
    python_requires='>=3.8.0',
    long_description=long_description,
    install_requires=[
        "requests"
    ],
    packages=['my_lib_teste']
)
