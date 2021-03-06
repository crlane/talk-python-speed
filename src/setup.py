from setuptools import (
    setup,
    find_packages
)
from Cython.Build import cythonize

setup(
    name='speedy',
    version='0.1.0.dev',
    description='shows how to use cython',
    author='Cameron Lane',
    author_email='crlane@adamanteus.com',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    ext_modules=cythonize("speedy/*.pyx", annotate=True),
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
