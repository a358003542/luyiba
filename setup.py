#!/usr/bin/env python
# -*-coding:utf-8-*-


from setuptools import setup, find_packages
import os

REQUIREMENTS = ['click',
                'diskcache',
                'requests',
                'my-fake-useragent',
                'js2py'
                ]
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='luyiba',
    version='0.3.0',
    description='英雄联盟随机英雄选择器',
    url='https://github.com/a358003542/luyiba',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='wanze',
    author_email='a358003542@gmail.com',
    maintainer='wanze',
    maintainer_email='a358003542@gmail.com',
    license='MIT',
    platforms='windows',
    keywords=['lol', 'python'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Operating System :: Microsoft :: Windows',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'
                 ],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    setup_requires=REQUIREMENTS,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['luyiba=luyiba.__main__:main', ],
    }
)
