# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['expression']

package_data = \
{'': ['*']}

install_requires = \
[]

setup_kwargs = {
    'name': 'expression',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'luliangce',
    'author_email': 'luliangce@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}

setup(**setup_kwargs)
