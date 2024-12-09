from setuptools import setup, find_packages

setup(
    name='finances',
    version='1.0',
    description='Backend de um aplicativo de finanças pessoais.',
    install_requires=['pytest', 'datetime'],
    packages=find_packages()
)
