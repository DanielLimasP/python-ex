try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'MyProject',
    'author': 'My Name',
    'url': 'URL to project',
    'download_url': 'Where to download it',
    'author_email': 'My email',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'rojectName'
]

setup(**config)
