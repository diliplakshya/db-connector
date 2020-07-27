#!/usr/bin/env python3.4

"""DAO factory for Database Connector configuration.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file dc_config_dao_factory.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 12th Feb 2019

About; -
--------
    This python module is responsible for creating configuration specific DAO factory for Database Connector.
    Each of such DAO factory is responsible for creating configuration specific DAOs for Database Connector.

Data Source; -
--------------
    It could be any type of configuration.

DAL/DAO Factory; -
------------------
    DAO (Data Access Object) Factory is part of DAL (Data Acceess Layer) which helps us to 
    create a loose coupling between Core logic and data source (Config).

    For each type of data source, we will have one DAO factory representing that data source.

Loose Coupling; -
-----------------
    Whene we use Database Connector in other projects then we do not need to change the
    core logic, we just need to update DAL or DAOs according to the configuration
    type used in that project.

    This way the core logic is segregated 
    from the data source and it does not talk to data source directly.

Design Pattern; -
-----------------
    DAO factory follows Abstract factory design pattern.

Working; -
----------
    This DAO will create configuration specific DAO factory on request.

    Each of these factories will create DAOs for Database Connector.
    
    For example, for JsonDCDaoFactory creates all DAOs of Database Connector 
    which are specific to Json configuration.

Uses; -
-------
    This DAO is used in Database Connector's core logic.

    Core logic will talk to this DAO Factory to create configuration specific dao.

Reference; -
------------
    

"""

# #############################################################################
# #######                      CHANGE RECORD                          #########
# -----------------------------------------------------------------------------
# Date (DD-MM-YY)  |  Author                    |   Change
# -----------------------------------------------------------------------------
# 12-02-19            Dilip Kumar Sharma            New file added.
#
#                                                                              
# #############################################################################


import os
import abc
from enum import IntEnum
from dc_connection_dao import JsonConnectionDao, YamlConnectionDao, IniConnectionDao, XmlConnectionDao, TextConnectionDao


class DCConfigFactoryType(IntEnum):
    """ Class DCConfigFactoryType represents the enumeration for factory types.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    JSON_FACTORY = 1
    YAML_FACTORY = 2
    INI_FACTORY  = 3
    XML_FACTORY  = 4
    TEXT_FACTORY = 5
    

class DCConfigDaoFactory(object):
    """ Abstract Class DCConfigDaoFactory is base class for configuration specific DCConfig Factory.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    __metaclass__ = abc.ABCMeta

    DC_CFG_FACT_ENV_VAR      =   "DC_CFG_FACT_TYPE"
    DEF_CFG_FACT_TYPE        =   DCConfigFactoryType.JSON_FACTORY

    def __init__(self):
        pass                        

    @classmethod
    def get_factory_type(cls):
        factory_type = os.getenv(cls.DC_CFG_FACT_ENV_VAR, None)        # Returns None if key does not exist

        return cls.DEF_CFG_FACT_TYPE if factory_type is None else int(factory_type)

    @classmethod
    def get_dc_config_dao_factory(cls):
        """ Creates configuration specific factory.
        
        Args:
            Not Applicable.
        Returns:
            DCConfigDaoFactory: Specific configuration DAO.
        Raises:
            ValueError: If configuration factory type is not among the constants in ConfigFactoryType.
        """
        factory_type = cls.get_factory_type()

        if factory_type == DCConfigFactoryType.JSON_FACTORY:
            return JsonDCConfigDaoFactory()
        elif factory_type == DCConfigFactoryType.YAML_FACTORY:
            return YamlDCConfigDaoFactory()            
        elif factory_type == DCConfigFactoryType.INI_FACTORY:
            return IniDCConfigDaoFactory()
        elif factory_type == DCConfigFactoryType.XML_FACTORY:
            return XmlDCConfigDaoFactory()
        elif factory_type == DCConfigFactoryType.TEXT_FACTORY:
            return TextDCConfigDaoFactory()
        else:
            raise ValueError("Invalid DC Config DAO Factory Type")

    @abc.abstractmethod
    def get_connection_dao(self):
        raise NotImplementedError("Abstract method 'get_connection_dao' needs implementation.")


class JsonDCConfigDaoFactory(DCConfigDaoFactory):
    """ Class JsonDCConfigDaoFactory is the specific DCConfigDaoFactory class for Json DAO factory.

    This is responsible for creating Json configuration specific DAO factory.

    This will create all Json DAOs required in Database Connector.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        pass                        

    def get_connection_dao(self):
        """ Returns Json connection DAO.

        This method is responsible for creating Json connection DAO object.

        Args:
            Not Applicable.
        Returns:
            JsonConnectionDao: Json DAO object for connection configuration.
        Raises:
            Not Applicable.
        """         
        return JsonConnectionDao()


class YamlDCConfigDaoFactory(DCConfigDaoFactory):
    """ Class YamlDCConfigDaoFactory is the specific DCConfigDaoFactory class for Yaml DAO factory.

    This is responsible for creating Yaml configuration specific DAO factory.

    This will create all Yaml DAOs required in Database Connector.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        pass                        

    def get_connection_dao(self):
        """ Returns Yaml connection DAO.

        This method is responsible for creating Yaml connection DAO object.

        Args:
            Not Applicable.
        Returns:
            YamlConnectionDao: Yaml DAO object for connection configuration.
        Raises:
            Not Applicable.
        """         
        return YamlConnectionDao()


class IniDCConfigDaoFactory(DCConfigDaoFactory):
    """ Class IniDCConfigDaoFactory is the specific DCConfigDaoFactory class for Ini DAO factory.

    This is responsible for creating Ini configuration specific DAO factory.

    This will create all Ini DAOs required in Database Connector.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        pass                        

    def get_connection_dao(self):
        """ Returns Ini connection DAO.

        This method is responsible for creating Ini connection DAO object.

        Args:
            Not Applicable.
        Returns:
            IniConnectionDao: Ini DAO object for connection configuration.
        Raises:
            Not Applicable.
        """         
        return IniConnectionDao()


class XmlDCConfigDaoFactory(DCConfigDaoFactory):
    """ Class XmlDCConfigDaoFactory is the specific DCConfigDaoFactory class for Xml DAO factory.

    This is responsible for creating Xml configuration specific DAO factory.

    This will create all Xml DAOs required in Database Connector.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        pass                        

    def get_connection_dao(self):
        """ Returns Xml connection DAO.

        This method is responsible for creating Xml connection DAO object.

        Args:
            Not Applicable.
        Returns:
            XmlConnectionDao: Xml DAO object for connection configuration.
        Raises:
            Not Applicable.
        """         
        return XmlConnectionDao()


class TextDCConfigDaoFactory(DCConfigDaoFactory):
    """ Class TextDCConfigDaoFactory is the specific DCConfigDaoFactory class for Text DAO factory.

    This is responsible for creating Text configuration specific DAO factory.

    This will create all Text DAOs required in Database Connector.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self):
        pass                        

    def get_connection_dao(self):
        """ Returns Text connection DAO.

        This method is responsible for creating Text connection DAO object.

        Args:
            Not Applicable.
        Returns:
            TextConnectionDao: Text DAO object for connection configuration.
        Raises:
            Not Applicable.
        """         
        return TextConnectionDao()