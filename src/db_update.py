#!/usr/bin/python3.4

import pymysql
import collections
from query_info import QueryType, CursorType, RecordCount


"""
Module which interacts with database by executing mysql queries and fetches records.

			SENSYS GATSO CONFIDENTIAL & PROPRIETARY
			
			@file db_update.py

			@author Dilip Kumar
			@brief Helper class which validate query parameters, executes query and returns the result back.
			@copyright Sensys Gatso Business
			@date 10th July 2019
"""


class DBUpdate:
	""" Class DBUpdate represents methods to be used for interacting with mysql DB.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
	DATABASE_HOST = 'localhost'
	DATABASE_NAME = 'aspect'
	DATABASE_USER = 'aspect'
	DATABASE_PASSWORD = ''

	def __init__(self):
		""" Construct for DBUpdate.

		Args:
			Not Applicable.
		Returns:
			Not Applicable.
		Raises:
			No Exception is raised.
		"""
		self.db_connection = None
		self.cursor = None
		self.dict_cursor = None

		self.connect_db()

	def connect_db(self):
		""" Establishes Connection with mysql DB.

		Args:
			None.
		Returns:
			None.
		Raises:
			Not Applicable.
		"""
		self.db_connection = pymysql.connect(DBUpdate.DATABASE_HOST, DBUpdate.DATABASE_USER, DBUpdate.DATABASE_PASSWORD, DBUpdate.DATABASE_NAME)

	def validate_query_parameter(self, query):
		""" Validates the query string parameter.

		Args:
			query: mysql query string to be validated.
		Returns:
			bool, Error message
		Raises:
			Not Applicable.
		"""
		is_valid = False
		message = str()

		if query is None:
			message = "Empty query string found. Skipped."
		else:
			is_valid = True

		return is_valid, message

	def validate_query_type_parameter(self, query_type):
		""" Validates the query type parameter.

		Args:
			query_type: mysql query type to be validated. E.g. SELECT or UPDATE.
		Returns:
			bool, Error message
		Raises:
			Not Applicable.
		"""
		is_valid = False
		message = str()

		if QueryType.is_valid(query_type):
			is_valid = True
		else:
			message = "Invalid Query Type is found. Valid Enum => {}".format(QueryType.get_members())

		return is_valid, message

	def validate_cursor_type_parameter(self, cursor_type):
		""" Validates the cursor type parameter.

		Args:
			cursor_type: mysql cursor type to be validated. E.g. NORMARL or DICTIONARY.
		Returns:
			bool, Error message
		Raises:
			Not Applicable.
		"""
		is_valid = False
		message = str()

		if CursorType.is_valid(cursor_type):
			is_valid = True
		else:
			message = "Invalid Cursor Type is found. Valid Enum => {}".format(CursorType.get_members())

		return is_valid, message

	def validate_record_count_parameter(self, query_type, record_count):
		""" Validates the record count parameter.

		Args:
			query_type: mysql query type. E.g. SELECT or UPDATE,
			record_count: mysql fetched record count. E.g. SINGLE or ALL.
		Returns:
			bool, Error message
		Raises:
			Not Applicable.
		"""
		is_valid = True
		message = str()

		if query_type == QueryType.SELECT:					# Record count is required only for Select query
			if record_count is None or not RecordCount.is_valid(record_count):
				is_valid = False
				message = "Invalid Record Count is found. Valid Enum => {}".format(RecordCount.get_members())

		return is_valid, message

	def validate_parameters(self, query, query_type, cursor_type, record_count):
		""" Validates all the parameters passed before executing mysql query.

		Args:
			query: mysql query string to be validated.
			query_type: mysql query type. E.g. SELECT or UPDATE.
			cursor_type: mysql cursor type to be validated. E.g. NORMARL or DICTIONARY.
			record_count: mysql fetched record count. E.g. SINGLE or ALL.
		Returns:
			bool, Error message
		Raises:
			Not Applicable.
		"""
		is_valid = False
		message = str()

		is_valid, message = self.validate_query_parameter(query)

		if is_valid:
			is_valid, message = self.validate_query_type_parameter(query_type)

			if is_valid:
				is_valid, message = self.validate_cursor_type_parameter(cursor_type)

				if is_valid:
					is_valid, message = self.validate_record_count_parameter(query_type, record_count)

		return is_valid, message

	def set_cursor(self, cursor_type):
		""" Sets the cursor type while fetching records.

		Args:
			cursor_type: mysql cursor type to be validated. E.g. NORMARL or DICTIONARY.
		Returns:
			None.
		Raises:
			Not Applicable.
		"""
		if cursor_type == CursorType.NORMAL:				# Normal cursor
			self.cursor = self.db_connection.cursor()
		elif cursor_type == CursorType.DICTIONARY:			# Dictionary cursor
			self.cursor = self.db_connection.cursor(pymysql.cursors.DictCursor)

	def execute(self, query):
		""" Executes query in mysql db.

		Args:
			query: mysql query string to be executed.
		Returns:
			Status Code, Message.
		Raises:
			Not Applicable.

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
		"""
		code = -1
		message = str()
		
		try:
			self.cursor.execute(query)
			code = 0		# Successfull
			message = "Query '{}' execution successful".format(query)
		except pymysql.ProgrammingError as error:
				code, message = error.args
		except pymysql.DataError as error:
				code, message = error.args
		except pymysql.InternalError as error:
				code, message = error.args
		except pymysql.IntegrityError as error:
				code, message = error.args
		except pymysql.DatabaseError as error:
				code, message = error.args
		except pymysql.NotSupportedError as error:
				code, message = error.args
		except pymysql.OperationalError as error:
				code, message = error.args
		except pymysql.MySQLError as error:
				code, message = error.args
		except pymysql.Error as error:
				code, message = error.args
		except Exception as error:
			message = str(error)

		return code, message

	def execute_query(self, query, query_type, cursor_type, record_count = None):
		""" Executes query in mysql db. Called by query_helper module.

		Args:
			query: mysql query string to be executed.
			query_type: mysql query type. E.g. SELECT or UPDATE.
			cursor_type: mysql cursor type. E.g. NORMARL or DICTIONARY.
			record_count: mysql fetched record count. E.g. SINGLE or ALL.
		Returns:
			A tuple representing (STATUS_CODE, MESSAGE, FETCHED_RECORD)
		Raises:
			Not Applicable.
		"""
		code = -1
		message = str()
		record = dict()

		query_result = collections.namedtuple('QueryResult', 'code message record')

		is_valid, message = self.validate_parameters(query, query_type, cursor_type, record_count)

		if not is_valid:			# Invalid query parameters
			return query_result(code=code, message=message, record=record)

		self.set_cursor(cursor_type)

		code, message = self.execute(query)

		if code == 0:								# Query executed successfully
			if query_type == QueryType.SELECT:		# Select query
				if record_count == RecordCount.SINGLE:
					record = self.cursor.fetchone()
				elif record_count == RecordCount.ALL:
					record = self.cursor.fetchall()
			elif query_type == QueryType.UPDATE:	# Update query
				self.db_connection.commit()

		return query_result(code=code, message=message, record=record)

	def __del__(self):
		""" Destructor for DBUpdate.
			Closes cursor and connection with DB.

		Args:
			None.
		Returns:
			None.
		Raises:
			Not Applicable.
		"""
		if self.cursor is not None:
			self.cursor.close()

		if self.dict_cursor is not None:
			self.dict_cursor.close()

		if self.db_connection is not None:
			self.db_connection.close()
