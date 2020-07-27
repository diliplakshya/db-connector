#!/usr/bin/python3.4

"""Provides database connection functionlity.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file db_connection.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 15th Feb 2019

About; -
--------
    This python module is responsible for providing database connection functionlity for database connection component.

Design Pattern; -
-----------------
    This is implemented as a part of Abstract factory design pattern.

Working; -
----------
    This python module provides methods to connect to database and disconnect from
    database.
    

Uses; -
-------
    This will be used by any client who wishes to communicate with database.

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
import pymysql
from db_query import MySqlQuery, OracleQuery
from db_query_info import QueryType, CursorType, RecordCount


class QueryResult:
    """ Class QueryResult represents the database query result which is sent to client post executing database query.

    This object is returned by QueryExecutor to denote the database query result.

    This object will be filled by a client who wishes to execute query in database.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    def __init__(self):
        self._code      =   None
        self._message   =   None
        self._result    =   None
        self._info      =   None            # Any other information will be store here. It's of a dict type.

    @property
    def code(self):       
        return self._code
    
    @code.setter
    def code(self, code):
        self._code = code

    @property
    def message(self):       
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message

    @property
    def result(self):       
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result

    @property
    def info(self):       
        return self._info
    
    @info.setter
    def info(self, info):
        self._info = info


class DBConnection:
    """ Abstract class DBConnection is base class for specific DBConnection.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, database_config):
        self.database_config = database_config

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError("Abstract method 'connect' needs implementation.")

    @abc.abstractmethod
    def execute(self, query, is_commit = False):
        raise NotImplementedError("Abstract method 'execute' needs implementation.")

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError("Abstract method 'commit' needs implementation.")

    @abc.abstractmethod
    def disconnect(self):
        raise NotImplementedError("Abstract method 'disconnect' needs implementation.")

    # To Do : Add method to set transaction level

class MySqlDBConnection(DBConnection):
    """ Class MySqlDBConnection is the specific DAO class for MySql Database connection.

        MYSQL Exception classification:
		------------------------------

		class MySQLError(Exception):
			Exception related to operation with MySQL.

		class Warning(Warning, MySQLError):
			Exception raised for important warnings like data truncations
			while inserting, etc.

		class Error(MySQLError):
			Exception that is the base class of all other error exceptions
			(not Warning).

		class InterfaceError(Error):
			Exception raised for errors that are related to the database
			interface rather than the database itself.

		class DatabaseError(Error):
			Exception raised for errors that are related to the
			database.

		class DataError(DatabaseError):
			Exception raised for errors that are due to problems with the
			processed data like division by zero, numeric value out of range,
			etc.

		class OperationalError(DatabaseError):
			Exception raised for errors that are related to the database's
			operation and not necessarily under the control of the programmer,
			e.g. an unexpected disconnect occurs, the data source name is not
			found, a transaction could not be processed, a memory allocation
			error occurred during processing, etc.

		class IntegrityError(DatabaseError):
			Exception raised when the relational integrity of the database
			is affected, e.g. a foreign key check fails, duplicate key,
			etc.

		class InternalError(DatabaseError):
			Exception raised when the database encounters an internal
			error, e.g. the cursor is not valid anymore, the transaction is
			out of sync, etc.

		class ProgrammingError(DatabaseError):
			Exception raised for programming errors, e.g. table not found
			or already exists, syntax error in the SQL statement, wrong number
			of parameters specified, etc.

		class NotSupportedError(DatabaseError):
			Exception raised in case a method or database API was used
			which is not supported by the database, e.g. requesting a
			.rollback() on a connection that does not support transaction or
			has transactions turned off.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self, database_config):
        super(MySqlDBConnection, self).__init__(database_config)
        self._connection = None
        self._cursor = None
        self._cursor_type = None

    @property
    def connection(self):       
        return self._connection
    
    @connection.setter
    def connection(self, connection):
        self._connection = connection

    @property
    def cursor(self):       
        return self._cursor
    
    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor

    @property
    def cursor_type(self):       
        return self._cursor_type
    
    @cursor_type.setter
    def cursor_type(self, cursor_type):
        self._cursor_type = cursor_type

    def connect(self):
        """ To connect to MySql database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        query_result = QueryResult()
		
        try:
            self.connection = pymysql.connect(self.database_config.host, self.database_config.user, self.database_config.password, self.database_config.name)
        except pymysql.ProgrammingError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DataError as error:
            query_result.code, query_result.message = error.args
        except pymysql.InternalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.IntegrityError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DatabaseError as error:
            query_result.code, query_result.message = error.args
        except pymysql.NotSupportedError as error:
            query_result.code, query_result.message = error.args
        except pymysql.OperationalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.MySQLError as error:
            query_result.code, query_result.message = error.args
        except pymysql.Error as error:
            query_result.code, query_result.message = error.args
        except Exception as error:
            query_result.code = 9999
            query_result.message = str(error)
        else:
            query_result.code       =       0		        # Successfull
            query_result.message    =       "Database connection successful."

        return query_result

    def set_cursor(self, cursor_type):
        """ To set cursor for MySql database.

        Args:
            cursor_type: Type of cursor, e.g. Dictionary Cursor
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        query_result = QueryResult()
		
        try:
            if cursor_type == CursorType.DICTIONARY:
                self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            else:
                self.cursor = self.connection.cursor()
        
        except pymysql.ProgrammingError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DataError as error:
            query_result.code, query_result.message = error.args
        except pymysql.InternalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.IntegrityError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DatabaseError as error:
            query_result.code, query_result.message = error.args
        except pymysql.NotSupportedError as error:
            query_result.code, query_result.message = error.args
        except pymysql.OperationalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.MySQLError as error:
            query_result.code, query_result.message = error.args
        except pymysql.Error as error:
            query_result.code, query_result.message = error.args
        except Exception as error:
            query_result.code = 9999
            query_result.message = str(error)
        else:
            query_result.code       =       0		        # Successfull
            query_result.message    =       "Cursor created successfully."

        return query_result

    def execute(self, query, is_commit = False):
        """ To execute query in MySql database.

        Args:
            query: MySqlQuery object representing query attributes.
        Returns:
            QueryResult: Object representing query result.
        Raises:
            Not Applicable.
        """
        query_result = QueryResult()
		
        try:
            self.cursor.execute(query.query_string)
        except pymysql.ProgrammingError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DataError as error:
            query_result.code, query_result.message = error.args
        except pymysql.InternalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.IntegrityError as error:
            query_result.code, query_result.message = error.args
        except pymysql.DatabaseError as error:
            query_result.code, query_result.message = error.args
        except pymysql.NotSupportedError as error:
            query_result.code, query_result.message = error.args
        except pymysql.OperationalError as error:
            query_result.code, query_result.message = error.args
        except pymysql.MySQLError as error:
            query_result.code, query_result.message = error.args
        except pymysql.Error as error:
            query_result.code, query_result.message = error.args
        except Exception as error:
            query_result.code = 9999
            query_result.message = str(error)
        else:
            query_result.code       =       0		        # Successfull
            query_result.message    =       "Query execution successful."

            if query.query_type == QueryType.SELECT:
                if query.record_count == RecordCount.SINGLE:
                    query_result.result = self.cursor.fetchone()
                elif query.record_count == RecordCount.Many:
                    query_result.result = self.cursor.fetchmany()                
                if query.record_count == RecordCount.ALL:
                    query_result.result = self.cursor.fetchall()
            elif is_commit:
                self.connection.commit()

        return query_result

    def commit(self):
        """ To commit recrods in MySql database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """        
        self.connection.commit()

    def disconnect(self):
        """ To disconnect from MySql database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """        
        if self.cursor is not None:
            self.cursor.close()

        if self.connection is not None:
            self.connection.close()

    def __del__(self):
        """ Destructor for DBUpdate.
		
        Closes cursor and connection.

		Args:
			None.
		Returns:
			None.
		Raises:
			Not Applicable.
		"""
        self.disconnect()


class OracleDBConnection(DBConnection):
    """ Class OracleDBConnection is the specific DAO class for Oracle Database connection.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self, database_config):
        super(OracleDBConnection, self).__init__(database_config)
        self.database_config = database_config      # OracleConnectionConfig object

    def connect(self):
        """ To connect to Oracle database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """        
        pass

    def execute(self, query, is_commit = False):
        """ To execute query in Oracle database.

        Args:
            query: OracleQuery object representing query attributes.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """        
        pass

    def commit(self):
        """ To commit recrods in Oracle database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        pass

    def disconnect(self):
        """ To disconnect from Oracle database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """        
        pass    