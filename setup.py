from setuptools import setup, find_packages

setup(
    name='mongo-exporter',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
    long_description=open('README.md').read(),
    install_requires=['pyyaml', 'pymongo', 'scorum'],
    entry_points={
        'console_scripts': [
            'modex = modex.mongo:main',
        ]
    },
)
