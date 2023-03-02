from setuptools import find_packages, setup
setup(
    name='pyloadanimate',
    packages=find_packages(),
    version='0.1.1',
    description='My first Python library',
    author='Nakul S Kulkarni',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    python_requires = ">=3.7"
)