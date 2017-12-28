from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='spiro',
    version='0.1.1',
    description='Module to draw spirographs with turtle graphics',
    url='https://github.com/david.dekoning/spiro',
    author='David de Koning',
    author_email='david.dekoning+spiro@gmail.com',
    python_requires='>=3.6',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Artistic Software',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='turtle spirograph education graphics',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
)