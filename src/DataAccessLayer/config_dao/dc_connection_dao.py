#!/usr/bin/python3.4

"""DAO for Database Connector configuration.

DILIP KUMAR SHARMA CONFIDENTIAL & PROPRIETARY

@file dc_connection_dao.py
@author Dilip Kumar Sharma
@copyright Dilip Kumar Sharma
@date 14th Feb 2019

About; -
--------
    This python module is responsible for creating DAO for database connection configuration.
    It is used to fetch connection information from configuration file.

Data Source; -
--------------
    It could be any type of configuration file.

DAL/DAO; -
----------
    DAO (Data Access Object) is part of DAL (Data Acceess Layer) which helps us to 
    create a loose coupling between Core logic and data source (Config).

    For each type of data source, we will have one DAO representing that data source.

Loose Coupling; -
-----------------
    Whene we use Database Connector in other projects then we do not need to change the
    core logic, we just need to update DAL or DAOs according to the configuration types of that project.

    This way the core logic is segregated 
    from the data source and it does not talk to data source directly.

Design Pattern; -
-----------------
    DAOs are created by a DAO Factory.
    Both DAO factory and DAOs are part of Abstract factory design pattern.

Transfer Object; -
------------------
    Each such DAO will return a Transfer object to core logic.

    The class structure of this Transfer object will remain same irrespective of
    the configuration used or the project in which this Database Connector is used.

    Core logic is tightly coupled with this Transfer object and fully
    dependent on this transfer object. 
    
    Whenever we use Database Connector to some other projects or whenever we change 
    the data source within the same project, then we must use the same 
    transfer object to avoid changing the core logic.

Working; -
----------
    This DAO will talk to configuration file and fetch information from configuration file.

    Each of configuration types will have its own DAO class responsible for writing piece of
    code to fetch information from configuration file.
    
    For example, for JSON configuration we will have one DAO class, while for YAML configuration 
    we will have separate DAO class and so on.

Uses; -
-------
    This DAO is used in Database Connector's core logic.

Reference; -
------------
    

"""

# #############################################################################
# #######                      CHANGE RECORD                          #########
# -----------------------------------------------------------------------------
# Date (DD-MM-YY)  |  Author                    |   Change
# -----------------------------------------------------------------------------
# 14-02-19            Dilip Kumar Sharma            New file added.
#
#                                                                              
# #############################################################################


import abc
import json
import os
# TO DO : Need to import package for parsing Yaml, INI, XML Configuration


class MySqlConnectionConfig:
    """ Class MySqlConnectionConfig is the transfer object for MySql database connection configuration.
    
    This transfer object represents the connection information fetched from configuration file.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self, database, host, port, name, user, password):
        self._database  =   database
        self._host      =   host
        self._port      =   port
        self._name      =   name
        self._user      =   user
        self._password  =   password               

    @property
    def database(self):       
        return self._database
    
    @database.setter
    def database(self, database):
        self._database = database 

    @property
    def host(self):       
        return self._host
    
    @host.setter
    def host(self, host):
        self._host = host 

    @property
    def port(self):       
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port 

    @property
    def name(self):       
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name 

    @property
    def user(self):       
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user 

    @property
    def password(self):       
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password


class OracleConnectionConfig:
    """ Class OracleConnectionConfig is the transfer object for Oracle database connection configuration.
    
    This transfer object represents the connection information fetched from configuration file.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    def __init__(self, database, host, port, service_name, name, user, password):
        self._database      =   database
        self._host          =   host
        self._port          =   port
        self._service_name  =   service_name
        self._name          =   name
        self._user          =   user
        self._password      =   password               

    @property
    def database(self):       
        return self._database
    
    @database.setter
    def database(self, database):
        self._database = database 

    @property
    def host(self):       
        return self._host
    
    @host.setter
    def host(self, host):
        self._host = host 

    @property
    def port(self):       
        return self._port
    
    @port.setter
    def port(self, port):
        self._port = port 

    @property
    def service_name(self):       
        return self._service_name
    
    @service_name.setter
    def service_name(self, service_name):
        self._service_name = service_name 

    @property
    def name(self):       
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name 

    @property
    def user(self):       
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user 

    @property
    def password(self):       
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password


class ConnectionDao:
    """ Abstract class ConnectionDao is base class for specific Connection DAO.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """
    __metaclass__ = abc.ABCMeta

    CONN_CFG_ENV_VAR      =   "DC_CONN_CFG"

    def __init__(self):
        pass

    def read_env(self):
        return os.getenv(ConnectionDao.CONN_CFG_ENV_VAR, None)        # Returns None if key does not exist

    @abc.abstractmethod
    def get_file_path(self):
        raise NotImplementedError("Abstract method 'get_file_path' needs implementation.")

    @abc.abstractmethod
    def read_configuration(self):
        raise NotImplementedError("Abstract method 'read_configuration' needs implementation.")

    @abc.abstractmethod
    def get_mysql_connection_config(self):
        raise NotImplementedError("Abstract method 'get_mysql_connection_config' needs implementation.")

    @abc.abstractmethod
    def get_oracle_connection_config(self):
        raise NotImplementedError("Abstract method 'get_oracle_connection_config' needs implementation.")


class JsonConnectionDao(ConnectionDao):
    """ Class JsonConnectionDao is the specific DAO class for Json connection configuration.

    This is responsible for fetching connection information from Json configuration.

    This class returns a Transfer object to core logic.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    CONN_CFG_DEF_PATH = "/home/aspect/release/conf/DBConnector/connection.json"

    def __init__(self):
        self.json_data = None
        self.read_configuration()     

    def get_file_path(self):
        """ To read Json connection configuration file path.

        If environment variable is not set then we use default file path.

        Args:
            Not Applicable.
        Returns:
            path: Json configuration file path.
        Raises:
            Not Applicable.
        """        
        path = self.read_env()

        if path is None:
            path = JsonConnectionDao.CONN_CFG_DEF_PATH

        return path

    def read_configuration(self):
        """ Reads Json logging configuration

        This method is responsible for reading Json logging configuration.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            ValueError: If Json logging configuration file path is invalid.
        """
        path = self.get_file_path()

        if os.path.exists(path):
            with open(path) as json_file_object:
                self.json_data = json.load(json_file_object)
        else:
            raise ValueError("Connection configuration file path '{}' is invalid.".format(path))                

    def get_mysql_connection_config(self):
        """ Returns MySql Json connection configuration data.

        Args:
            Not Applicable.
        Returns:
            MySqlConnectionConfig: Transfer Object representing Json connection information.
        Raises:
            Not Applicable.
        """
        mysql_data  =       self.json_data["MySql"]

        database    =       mysql_data["Database"]
        host        =       mysql_data["Host"]
        port        =       mysql_data["Port"]
        name        =       mysql_data["Name"]
        user        =       mysql_data["User"]
        password    =       mysql_data["Password"]

        return MySqlConnectionConfig(database, host, port, name, user, password)

    def get_oracle_connection_config(self):
        """ Returns Oracle Json connection configuration data.

        Args:
            Not Applicable.
        Returns:
            OracleConnectionConfig: Transfer Object representing Oracle Json connection information.
        Raises:
            Not Applicable.
        """
        oracle_data     =       self.json_data["Oracle"]

        database        =       oracle_data["Database"]
        host            =       oracle_data["Host"]
        port            =       oracle_data["Port"]
        service_name    =       oracle_data["ServiceName"]
        name            =       oracle_data["Name"]
        user            =       oracle_data["User"]
        password        =       oracle_data["Password"]

        return OracleConnectionConfig(database, host, port, service_name, name, user, password)


class YamlConnectionDao(ConnectionDao):
    """ Class YamlConnectionDao is the specific DAO class for Yaml connection configuration.

    This is responsible for fetching connection information from Yaml configuration.

    This class returns a Transfer object to core logic.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    CONN_CFG_DEF_PATH = "/home/aspect/release/conf/DBConnector/connection.yaml"

    def __init__(self):
        self.yaml_data = None
        self.read_configuration()     

    def get_file_path(self):
        """ To read Yaml connection configuration file path.

        If environment variable is not set then we use default file path.

        Args:
            Not Applicable.
        Returns:
            path: Yaml configuration file path.
        Raises:
            Not Applicable.
        """        
        path = self.read_env()

        if path is None:
            path = YamlConnectionDao.CONN_CFG_DEF_PATH

        return path

    def read_configuration(self):
        """ Reads Yaml logging configuration

        This method is responsible for reading Yaml logging configuration.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            ValueError: If Yaml logging configuration file path is invalid.
        """
        path = self.get_file_path()

        if os.path.exists(path):
            pass # TO DO : Add code to read file
        else:
            raise ValueError("Connection configuration file path '{}' is invalid.".format(path))                

    def get_mysql_connection_config(self):
        """ Returns MySql Yaml connection configuration data.

        Args:
            Not Applicable.
        Returns:
            MySqlConnectionConfig: Transfer Object representing Yaml connection information.
        Raises:
            Not Applicable.
        """

        database    =       None # TO DO : To be filled
        host        =       None # TO DO : To be filled
        name        =       None # TO DO : To be filled
        port        =       None # TO DO : To be filled
        user        =       None # TO DO : To be filled
        password    =       None # TO DO : To be filled

        return MySqlConnectionConfig(database, host, port, name, user, password)

    def get_oracle_connection_config(self):
        """ Returns Oracle Yaml connection configuration data.

        Args:
            Not Applicable.
        Returns:
            OracleConnectionConfig: Transfer Object representing Oracle Yaml connection information.
        Raises:
            Not Applicable.
        """
        database        =       None # TO DO : To be filled
        host            =       None # TO DO : To be filled
        name            =       None # TO DO : To be filled
        port            =       None # TO DO : To be filled
        service_name    =       None # TO DO : To be filled
        user            =       None # TO DO : To be filled
        password        =       None # TO DO : To be filled

        return OracleConnectionConfig(database, host, port, service_name, name, user, password)


class IniConnectionDao(ConnectionDao):
    """ Class IniConnectionDao is the specific DAO class for Ini connection configuration.

    This is responsible for fetching connection information from Ini configuration.

    This class returns a Transfer object to core logic.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    CONN_CFG_DEF_PATH = "/home/aspect/release/conf/DBConnector/connection.ini"

    def __init__(self):
        self.ini_data = None
        self.read_configuration()     

    def get_file_path(self):
        """ To read Ini connection configuration file path.

        If environment variable is not set then we use default file path.

        Args:
            Not Applicable.
        Returns:
            path: Ini configuration file path.
        Raises:
            Not Applicable.
        """        
        path = self.read_env()

        if path is None:
            path = IniConnectionDao.CONN_CFG_DEF_PATH

        return path

    def read_configuration(self):
        """ Reads Ini logging configuration

        This method is responsible for reading Ini logging configuration.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            ValueError: If Ini logging configuration file path is invalid.
        """
        path = self.get_file_path()

        if os.path.exists(path):
            pass # TO DO : Add code to read file
        else:
            raise ValueError("Connection configuration file path '{}' is invalid.".format(path))                

    def get_mysql_connection_config(self):
        """ Returns MySql Ini connection configuration data.

        Args:
            Not Applicable.
        Returns:
            MySqlConnectionConfig: Transfer Object representing Ini connection information.
        Raises:
            Not Applicable.
        """

        database    =       None # TO DO : To be filled
        host        =       None # TO DO : To be filled
        name        =       None # TO DO : To be filled
        port        =       None # TO DO : To be filled
        user        =       None # TO DO : To be filled
        password    =       None # TO DO : To be filled

        return MySqlConnectionConfig(database, host, port, name, user, password)

    def get_oracle_connection_config(self):
        """ Returns Oracle Ini connection configuration data.

        Args:
            Not Applicable.
        Returns:
            OracleConnectionConfig: Transfer Object representing Oracle Ini connection information.
        Raises:
            Not Applicable.
        """
        database        =       None # TO DO : To be filled
        host            =       None # TO DO : To be filled
        name            =       None # TO DO : To be filled
        port            =       None # TO DO : To be filled
        service_name    =       None # TO DO : To be filled
        user            =       None # TO DO : To be filled
        password        =       None # TO DO : To be filled

        return OracleConnectionConfig(database, host, port, service_name, name, user, password)


class XmlConnectionDao(ConnectionDao):
    """ Class XmlConnectionDao is the specific DAO class for Xml connection configuration.

    This is responsible for fetching connection information from Xml configuration.

    This class returns a Transfer object to core logic.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    CONN_CFG_DEF_PATH = "/home/aspect/release/conf/DBConnector/connection.xml"

    def __init__(self):
        self.xml_data = None
        self.read_configuration()     

    def get_file_path(self):
        """ To read Xml connection configuration file path.

        If environment variable is not set then we use default file path.

        Args:
            Not Applicable.
        Returns:
            path: Xml configuration file path.
        Raises:
            Not Applicable.
        """        
        path = self.read_env()

        if path is None:
            path = XmlConnectionDao.CONN_CFG_DEF_PATH

        return path

    def read_configuration(self):
        """ Reads Xml logging configuration

        This method is responsible for reading Xml logging configuration.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            ValueError: If Xml logging configuration file path is invalid.
        """
        path = self.get_file_path()

        if os.path.exists(path):
            pass # TO DO : Add code to read file
        else:
            raise ValueError("Connection configuration file path '{}' is invalid.".format(path))                

    def get_mysql_connection_config(self):
        """ Returns MySql Xml connection configuration data.

        Args:
            Not Applicable.
        Returns:
            MySqlConnectionConfig: Transfer Object representing Xml connection information.
        Raises:
            Not Applicable.
        """

        database    =       None # TO DO : To be filled
        host        =       None # TO DO : To be filled
        name        =       None # TO DO : To be filled
        port        =       None # TO DO : To be filled
        user        =       None # TO DO : To be filled
        password    =       None # TO DO : To be filled

        return MySqlConnectionConfig(database, host, port, name, user, password)

    def get_oracle_connection_config(self):
        """ Returns Oracle Xml connection configuration data.

        Args:
            Not Applicable.
        Returns:
            OracleConnectionConfig: Transfer Object representing Oracle Xml connection information.
        Raises:
            Not Applicable.
        """
        database        =       None # TO DO : To be filled
        host            =       None # TO DO : To be filled
        name            =       None # TO DO : To be filled
        port            =       None # TO DO : To be filled
        service_name    =       None # TO DO : To be filled
        user            =       None # TO DO : To be filled
        password        =       None # TO DO : To be filled

        return OracleConnectionConfig(database, host, port, service_name, name, user, password)


class TextConnectionDao(ConnectionDao):
    """ Class TextConnectionDao is the specific DAO class for Text connection configuration.

    This is responsible for fetching connection information from Text configuration.

    This class returns a Transfer object to core logic.
    
    Args:
        Not Applicable.
    Returns:
        Not Applicable.
    Raises:
        Not Applicable.
    """

    CONN_CFG_DEF_PATH = "/home/aspect/release/conf/DBConnector/connection.txt"

    def __init__(self):
        self.text_data = None
        self.read_configuration()     

    def get_file_path(self):
        """ To read Text connection configuration file path.

        If environment variable is not set then we use default file path.

        Args:
            Not Applicable.
        Returns:
            path: Text configuration file path.
        Raises:
            Not Applicable.
        """        
        path = self.read_env()

        if path is None:
            path = TextConnectionDao.CONN_CFG_DEF_PATH

        return path

    def read_configuration(self):
        """ Reads Text logging configuration

        This method is responsible for reading Text logging configuration.

        Args:
            Not Applicable.
        Returns:
            Not Applicable.
        Raises:
            ValueError: If Text logging configuration file path is invalid.
        """
        path = self.get_file_path()

        if os.path.exists(path):
            pass # TO DO : Add code to read file
        else:
            raise ValueError("Connection configuration file path '{}' is invalid.".format(path))                

    def get_mysql_connection_config(self):
        """ Returns MySql Text connection configuration data.

        Args:
            Not Applicable.
        Returns:
            MySqlConnectionConfig: Transfer Object representing Text connection information.
        Raises:
            Not Applicable.
        """

        database    =       None # TO DO : To be filled
        host        =       None # TO DO : To be filled
        name        =       None # TO DO : To be filled
        port        =       None # TO DO : To be filled
        user        =       None # TO DO : To be filled
        password    =       None # TO DO : To be filled

        return MySqlConnectionConfig(database, host, port, name, user, password)

    def get_oracle_connection_config(self):
        """ Returns Oracle Text connection configuration data.

        Args:
            Not Applicable.
        Returns:
            OracleConnectionConfig: Transfer Object representing Oracle Text connection information.
        Raises:
            Not Applicable.
        """
        database        =       None # TO DO : To be filled
        host            =       None # TO DO : To be filled
        name            =       None # TO DO : To be filled
        port            =       None # TO DO : To be filled
        service_name    =       None # TO DO : To be filled
        user            =       None # TO DO : To be filled
        password        =       None # TO DO : To be filled

        return OracleConnectionConfig(database, host, port, service_name, name, user, password)