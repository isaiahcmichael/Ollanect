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
Ollanect
Copyright (C) 2025 Isaiah Michael

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions. See the GNU General Public License v3.0
for more details: <https://www.gnu.org/licenses/>.
"""

if "--license" in sys.argv:
    print(LICENSE_TEXT)
    sys.exit(0)

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
    lines = infoFile.readlines()
    if lines:
        inputServer = lines[0]
    infoFile.close()
    return inputServer

inputServer = getServer(infoFile)

apiURL = f"http://{inputServer}/api/"

def getModel():
    try:
        # Send a GET request to retrieve available models
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
        quit()

    while True:
        print('\nWhich model do you want?')
        inputModel = input('> ').strip()
        if inputModel in base_models:
            return base_models[inputModel]  # Return the full model name
        if inputModel == 'exit':
            exit()
        print("Invalid model. Please enter a valid model name from the list.")

def getPrompt():
    print('Prompt:')
    inputPrompt = input('> ')
    return inputPrompt

inputModel = getModel()
inputPrompt = getPrompt()

payload = {
    "model": inputModel,
    "prompt": inputPrompt,
    "stream": True  # Streaming mode
}

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
