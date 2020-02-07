#!/usr/bin/python3.4


"""
Module with different enum types to be used while interacting with database.

			SENSYS GATSO CONFIDENTIAL & PROPRIETARY
			
			@file query_info.py

			@author Dilip Kumar
			@brief Helper class which represents DB Query
			@copyright Sensys Gatso Business
			@date 10th July 2019

"""

from enum import Enum


class QueryEnum(Enum):
	""" Class QueryEnum represents query enum to be used while fetching query string for DB.

    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
	SELECT_POINT_SITES 			= 	1
	SELECT_P2P_SITES 			= 	2
	SELECT_CAMERA_DETAILS 		= 	3
	UPDATE_PTP_ANPR_SIGHTING 	= 	4

	def __iter__(self):
		""" Iterator to Query Enums.

		Args:
			Not Applicable.
		Returns:
			Enum Members.
		Raises:
			Not Applicable.
		"""
		yield QueryEnum.SELECT_POINT_SITES
		yield QueryEnum.SELECT_P2P_SITES
		yield QueryEnum.SELECT_CAMERA_DETAILS
		yield QueryEnum.UPDATE_PTP_ANPR_SIGHTING

	@classmethod
	def is_valid(cls, query_enum):
		""" To validate a query_enum argument.
		
		Args:
			query_enum: Query enum number to be validated.
		Returns:
			bool.
		Raises:
			Not Applicable.
		"""
		return query_enum in QueryEnum

	@classmethod
	def get_members(cls):
		""" To get list of Query enum members.
		
		Args:
			None.
		Returns:
			Enum members.
		Raises:
			Not Applicable.
		"""
		return str(list(QueryEnum))

class QueryType(Enum):
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

	def __iter__(self):
		""" Iterator to get Query Type Enums.

		Args:
			Not Applicable.
		Returns:
			Enum Members.
		Raises:
			Not Applicable.
		"""
		yield QueryType.SELECT
		yield QueryType.UPDATE

	@classmethod
	def is_valid(cls, query_type):
		""" To validate a query_type argument.
		
		Args:
			query_type: Query type to be validated.
		Returns:
			bool.
		Raises:
			Not Applicable.
		"""
		return query_type in QueryType

	@classmethod
	def get_members(cls):
		""" To get list of Query Type enum members.
		
		Args:
			None.
		Returns:
			Enum members.
		Raises:
			Not Applicable.
		"""
		return str(list(QueryType))

class CursorType(Enum):
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
	NORMAL 		= 1
	DICTIONARY 	= 2

	def __iter__(self):
		""" Iterator to get Cursor Type Enums.

		Args:
			Not Applicable.
		Returns:
			Enum Members.
		Raises:
			Not Applicable.
		"""
		yield CursorType.NORMAL
		yield CursorType.DICTIONARY

	@classmethod
	def is_valid(cls, cursor_type):
		""" To validate a cursor_type argument.
		
		Args:
			cursor_type: Cursor type to be validated.
		Returns:
			bool.
		Raises:
			Not Applicable.
		"""
		return cursor_type in CursorType

	@classmethod
	def get_members(cls):
		""" To get list of Cursor Type enum members.
		
		Args:
			None.
		Returns:
			Enum members.
		Raises:
			Not Applicable.
		"""
		return str(list(CursorType))

class RecordCount(Enum):
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
	SINGLE 		= 1
	ALL 		= 2

	def __iter__(self):
		""" Iterator to get Record Count Enums.

		Args:
			Not Applicable.
		Returns:
			Enum Members.
		Raises:
			Not Applicable.
		"""
		yield RecordCount.SINGLE
		yield RecordCount.ALL

	@classmethod
	def is_valid(cls, record_count):
		""" To validate a record_count argument.
		
		Args:
			record_count: Record count to be validated.
		Returns:
			bool.
		Raises:
			Not Applicable.
		"""
		return record_count in RecordCount

	@classmethod
	def get_members(cls):
		""" To get list of Record Count enum members.
		
		Args:
			None.
		Returns:
			Enum members.
		Raises:
			Not Applicable.
		"""
		return str(list(RecordCount))

class Query:
	""" Class Query represents Database query information.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
	"""
	QUERY_SELECT_POINT_SITES 				= 		'''
														SELECT PtpCameraConfig.siteCode, SiteCodeToSiteIndex.siteIndex 
														FROM PtpCameraConfig, SiteCodeToSiteIndex 
														WHERE PtpCameraConfig.siteCode = SiteCodeToSiteIndex.siteCode 
														ORDER BY SiteCodeToSiteIndex.siteIndex;
													'''

	QUERY_SELECT_P2P_SITES					=		'''
														SELECT routeStartSiteCode, routeEndSiteCode, routeIdentifierCode, distanceKm FROM PtpRoute;
													'''

	QUERY_SELECT_CAMERA_DETAILS				=		'''
														SELECT cameraIP, username, password FROM PtpCameraConfig WHERE siteCode = '%s';
													'''

	QUERY_UPDATE_PTP_ANPR_SIGHTING			=		'''
														INSERT INTO PtpAnprSighting(siteCode, uniqueSequence, eventNum, detectionTimeStampUTC, 
														detectionTimeStampUTCSecFraction, detectionTimeStampLocal, lane, numberPlate, 
														numberPlateConfidence, mediaFileLocation, trafficTowards, usedAsTest)
														VALUES ('%s', %s, %s, %s, %f, '%s', %s, '%s', %s, '%s', %s, %s);
													'''

	def __init__(self):
		""" Constructor for Class Query.

		Args:
			Not Applicable.
		Returns:
			Not Applicable.
		Raises:
			Not Applicable.
		"""
		self._query = str()

	@property
	def query(self):
		""" Getter method which represents a mysql query.

		Args:
			Not Applicable.
		Returns:
			Member variable '_query'.
		Raises:
			No Exception is raised.
		"""
		return self._query

	@query.setter
	def query(self, query):
		""" Setter method which represents a mysql query.

		Args:
			query: To be set to member variable '_query'.
		Returns:
			None.
		Raises:
			No Exception is raised.
		""" 
		self._query = query

	def validate_parameter(self, query_enum):
		""" To Validate query enum.

		Args:
			query_enum: One of the enums from 'QueryEnum' class.
		Returns:
			bool, message.
		Raises:
			No Exception is raised.
		"""
		is_valid = False
		message = str()

		if QueryEnum.is_valid(query_enum):
			is_valid = True
		else:
			message = "Invalid Query Enum is found. Valid Enum => {}".format(QueryEnum.get_members())

		return is_valid, message

	@classmethod
	def get_query(cls, query_enum, args = None):
		""" Construct database query string based on query_enum parameter.

		Args:
			query_enum: One of the enums from 'QueryEnum' class.
			args: Arguments to be passed to database query string.
		Returns:
			bool, query_string.
		Raises:
			No Exception is raised.
		"""
		is_valid, message = cls.validate_parameter(cls, query_enum)

		if not is_valid:
			return is_valid, message

		if query_enum == QueryEnum.SELECT_POINT_SITES:
			cls.query = Query.QUERY_SELECT_POINT_SITES

		elif query_enum == QueryEnum.SELECT_P2P_SITES:
			cls.query = Query.QUERY_SELECT_P2P_SITES

		elif query_enum == QueryEnum.SELECT_CAMERA_DETAILS:
			cls.query	= Query.QUERY_SELECT_CAMERA_DETAILS

			if args is not None:
				cls.query = cls.query % (args)

		elif query_enum == QueryEnum.UPDATE_PTP_ANPR_SIGHTING:
			cls.query	= Query.QUERY_UPDATE_PTP_ANPR_SIGHTING

			if args is not None:
				cls.query = cls.query % (args)

		return True, cls.query
