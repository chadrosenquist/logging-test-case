from setuptools import setup

"""
To upload to PyPI:
https://packaging.python.org/tutorials/distributing-packages/

python setup.py sdist bdist_wheel
twine upload dist/*
"""
setup(name='logging-test-case',
      version='1.1',
      description='Provides class LoggingTestCase to help test log files.',
      keywords='unit testing log files logging regression',
      author='Chad Rosenquist',
      author_email='chadrosenquist@gmail.com',
      url='https://github.com/chadrosenquist/logging-test-case',
      packages=['loggingtestcase'],
      license='MIT',
      python_requires='>=3.6'
)
