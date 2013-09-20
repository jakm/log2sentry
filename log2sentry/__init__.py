# -*- coding: utf8 -*-
"""
Provides Log2Json class which is a stdlib log formatter that will output log
record in Sentry's JSON format.

Code is based on snitch (https://github.com/ronaldevers/snitch) and
raven-python (https://github.com/getsentry/raven-python) projects.
"""

from .log2json import Log2Json

__all__ = ('Log2Json')
