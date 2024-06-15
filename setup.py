from setuptools import setup, find_packages

setup(
    name='m-shell',
    version='0.1',
    packages=find_packages(),
    author='Serge-Olivier Malouin',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'm-shell = m-shell.__main__:main'
        ]
    }
)