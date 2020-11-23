from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="jezykiSkryptoweProjekt",
    version="0.0.1",
    author="Tomasz Kumor",
    author_email="romukkemot@gmail.com",
    description="A package to convert your Jupyter Notebook",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/TiPiKej/jezykiSkryptoweProjekt",
    packages=find_packages(),
    install_requires=[
        "openpyxl>=3.0.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
