import re
import sys
from setuptools import setup
from io import open

VERSION = '1.6.4'

long_description = open('README.rst', 'rt', encoding='utf8').read()

# PyPI can't process links with anchors
long_description = re.sub(r'<(.*)#.*>`_', '<\g<1>>`_', long_description)

setup(
    name='aio-cloudpayments',  # Переименовано, чтобы указать асинхронную природу
    packages=['cloudpayments'],

    description='CloudPayments Python Client Library (Asynchronous version)',
    long_description=long_description,

    version=VERSION,

    author='Antida software',
    author_email='info@antidasoftware.com',
    license='MIT license',

    url='https://github.com/ex3lite/aio-cloudpayments-python-client',  # Ссылка на ваш форк
    download_url=f'https://github.com/ex3lite/aio-cloudpayments-python-client/tarball/{VERSION}',

    install_requires=[
        'aiohttp >=3.7.0',  # Асинхронная зависимость для HTTP-запросов
        'pytz >=2015.7'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',  # Обновлено
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    zip_safe=False
)
