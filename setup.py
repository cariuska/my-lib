from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lib-teste",
    version="0.0.1",
    author="Thiago Cariuska",
    python_requires='>=3.8.0',
    install_requires=[
        "requests"
    ],
    packages=['my_lib_teste']
)
