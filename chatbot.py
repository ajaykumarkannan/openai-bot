#!/usr/bin/env python3
import openai
import re
from keys import openai_api_key


def main():
    openai.api_key = openai_api_key
    model = "text-davinci-003"
    max_token_value = 3000
    print('Welcome to a simple OpenAI CLI chat bot. Type "exit" or "quit" to quit')
    while 1:
        try:
            prompt_value = input("> ")
            if prompt_value.lower() == "exit":
                print("Thanks for playing! Exiting")
                exit()
            elif prompt_value.lower() == "quit":
                print("Thanks for playing! Exiting")
                exit()

            # create a completion
            completion = openai.Completion.create(
                engine=model, prompt=prompt_value, max_tokens=max_token_value
            )

            # print the completion
            print(completion.choices[0].text.strip())
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
