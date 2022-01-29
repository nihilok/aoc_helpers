from setuptools import setup, find_packages

setup(
    name='aoc-helpers',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/nihilok/aoc-helpers',
    license='MIT',
    author='nihilok',
    author_email='mjfullstack@gmail.com',
    description='Tools to help with Advent of Code puzzles',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
)
