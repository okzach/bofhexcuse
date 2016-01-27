from setuptools import setup

setup(
    name='bofhexcuse',
    version='0.2.0',
    packages=['bofhexcuse'],
    url='https://github.com/okzach/bofhexcuse/',
    license='',
    author='Zach Adams',
    author_email='zach@okzach.com',
    description='Channel the BOFH to generate a random technical excuse.',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bofhexcuse=bofhexcuse:main'
        ]
    }
)
