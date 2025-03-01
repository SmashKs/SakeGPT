from base64 import b64encode
from abc import abstractmethod


class OnlineAIClient:

    def __init__(self):
        self._model = ''
        self._api_token = ''

    def send_image_file(self, path, prompt):
        with open(path, 'rb') as image_flip:
            image = b64encode(image_flip.read()).decode('utf-8')
            return self.send_image(image, prompt)

    def send_image_b64(self, content, prompt):
        return self.send_image(content, prompt)

    @abstractmethod
    def send_message(self, prompt):
        pass

    @abstractmethod
    def send_image(self, img, prompt):
        pass

    @abstractmethod
    def set_role(self, prompt):
        pass

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def api_token(self):
        return self._api_token
