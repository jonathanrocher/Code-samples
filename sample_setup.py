import os
from setuptools import setup

setup(
    name = "foo",
    version = "0.1",
    author = "Enthought Inc.",
    author_email = "info@enthought.com",
    description = ("This is a foo package that doesn't do anything"),
    license = "GPL",
    packages=['dir1'],
    long_description=""" This is a long description
    for my package.
    """,
    entry_points = {
        'console_scripts': [
            'foo_exec = dir1.run:main',
            ],
        },
    include_package_data = True,
    data_files=["doc.html"],
    zip_safe = False,
)
