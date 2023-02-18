import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="saxs_analysis",
    version="0.0.6",
    author="Elizabeth Mathew",
    author_email="Elizabeth.Mathew@hereon.de",
    description="SAXS python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/emathew16/SAXS_analysis",
    packages=setuptools.find_packages(),
    py_modules=['saxspy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
from setuptools import find_packages, setup

setup(
    name='mypkg',
    version='0.1',
    packages=find_packages(),
    py_modules=['bacon']
)
