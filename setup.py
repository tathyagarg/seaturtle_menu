from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Make effective terminal menus quickly and concisely.'

setup(
    name='seaturtle_menu',
    version=VERSION,
    author='Tathya Garg',
    author_email='tathya.garg@gmail.com',
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['menu'],
    project_urls={
        "Homepage": "https://github.com/tathyagarg/seaturtle_menu",
        "Documentation": "https://github.com/tathyagarg/seaturtle_menu",
        "Repository": "https://github.com/tathyagarg/seaturtle_menu",
        "Changelog": "https://github.com/tathyagarg/seaturtle_menu/blob/main/CHANGELOG.md"
    }
)