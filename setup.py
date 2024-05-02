from setuptools import setup, find_packages

VERSION = '0.1.0.dev0'
DESCRIPTION = 'Make effective terminal menus quickly and concisely.'

setup(
    name='seaturtle_menu',
    version=VERSION,
    author='Tathya Garg',
    author_email='tathya.garg@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['menu'],
)