#!/usr/bin/python3.4

"""Provides database query attributes.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file db_query.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 15th Feb 2019

About; -
--------
    This python module is responsbile for providing attributes required to execute database query.

Design Pattern; -
-----------------
    This is implemented as a part of Abstract factory design pattern.

Working; -
----------
    This python module helps to set query parameters.

Uses; -
-------
    This will be used by any client who wishes to execute query in database.

Reference; -
------------
    

"""

# #############################################################################
# #######                      CHANGE RECORD                          #########
# -----------------------------------------------------------------------------
# Date (DD-MM-YY)  |  Author                    |   Change
# -----------------------------------------------------------------------------
# 15-02-19            Dilip Kumar Sharma            New file added.
#
#                                                                              
# #############################################################################


import abc


class Query:
    """ Class Query represents the database query used by a client to execute a query in database.

    This object is received by Connection class to execute query in database.

    This object will be filled by a client who wishes to execute query in database.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    pass


class MySqlQuery(Query):
    """ Class MySqlQuery represents the MySql database query used by a client to execute a MySql query in database.

    This object is received by MySqlDBConnection class to execute query in MySql database.

    This object will be filled by a client who wishes to execute query in MySql database.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    def __init__(self):
        self._query_string      =   None
        self._query_type        =   None
        self._record_count      =   None
        self._info              =   None                # This will be of dict type. All other information will be stored in this.

    @property
    def query_string(self):       
        return self._query_string
 
    @query_string.setter
    def query_string(self, query_string):
        self._query_string = query_string

    @property
    def query_type(self):       
        return self._query_type
    
    @query_type.setter
    def query_type(self, query_type):
        self._query_type = query_type

    @property
    def record_count(self):       
        return self._record_count
    
    @record_count.setter
    def record_count(self, record_count):
        self._record_count = record_count

    @property
    def info(self):       
        return self._info
    
    @info.setter
    def info(self, info):
        self._info = info


class OracleQuery(Query):
    """ Class OracleQuery represents the Oracle database query used by a client to execute a Oracle query in database.

    This object is received by OracleDBConnection class to execute query in Oracle database.

    This object will be filled by a client who wishes to execute query in Oracle database.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    def __init__(self):
        self._query_string      =   None
        self._query_type        =   None
        self._record_count      =   None
        self._info              =   None                # This will be of dict type. All other information will be stored in this.

    @property
    def query_string(self):       
        return self._query_string
 
    @query_string.setter
    def query_string(self, query_string):
        self._query_string = query_string

    @property
    def query_type(self):       
        return self._query_type
    
    @query_type.setter
    def query_type(self, query_type):
        self._query_type = query_type

    @property
    def record_count(self):       
        return self._record_count
    
    @record_count.setter
    def record_count(self, record_count):
        self._record_count = record_count

    @property
    def info(self):       
        return self._info
    
    @info.setter
    def info(self, info):
        self._info = info
