import os
from os.path import join

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

# code from https://github.com/rafaelpsilva07/cython_package_example

directory_path = os.path.dirname(os.path.abspath(__file__))

ext_data = {
    "core.levenshtein": {
        "sources": [join(directory_path, "fuzzcy", "core", "levenshtein.pyx")],
        "include": [np.get_include()],
    },
}


extensions = []

for name, data in ext_data.items():

    sources = data["sources"]
    include = data.get("include", [])

    obj = Extension(name, sources=sources, include_dirs=include)

    extensions.append(obj)

setup(
    name="levenshtein",
    author="Cloves Paiva",
    package_dir={"core": join(directory_path, "fuzzcy")},
    ext_modules=cythonize(extensions),
)
