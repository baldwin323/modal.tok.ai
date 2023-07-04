from setuptools import setup, find_packages

setup(
    name='Prompt.md',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open('requirements.txt', 'r')
    ],
    entry_points={
        'console_scripts': [
            'promptmd=src.main:main',
        ],
    },
    test_suite='tests',
)