#!/usr/bin/env python

"""
python-django
-------------

python-django -- Description

"""

from os import path as op, walk

from setuptools import setup


def read(path):
    try:
        return open(op.join(op.dirname(__file__), path)).read()
    except IOError:
        return ''

package_data = []
template_path = op.join('starter', 'templates', 'python-django')
for root, dirs, files in walk(template_path):
    if "/.env" in root or '/.tox' in root:
        continue

    for fname in filter(lambda f: not f.endswith('.pyc'), files): # nolint
        if fname in ('django_master.sqlite', 'tox.ini'):
            continue

        fpath = op.join(root, fname)
        package_data.append(op.relpath(
            fpath,
            template_path
        ))


setup(
    name="starter.templates.python-django",
    version="0.1.1",
    license="BSD",
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    platforms=('Any'),

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url='http://github.com//',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    packages=['starter', 'starter.templates',
              'starter.templates.python-django'],
    package_data={"starter.templates.python-django":
                  package_data, "starter.templates": ["python-django.ini"]},
    namespace_packages=["starter", "starter.templates"],
    install_requires = ["starter"],
)
