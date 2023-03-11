from distutils.core import Extension, setup

from Cython.Build import cythonize

exts = cythonize(
    [
        Extension(
            "levenshtein_import",
            sources=["src/core/levenshtein.c", "levenshtein_import.pyx"],
        )
    ]
)

setup(ext_modules=exts)
