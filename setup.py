"""
Setup the package.

To use this file, you must:

```sh
$ pip install twine
$ pip install wheel
```
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME = "hintwith"
DESCRIPTION = "Hints your function with an existing one."
URL = "https://github.com/Chitaoji/dataplot"
EMAIL = "2360742040@qq.com"
AUTHOR = "Chitaoji"
REQUIRES_PYTHON = ">=3.8.13"
VERSION = None
REQUIRED = []
EXTRAS = {}


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        LONG_DESCRIPTION = "\n" + f.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
python_exec = exec
if not VERSION:
    PROJECT_SLUG = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(
        os.path.join(here, PROJECT_SLUG, "__version__.py"), encoding="utf-8"
    ) as f:
        python_exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        """Initialize options."""

    def finalize_options(self):
        """Finalize options."""

    def run(self):
        """Run commands."""
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(f"{sys.executable} setup.py sdist bdist_wheel --universal")

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system(f"git tag v{about['__version__']}")
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["examples"]),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="BSD",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
