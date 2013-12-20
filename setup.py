from setuptools import setup, find_packages

import recontools

setup(
    name='recontools',
    version=recontools.__VERSION__,

    provides=['recontools',],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'swiftrecon.plugin': [
            'bender = recontools.bender:Bender',
            'brasilian = recontools.brasilian:Brasilian',
        ]
    },
    zip_safe=False,
)
