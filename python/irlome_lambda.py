#!/usr/bin/env python3
''' Template for IRLOME lambda version
'''

__author__ = "Nick Dickens"
__copyright__ = "Copyright 2018, Nicholas J. Dickens"
__email__ = "dickensn@fau.edu"
__license__ = "MIT"

import json
import os


def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['filename'],
                                    event['geotag'])
    return {
        'message' : message
    }
