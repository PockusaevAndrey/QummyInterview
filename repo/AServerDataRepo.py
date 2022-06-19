from abc import ABCMeta, abstractmethod

from entity.db.ServerData import ServerData


class AServerDataRepo(metaclass=ABCMeta):
    @abstractmethod
    def add_encrypted(self, encrypted_text: str) -> None: pass

    @abstractmethod
    def add_decrypted(self, encrypted_text: str, decrypted_text: str) -> None: pass
