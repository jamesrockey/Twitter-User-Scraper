from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='twitter-user-scraoer',
    version='0.1.0',
    description='Twitter user data scraper for Quant application',
    long_description=readme,
    author='James Rockey',
    author_email='jmsneilrock@gmail.com',
    url='https://github.com/jamesrockey/James-Rockey-Quant-OA',
    license=license,
    packages=find_packages()
)