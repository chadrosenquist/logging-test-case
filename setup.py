from setuptools import setup
import io
import os

"""
To upload to PyPI:
https://packaging.python.org/tutorials/distributing-packages/

python setup.py sdist bdist_wheel
twine upload dist/*
"""

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
cwd = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(cwd, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
    name='logging-test-case',
    version='1.2',
    description='Provides class LoggingTestCase to help test log files.',
    long_description=long_description,
    keywords='unit testing log files logging regression logging-test-case loggingtestcase',
    author='Chad Rosenquist',
    author_email='chadrosenquist@gmail.com',
    url='https://github.com/chadrosenquist/logging-test-case',
    packages=['loggingtestcase'],
    license='MIT',
    python_requires='>=3'
)
