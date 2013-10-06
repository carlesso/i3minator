from setuptools import setup

setup(
    name = 'i3minator',
    version = '0.0.2',
    author = 'Enrico Carlesso',
    author_email = 'enricocarlesso@gmail.com',
    packages = ['i3minator'],
    scripts = ['bin/i3minator'],
    url = 'https://github.com/carlesso/i3minator',
    license = 'LICENSE.txt',
    description = 'i3 project manager similar to tmuxinator',
    long_description = open("README.md").read(),
    install_requires = ['i3-py >= 0.6.4']
)
