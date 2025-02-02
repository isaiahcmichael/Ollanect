#!/bin/python3

# This file is part of Ollanect.
#
# Ollanect is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ollanect is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ollanect. If not, see <https://www.gnu.org/licenses/>.

import requests
import json
import platform
import os
import sys

LICENSE_TEXT = """
Ollanect - Version 0.1.5
Copyright (C) 2025 Isaiah Michael

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the GNU General Public License v3.0
for more details: <https://www.gnu.org/licenses/>.
"""

HELP_TEXT = """
Ollanect Help:

Usage: ollanect [options]
Options:
--help - Shows this menu
--license - Shows Ollanect's license
--one-prompt - Does not continue chat
--model or -m - Defines Model (example: --model phi4:latest)
--prompt -m - Specifies Prompt (example --prompt 'When was GitHub created?')
"""

HELP_TEXT_CHAT = """
Ollanect Chat Help:

Type your prompt and press Enter to get a response.
Options:
/help or /? - Shows this menu
/exit - Exits the chat
"""

if "--help" in sys.argv:
    print(HELP_TEXT)
    sys.exit(0)
elif '--help-chat' in sys.argv:
    print(HELP_TEXT_CHAT)
    sys.exit(0)
else:
    pass

if "--license" in sys.argv:
    print(LICENSE_TEXT)
    sys.exit(0)

# Finds the config file for Ollanect. If not found, the setup script runs
try:
    scriptLocation = os.path.dirname(os.path.realpath(__file__))
    infoFile = open(f'{scriptLocation}/config/serverInfo', 'r')
except FileNotFoundError:
    systemOS = platform.system()
    if systemOS == 'Linux':
        scriptLocation = os.path.dirname(os.path.realpath(__file__))
        os.system(f'chmod +x {scriptLocation}/setup-Linux')
        os.system(f'sh {scriptLocation}/setup-Linux')
        quit()

def getServer(infoFile):
    # Gets the server info
    lines = infoFile.readlines()
    if lines:
        inputServer = lines[0]
    infoFile.close()
    return inputServer

inputServer = getServer(infoFile)

# Defines the URL for the Ollama Server
apiURL = f"http://{inputServer}/api/"

def getModel():
    if "-m" in sys.argv:
        mFlag = sys.argv.index("-m")
        if mFlag + 1 < len(sys.argv):
            inputModel = sys.argv[mFlag + 1]
            return inputModel
        else:
            print("Flag -m expected one argument, got 0.")
    elif "--model" in sys.argv:
        mOption = sys.argv.index("--model")
        if mOption + 1 < len(sys.argv):
            inputModel = sys.argv[mOption + 1]
            return inputModel
        else:
            print("Option --model expected one argument, got 0.")
    else:
        # Gets the info for the model used, if not already specified
        try:
            # Sends a response to get available models (GET)
            response = requests.get(f'{apiURL}tags')
            response.raise_for_status()  # Raise an error for HTTP errors

            # Parse the JSON response
            models = response.json().get("models", [])
            model_names = [model["name"] for model in models]

            base_models = {}
            for name in model_names:
                base_name = name.split(":")[0]  # Get the name before ":"
                if base_name not in base_models or name.endswith(":latest"):
                    base_models[base_name] = name  # Prefer ":latest" if available

            # Print the model names
            print("Available models on Ollama server:")
            for base_name in base_models:
                print(base_name)

        except requests.exceptions.RequestException as e:
            print("Error connecting to Ollama server:", e)
            sys.exit(0)

        while True:
            print('\nWhich model do you want?')
            inputModel = input('> ').strip()
            if inputModel in base_models:
                return base_models[inputModel]  # Return the full model name
            if inputModel == 'exit':
                exit()
            print("Invalid model. Please enter a valid model name from the list.")

def getPrompt():
    # Gets the prompt if not already specified
    print('Prompt:')
    inputPrompt = input('> ')
    return inputPrompt

inputModel = getModel()

if "--one-prompt" in sys.argv:
    chat = False
else:
    chat = True

def getData(apiURL,inputModel,chat):
    # Gets the prompt if already specified
    if "-p" in sys.argv:
        pFlag = sys.argv.index("-p")
        if pFlag + 1 < len(sys.argv):
            inputPrompt = sys.argv[pFlag + 1]
            chat = False
        else:
            print("Flag -p expected 1 element, got 0")
    elif '--prompt' in sys.argv:
        pOption = sys.argv.index("--prompt")
        if pOption + 1 < len(sys.argv):
            inputPrompt = sys.argv[pOption + 1]
            chat = False
        else:
            print("Option --prompt expected 1 element, got 0")
    else:
        inputPrompt = getPrompt()
    
    # Chat options
    if inputPrompt == '/exit':
        print('\nExiting!')
        sys.exit(0)
    elif inputPrompt in ['/help', '/?']:
        print(HELP_TEXT_CHAT)
        sys.exit(0)
    else:
        pass

    # Defines what is sent to the server and sends it (requests.post)
    payload = {
        "model": inputModel,
        "prompt": inputPrompt,
        "stream": True  # Streaming mode
    }
    try:
        with requests.post(f'{apiURL}generate', json=payload, stream=True) as response:
            for line in response.iter_lines():
                if line:
                    try:
                        # Decode JSON line
                        data = json.loads(line.decode("utf-8"))

                        # Extract and print the model's response
                        print(data.get("response", ""), end="", flush=True)

                    except json.JSONDecodeError as e:
                        print("\nError decoding JSON:", e)
                        print("Raw line:", line.decode("utf-8"))
        print('')
        if chat == True:
            getData(apiURL,inputModel,chat)
        elif chat == False:
            sys.exit(0)
        else:
            print('Unknown error!')
            sys.exit(0)
        print('')
    except KeyboardInterrupt:
        print('\nExiting!')
        sys.exit(0)

getData(apiURL,inputModel,chat)

# End of Ollanect File.