from setuptools import setup, find_packages

VERSION = '1.0.0' 
DESCRIPTION = 'Computes a phonetic distance between two words'
LONG_DESCRIPTION = 'Computes a phonetic distance between two words'

# Setting up
setup(
    name='phonetic_distance',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'phonetic_distance = phonetic_distance.__main__:main',
        ],
    },
)
