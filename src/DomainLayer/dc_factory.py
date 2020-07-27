#!/usr/bin/env python3.4

"""Database Connector Factory.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file dc_factory.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 16th Feb 2019

About; -
--------
    This python module is responsible for creating factory for Database Connector.
    Each of such database connector factory is responsible for creating database specific objects.

Design Pattern; -
-----------------
    It is implemented as Abstract factory design pattern.

Working; -
----------
    This python module will create database specific objects.

    For example, for MySqlDCFactory creates all objects related to MySql database communication.

Uses; -
-------
    This will be used by any client who wishes to communicate with database.

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


import os
import abc
from enum import IntEnum
from dc_config_dao_factory import DCConfigDaoFactory
from db_connection import MySqlDBConnection, OracleDBConnection
from db_query import MySqlQuery, OracleQuery


class DCFactoryType(IntEnum):
    """ Class DCFactoryType represents the enumeration for factory types.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    MYSQL_FACTORY   =   1
    ORACLE_FACTORY  =   2
    

class DCFactory(object):
    """ Abstract Class DCFactory is base class for database specific DC Factory.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    __metaclass__ = abc.ABCMeta

    DC_FACT_ENV_VAR         =   "DC_FACT_TYPE"
    DEF_DC_FACT_TYPE        =   DCFactoryType.MYSQL_FACTORY    

    def __init__(self):
        self.config_dao_factory = None
        self.database_config = None
        self.initialize()                   

    def initialize(self):
        """ To initialize database configuration.

        It will create config dao factory and read the configurations.

        This method needs to be called once only to read the configuration of database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """ 
        self.config_dao_factory      =   DCConfigDaoFactory().get_dc_config_dao_factory()
        
    @classmethod
    def get_factory_type(cls):
        factory_type = os.getenv(cls.DC_FACT_ENV_VAR, None)        # Returns None if key does not exist

        return cls.DEF_DC_FACT_TYPE if factory_type is None else int(factory_type)

    @abc.abstractmethod
    def get_connection(self):
        raise NotImplementedError("Abstract method 'get_connection' needs implementation.")

    @abc.abstractmethod
    def get_query(self):
        raise NotImplementedError("Abstract method 'get_query' needs implementation.")

    @classmethod
    def get_dc_factory(cls):
        """ Creates database specific factory.

        Args:
            Not Applicable.
        Returns:
            DCFactory: Specific configuration DAO.
        Raises:
            ValueError: If configuration factory type is not among the constants in DCFactoryType.
        """
        factory_type = cls.get_factory_type()

        if factory_type == DCFactoryType.MYSQL_FACTORY:
            return MySqlDCFactory()
        elif factory_type == DCFactoryType.ORACLE_FACTORY:
            return OracleDCFactory()
        else:
            raise ValueError("Invalid DC Factory Type")


class MySqlDCFactory(DCFactory):
    """ Class MySqlDCFactory is the specific DCFactory class for MySql database.

    This is responsible for creating MySql specific objects.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        super(MySqlDCFactory, self).__init__()
        self.database_config = None
        self.initialize()               

    def initialize(self):
        """ To initialize MySql database configuration.

        It will create config dao factory and read the configurations.

        This method needs to be called once only to read the configuration of database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        super(MySqlDCFactory, self).initialize()
        connection_dao          =   self.config_dao_factory.get_connection_dao()
        self.database_config    =   connection_dao.get_mysql_connection_config()

    def get_connection(self):
        """ Returns MySqlDBConnection class object.

        Args:
            Not Applicable.
        Returns:
            MySqlDBConnection: To connect to MySql database.
        Raises:
            Not Applicable.
        """         
        return MySqlDBConnection(self.database_config)

    def get_query(self):
        """ Returns Query object for MySql database.

        Args:
            Not Applicable.
        Returns:
            MySqlQuery: Query object for MySql database.
        Raises:
            Not Applicable.
        """         
        return MySqlQuery()


class OracleDCFactory(DCFactory):
    """ Class OracleDCFactory is the specific DCFactory class for Oracle database.

    This is responsible for creating Oracle specific objects.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        super(OracleDCFactory, self).__init__()
        self.database_config = None
        self.initialize()               

    def initialize(self):
        """ To initialize Oracle database configuration.

        It will create config dao factory and read the configurations.

        This method needs to be called once only to read the configuration of database.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            Not Applicable.
        """
        super(OracleDCFactory, self).initialize()
        connection_dao          =   self.config_dao_factory.get_connection_dao()
        self.database_config    =   connection_dao.get_oracle_connection_config()                

    def get_connection(self):
        """ Returns OracleDBConnection class object.

        Args:
            Not Applicable.
        Returns:
            OracleDBConnection: To connect to Oracle database.
        Raises:
            Not Applicable.
        """         
        return OracleDBConnection(self.database_config)

    def get_query(self):
        """ Returns Query object for Oracle database.

        Args:
            Not Applicable.
        Returns:
            OracleQuery: Query object for Oracle database.
        Raises:
            Not Applicable.
        """
        return OracleQuery()       