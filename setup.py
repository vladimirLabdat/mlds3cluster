from setuptools import setup, find_packages

with open("requirements.txt",'r') as f:
	requirements = f.readlines()

with open("README.md", 'r') as f:
	readme = f.read()

setup(
	name = "mlds3das",
	version = "0.1.0",
	author = "Vladimir A. Fajardo",
	author_email = "vladimir.fajardo@labdat.com.co",
	package = find_packages(),
	install_requires = requirements,
	long_description = readme,
	long_description_content_type = "text/markdown",
	description = "Tablero para MLDS6",
	license = "MIT",
	url = "www.labdat.com.co"
)
