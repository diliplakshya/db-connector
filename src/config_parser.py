import json

class ConnectionInfo:
    def __init__(self):
        self._host = None
        self._name = None
        self._user = None
        self._password = None

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

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

    def __iter__(self):
        yield self._host
        yield self._name
        yield self._user
        yield self._password


class DBConfigParser:
    CONFIG_PATH = "/home/local/Documents/DBConnector/config/db_info.json"

    def __init__(self):
        self.connection_info = ConnectionInfo()
        self.info = None

        self.load_config()
        self.set_info()

    def load_config(self):
        with open(DBConfigParser.CONFIG_PATH) as config_object:
            self.info = json.load(config_object)

    def set_info(self):
        self.connection_info.host = self.info["host"]
        self.connection_info.name = self.info["name"]
        self.connection_info.user = self.info["user"]
        self.connection_info.password = self.info["password"]

    def get_connection_info(self):
        return tuple(self.connection_info)

ob = DBConfigParser()
res = ob.get_connection_info()
print(res)
