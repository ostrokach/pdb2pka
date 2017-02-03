import os
# import os.path as op
# from distutils.sysconfig import get_python_inc

from setuptools import Extension, setup
# from setuptools.command.build_py import build_py
import numpy as np


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pdb2pka',
    version='1.3.29',
    url='http://www.poissonboltzmann.org/',
    description=(
        "PDB2PKA is the PDB2PQR library that includes both ligand parameterization and "
        "Poisson-Boltzmann-based pKa calculation routines."),
    long_description=read("README.md"),
    license="LGPL",
    packages=[
        'pdb2pka',
        'pdb2pka.graph_cut',
        'pdb2pka.ligandclean',
        'pdb2pka.substruct',
    ],
    package_data={
        'pdb2pka': ['TITRATION.dat'],
        'pdb2pka.ligandclean': ['testcomplexes'],
        'pdb2pka.substruct': ['clique'],
    },
    ext_modules=[
        Extension(
            'pdb2pka/substruct/Algorithms',
            sources=['pdb2pka/substruct/Algorithms.cpp'],
            include_dirs=[np.get_include()]),
        Extension(
            'pdb2pka/_pMC_mult',
            sources=['pdb2pka/pMC_mult.cpp', 'pdb2pka/pMC_mult.i'],
            swig_opts=['-c++'],
            include_dirs=['include']),
    ]
)
