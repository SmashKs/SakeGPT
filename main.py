from OpenAIClient import OpenAIClient
import os


def main():
    client = OpenAIClient(os.getenv('OPENAI_API_TOKEN'))
    client.set_role('you are an alcohol vendor, your response must follow this rule. Vendor: [], Product Name: []')
    print(client.send_image_file("3236fdf6-6ee8-4121-8034-c603c5b72d9d.png", "what is this?"))


if __name__ == '__main__':
    main()
