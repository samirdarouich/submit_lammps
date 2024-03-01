
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Setting up LAMMPS simulations to cluster'

# Setting up
setup(
    name="run_lmp",
    version=VERSION,
    author="Samir Darouich",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy',
                      'toml',
                      'jinja2'
                      ],
    entry_points={'console_scripts': ['run_lammps = run_lmp.main:main',]
    },

    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
