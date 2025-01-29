from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_token, model='gpt-3.5-turbo'):
        self._api_token = api_token
        self._model = model
        if self._api_token is None:
            raise ValueError('API token must be provided or set as OPENAI_API_TOKEN environment variable')

        self.client = OpenAI(api_key=self._api_token)
        self.conversation_history = []

    def set_role(self, prompt):
        self.clear_history()
        self.conversation_history.append({
            'role': 'system',
            'content': prompt
        })

    def send_message(self, message):
        try:
            self.conversation_history.append({
                'role': 'user',
                'content': message
            })

            response = self.client.chat.completions.create(
                model=self._model,
                messages=self.conversation_history
            )

            assistant_response = response.choices[0].message.content
            self.conversation_history.append({
                'role': 'assistant',
                'content': assistant_response
            })

            return assistant_response
        except Exception as error:
            return f"Error: {str(error)}"

    def clear_history(self):
        self.conversation_history.clear()

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def api_token(self):
        return self._api_token
