
from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="sagar",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ', 'datasets','pypdf','python-dotenv','flask']
)