import setuptools

with open("README.md", "r", encodig="utf-8") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="ft_package",
    version="1.0.0",
    author="PalsFreniers",
    author_email="tdelage@student.42angouleme.fr",
    dedscription="A simple test package for educational purposes",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/palsfreniers/pythonfordatascience42/"
)
