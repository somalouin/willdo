from setuptools import setup, find_packages

setup(
    name='willdo',
    version='0.1',
    packages=find_packages(),
    author='Serge-Olivier Malouin',
    install_requires=[
      'pytest',
      'pylint',
      'pyfiglet',
      "notion-client",
      "python-dotenv"
    ],
    entry_points={
        'console_scripts': [
            'willdo = willdo.__main__:main'
        ]
    }

)