from setuptools import setup

setup(
    name='flask-my-extension',
    entry_points={
        'console_scripts': [
            'wiki=wiki:cli'
        ],
    },
)
