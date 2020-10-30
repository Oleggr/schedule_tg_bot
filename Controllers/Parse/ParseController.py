import json
import requests
from abc import abstractmethod

from Controllers.Log.LogController import LogController
from Controllers.File.FileController import FileController


class ParseController:

    logger = LogController()

    def writeToJsonFile(self, file_name: str, group_name: str):
        self.logger.info(f"Parser {self.__class__.__name__} started for {group_name}")
        json = self.makeJson(group_name)
        filepath = f'{file_name}.json'
        FileController.writeToFile(filepath, json)

    def makeJson(self, group_name: str):
        self.logger.info(f"Parser {self.__class__.__name__} started for {group_name}")
        return str(self._parse(group_name))

    def _getUrl(self, url):
        try:
            response = requests.get(url, timeout=30)
        except requests.Timeout:
            self.logger.alert(f'Timeout error, url: {url}')
            return None
        except requests.HTTPError as err:
            code = err.response.status_code
            self.logger.alert(f'Error url: {url}, code: {code}')
            return None
        except requests.RequestException:
            self.logger.alert(f'Downloading error url: {url}')
            return None
        else:
            return response

    @abstractmethod
    def _parse(self, group_name: str):
        pass

    @abstractmethod
    def __str__(self):
        pass
