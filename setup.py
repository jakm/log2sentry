#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

setup(
    name='log2sentry',
    packages=['log2sentry',
              'log2sentry.raven',
              'log2sentry.raven.serializer'],
    version='0.2',
    author='Jakub Matys',
    author_email='matys.jakub@gmail.com',
    url='https://github.com/jakm/log2sentry',
    description="Sentry's JSON log formatter"
)
