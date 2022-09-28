from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lib",
    version="0.0.1",
    python_requires='>=3.6.0',
    install_requires=[
        "requests"
    ],
    packages=['my_lib']
)
