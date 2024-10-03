from setuptools import setup, find_packages

setup (
    name = 'GetweatherdataUploadPyPi',
    version = '0.0.1',
    author = 'DmitryBaranovgit',
    author_email = 'dmitrybaranovmail@gmail.com',
    description = 'A simple package for retrieving weather data using the OpenWeatherMap API',
    long_description = open('README.md', encoding = 'utf-8').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/DmitryBaranovgit/Prog5/blob/main/Lr3',
    packages = find_packages(),
    install_requires = [
        'requests',
        'pytest'
    ],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.6',
)