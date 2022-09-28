from setuptools import setup

setup(
    name="mylib",
    version="0.0.1",
    python_requires='>=3.6.0',
    install_requires=[
        "requests"
    ],
    extras_require={
    },
    packages=['mylib']
)
