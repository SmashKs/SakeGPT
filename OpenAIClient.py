from openai import OpenAI
from OnlineAIClient import OnlineAIClient


class OpenAIClient(OnlineAIClient):
    def __init__(self, api_token, model='gpt-3.5-turbo'):
        super().__init__()
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

    def send_image(self, image, prompt):
        self.conversation_history.append({
            'role': 'user',
            'content': [
                {'type': 'text', 'text': prompt},
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f"data:image/jpeg;base64,{image}"
                    }
                }
            ],
            'detail': 'auto'
        })

        response = self.client.chat.completions.create(
            model='gpt-4o-mini',
            messages=self.conversation_history,
            max_tokens=300
        )

        assistant_response = response.choices[0].message.content
        self.conversation_history.append({
            'role': 'assistant',
            'content': assistant_response
        })

        return assistant_response

    def send_message(self, prompt):
        try:
            self.conversation_history.append({
                'role': 'user',
                'content': prompt
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
