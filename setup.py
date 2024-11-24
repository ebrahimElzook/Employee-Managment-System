from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in employee_managment_system/__init__.py
from employee_managment_system import __version__ as version

setup(
	name="employee_managment_system",
	version=version,
	description="Employee Managment System BrainWise task",
	author="ebrahimelzook@gmail.com",
	author_email="ebrahimelzook@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
