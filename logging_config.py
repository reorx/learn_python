#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Requires colorlog package

import logging
import logging.config


sock_log = logging.getLogger('socket')
data_log = logging.getLogger('data')

conf = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'colored',
            'level': 'INFO',
        }
    },
    'formatters': {
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(name)-6s] %(asctime)s %(levelname)-5s %(message)s',
        },
        'normal': {
            'format': '[%(name)-6s] %(asctime)s %(levelname)-5s %(message)s',
        }
    },
}


def dict_config(config=None):
    if not config:
        config = conf
    logging.config.dictConfig(conf)
