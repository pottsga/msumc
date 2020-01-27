from setuptools import setup

package_name = 'directory'

# List of dependencies installed via `pip install -e .`
requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_tm',
    'pyramid_retry',
    'waitress',
    'sqlalchemy',
    'zope.sqlalchemy',
    'bcrypt',
]

dev_requires = [
    'pytest',
]

setup(
    name=package_name,
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            f'main = {package_name}:main'
        ],
        'console_scripts': [
            f'initialize_db = {package_name}.scripts.initialize_db:main'
        ],
    },
)
