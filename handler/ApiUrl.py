from config import RemoteServerConfig


class ApiUrl:
    decrypt = RemoteServerConfig.host + "/api/decrypt"
    result = RemoteServerConfig.host + "/api/result"
    top_secret_data = RemoteServerConfig.host + "/api/top-secret-data"
