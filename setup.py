# coding: utf-8
from setuptools import find_packages, setup

setup(
    name='acrux_blog',
    description='Blog que adiciona dados em um Banco Relacional e no Redis, para seu comparativo',
    author='Douglas Bastos',
    author_email='douglashsb@gmail.com',
    url='',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'redis==2.10.3'
    ]
)
