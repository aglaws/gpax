"""GPax.

See more details in the
[`README.md`](https://github.com/aglaws/gpax).
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name='gpax',
    version='0.0.1',
    description='gpax',
    author='gpax Team',
    url='http://github.com/aglaws/gpax',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'absl-py>=0.8.1',
        'flax',
        'jax',
        'ml_collections',
        'numpy>=1.7',
        'optax',
        'pandas',
        'tensorflow_probability',
    ],
    extras_require={},
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='gaussian process jax',
)
