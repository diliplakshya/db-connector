#!/usr/bin/python3.4

"""Provides database query attributes.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file db_query_info.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 15th Feb 2019

About; -
--------
    This python module is responsbile for providing database query information.

Design Pattern; -
-----------------
    This is implemented as a part of Abstract factory design pattern.

Working; -
----------
    This python module helps to read query information.

Uses; -
-------
    This will be used by any client who wishes to execute query in database.

Reference; -
------------
    http://wiki.aspecttraffic.com.au/display/SFTW/Database+Connector+Design+Document

"""

# #############################################################################
# #######                      CHANGE RECORD                          #########
# -----------------------------------------------------------------------------
# Date (DD-MM-YY)  |  Author                    |   Change
# -----------------------------------------------------------------------------
# 16-02-19            Dilip Kumar Sharma            New file added.
#
#                                                                              
# #############################################################################


import abc
from enum import IntEnum


class QueryType(IntEnum):
    """ Class QueryType represents query type.
		To fetch record from DB table, use 'SELECT'.
		To update DB table, use 'UPDATE'.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
    SELECT = 1
    UPDATE = 2


class CursorType(IntEnum):
    """ Class CursorType represents type of database cursor to be used while fetching records.
		To fetch normal record from DB table, use 'NORMAL'.
		To fetch dictionary type records from DB table, use 'DICTIONARY'.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
    NORMAL      = 1
    DICTIONARY  = 2


class RecordCount(IntEnum):
    """ Class RecordCount represents Record Count Type.
		To fetch single record from DB table, use 'SINGLE'.
		To fetch all records from DB table, use 'ALL'.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
    SINGLE  =   1
    Many    =   2
    ALL     =   3
