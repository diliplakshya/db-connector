#!/usr/bin/python3.4

"""
Module to trigger mysql query execution.

			SENSYS GATSO CONFIDENTIAL & PROPRIETARY
			
			@file query_helper.py

			@author Dilip Kumar
			@brief Helper class which is used by external python module to execute a DB query.
			@copyright Sensys Gatso Business
			@date 10th July 2019
"""

from db_update import DBUpdate
from query_info import Query, QueryType, CursorType, RecordCount


class QueryHelper:
	""" Class QueryHelper helps in executing DB query.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
	def __init__(self):
		""" Constructor for Class QueryHelper.
			It connects db_update module.

		Args:
			Not Applicable.
		Returns:
			Not Applicable.
		Raises:
			Not Applicable.
		"""
		self.connection = DBUpdate()

	def execute_query(self, query_enum, query_type = QueryType.SELECT, cursor_type = CursorType.DICTIONARY, args = None, record_count = RecordCount.ALL):
		""" Helper to execute DB query.
			It calls db_update module with actually executes the DB query.

		Args:
			query_enum: Enum representing the Query string to be picked up for executing sql command.
			query_type: Enum representing the Query type to choose from 'SELECT' or 'UPDATE'.
			cursor_type: Enum representing the Cursor type to choose from. Normal cursor or Dictionary Cursor.
			args: Arguments tuple to be passed to Query string.
			record_count: Enum representing the number of records to be fetched. Either Single or ALL records.
		Returns:
			A tuple representing (STATUS_CODE, MESSAGE, FETCHED_RECORD)
		Raises:
			Not Applicable.
		"""
		# Fetch query string
		is_valid, query_string = Query.get_query(query_enum = query_enum, args = args)

		if is_valid:		# Valid query
			return self.connection.execute_query(query_string, query_type = query_type, cursor_type = cursor_type, record_count = record_count)
		else:# Invalid query
			return -1, query_string, None
