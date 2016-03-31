from setuptools import setup

setup(
    name='bofhexcuse',
    version='0.3.0',
    packages=['bofhexcuse'],
    url='https://github.com/okzach/bofhexcuse/',
    license='',
    author='Zach Adams',
    author_email='zach@okzach.com',
    description='Generate random BOFH themed technical excuses!',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bofhexcuse=bofhexcuse:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language:: Python:: 2',
        'Programming Language:: Python:: 2.7',
        'Programming Language:: Python:: 3',
        'Programming Language:: Python:: 3.5',
        'Topic :: Games/Entertainment :: Fortune Cookies'
    ]
)
