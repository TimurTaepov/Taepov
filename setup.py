from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'cmf-options-pricer',
    version = version,
    license = license,
    author = 'CMF Team',
    description = 'Options Pricer',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        # put packages here
        'six',
    ],
    test_suite = 'tests',
    entry_points = {
	    'console_scripts': [
	        'packagename = packagename.__main__:main',
	    ]
	}
)
