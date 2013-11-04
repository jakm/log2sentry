# -*- coding: utf8 -*-
"""
Provides Log2Json class which is a stdlib log formatter that will output log
record in Sentry's JSON format.

Code is based on snitch (https://github.com/ronaldevers/snitch) and
raven-python (https://github.com/getsentry/raven-python) projects.
"""

from .log2json import Log2Json

try:
    VERSION = __import__('pkg_resources').get_distribution('log2sentry').version
except Exception as e:
    VERSION = 'unknown'

__all__ = ('VERSION', 'Log2Json')
