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
import zipfile

LICENSE_TEXT = """
Ollanect - Version 0.3
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
--help or -h - Shows this menu
--license - Shows Ollanect's license
--one-prompt - Does not continue chat
--model or -m - Defines Model (example: --model phi4:latest)
--prompt or -p - Specifies Prompt (example --prompt 'When was GitHub created?')
--version or -v - Prints the version of Ollanect
--file or -f - Uploads a file
--addon or -a - Uses an addon
-1, -2, -3, -4, -5 - Uses a different server file (by default, -1 is the flag used by Ollanect)
"""

HELP_TEXT_CHAT = """
Ollanect Chat Help:

Type your prompt and press Enter to get a response.
Options:
/help or /? - Shows this menu
/exit, /quit, or /bye - Exits the chat
/file or /f - Uploads a file
"""

if "--help" in sys.argv:
    print(HELP_TEXT)
    sys.exit(0)
elif '--help-chat' in sys.argv:
    print(HELP_TEXT_CHAT)
    sys.exit(0)
elif '-h' in sys.argv:
    print(HELP_TEXT)
    sys.exit(0)
else:
    pass

def versionCheck():
    githubReleases = 'https://api.github.com/repos/isaiahcmichael/Ollanect/releases/latest'
    githubResponse = requests.get(githubReleases)
    currentVersion = 'v0.3'

    def makeNumber(version: str):
        return tuple(map(int, version.lstrip('v').split('.')))

    try:
        if githubResponse.status_code == 200:
            githubData = githubResponse.json()
            latestVersion = githubData['tag_name']
            currentVersionT = makeNumber(currentVersion)
            latestVersionT = makeNumber(latestVersion)
            if latestVersionT > currentVersionT:
                print(f'New version available: {latestVersion}')
            elif latestVersionT < currentVersionT:
                print('You are using a development version of Ollanect.')
            else:
                print(f'You are using the latest version of Ollanect. ({currentVersion})')
    except Exception as e:
        print(f'Error checking for updates: {e}')

if "--license" in sys.argv:
    print(LICENSE_TEXT)
    sys.exit(0)
elif '--version' in sys.argv:
    print(LICENSE_TEXT)
    versionCheck()
    sys.exit(0)
elif '-v' in sys.argv:
    print(LICENSE_TEXT)
    versionCheck()
    sys.exit(0)

# Addon support
if '--addon' in sys.argv:
    addonOption = sys.argv.index('--addon')
    if addonOption + 1 < len(sys.argv):
        addon = sys.argv[addonOption + 1]
    else:
        print("Option --addon expected two arguments, got 0.")
elif '-a' in sys.argv:
    addonFlag = sys.argv.index('-a')
    if addonFlag + 1 < len(sys.argv):
        addon = sys.argv[addonFlag + 1]
    else:
        print("Flag -a expected two arguments, got 0.")
else:
    addon = False

if addon == False:
    pass
elif addon == 'install':
    addonInstall = sys.argv.index('install')
    if addonInstall + 1 < len(sys.argv):
        addonURL = sys.argv[addonInstall + 1]
        URLcheck = requests.get(addonURL)
        scriptLocation = os.path.dirname(os.path.realpath(__file__))
        scriptParent = os.path.dirname(scriptLocation)
        if URLcheck.status_code == 200:
            fileName = addonURL.split('/')[-1]
            addonDirectory = os.path.join(scriptParent, 'addons', fileName)
            os.makedirs(addonDirectory, exist_ok=True)
            infoFile = os.path.join(addonDirectory, fileName)
            with open(infoFile, 'wb') as file:
                file.write(URLcheck.content)
                lines = infoFile.readlines()
                if lines:
                    zipCheck = requests.get(lines[1])
                    if zipCheck.status_code == 200:
                        zipPath = f'{addonDirectory}/{fileName}.zip'
                        with open(zipPath, 'wb') as zipFile:
                            zipFile.write(zipCheck.content)
                        with zipfile.ZipFile(zipPath, 'r') as zipFileWritten:
                            zipFileWritten.extractall(addonDirectory)
                            print(f'Addon {fileName} installed successfully!')
                            quit()
    else:
        print("Option --addon install expected one argument, got 0.")
        quit()
elif addon == 'remove':
    addonRemove = sys.argv.index('remove')
    if addonRemove + 1 < len(sys.argv):
        addonName = sys.argv[addonRemove + 1]
        scriptLocation = os.path.dirname(os.path.realpath(__file__))
        scriptParent = os.path.dirname(scriptLocation)
        addonDirectory = os.path.join(scriptParent, 'addons', addonName)
        if os.path.exists(addonDirectory):
            os.remove(addonDirectory)
            print(f'Addon {addonName} removed successfully!')
            quit()
        else:
            print(f'Addon {addonName} does not exist.')
            quit()
    else:
        print("Option --addon remove expected one argument, got 0.")
        quit()
elif addon == 'list':
    scriptLocation = os.path.dirname(os.path.realpath(__file__))
    scriptParent = os.path.dirname(scriptLocation)
    addonsDirectory = os.path.join(scriptParent, 'addons')
    if os.path.exists(addonsDirectory):
        print('Addons:')
        for file in os.listdir(addonsDirectory):
            print(file)
        quit()
    else:
        print('No addons found.')
        quit()
elif addon == 'run':
    addonRun = sys.argv.index('run')
    if addonRun + 1 < len(sys.argv):
        addonName = sys.argv[addonRun + 1]
        scriptLocation = os.path.dirname(os.path.realpath(__file__))
        scriptParent = os.path.dirname(scriptLocation)
        addonDirectory = os.path.join(scriptParent, 'addons', addonName)
        if os.path.exists(addonDirectory):
            addonScript = os.path.join(addonDirectory, 'main.py')
            os.system(f'python3 {addonScript}')
            quit()
        else:
            print(f'Addon {addonName} does not exist.')
            quit()
    else:
        print("Option --addon run expected one argument, got 0.")
        quit()
else:
    print(f'Option --addon does not have option {addon}.')
    quit()

# Finds the config file for Ollanect. If not found, the setup script runs
systemOS = platform.system()

def getServer():
    # Gets the server info

    # Checks if the user specified a server file
    if '-1' in sys.argv:
        serverFile = "Ollanect/serverInfo"
        altFile = False
    elif '-2' in sys.argv:
        serverFileTag = '-2'
        serverFile = "Ollanect/serverInfo-2"
        altFile = True
    elif '-3' in sys.argv:
        serverFileTag = '-3'
        serverFile = "Ollanect/serverInfo-3"
        altFile = True
    elif '-4' in sys.argv:
        serverFileTag = '-4'
        serverFile = "Ollanect/serverInfo-4"
        altFile = True
    elif '-5' in sys.argv:
        serverFileTag = '-5'
        serverFile = "Ollanect/serverInfo-5"
        altFile = True
    else:
        serverFile = "Ollanect/serverInfo"
        altFile = False

    try:
        scriptLocation = os.path.dirname(os.path.realpath(__file__))
        if systemOS == 'Linux':
            userHome = os.environ['HOME']
            infoFile = open(f'{userHome}/.config/{serverFile}', 'r')
        elif systemOS == 'Windows':
            appData = os.environ['APPDATA']
            infoFile = open(f'{appData}/{serverFile}.txt', 'r')
    except FileNotFoundError:
        if systemOS == 'Linux':
            scriptLocation = os.path.dirname(os.path.realpath(__file__))
            if altFile == True:
                os.system(f'chmod +x {scriptLocation}/setup-Linux')
                os.system(f'sh {scriptLocation}/setup-Linux {serverFileTag}')
                quit()
            else:
                os.system(f'chmod +x {scriptLocation}/setup-Linux')
                os.system(f'sh {scriptLocation}/setup-Linux')
                quit()
        elif systemOS == 'Windows':
            if altFile == True:
                os.system(rf'"C:\Program Files\Ollanect\ollanectSetupWindows.bat" {serverFileTag}')
                quit()
            else:
                os.system(r'"C:\Program Files\Ollanect\ollanectSetupWindows.bat"')
                quit()
    lines = infoFile.readlines()
    if lines:
        inputServer = lines[0]
    infoFile.close()
    return inputServer

if '-s' in sys.argv:
    sFlag = sys.argv.index('-s')
    if sFlag + 1 < len(sys.argv):
        inputServer = sys.argv[sFlag + 1]
    else:
        print("Flag -s expected one argument, got 0.")
elif '--server' in sys.argv:
    sOption = sys.argv.index('--server')
    if sOption + 1 < len(sys.argv):
        inputServer = sys.argv[sOption + 1]
    else:
        print("Option --server expected one argument, got 0.")
else:
    inputServer = getServer()

# Defines the URL for the Ollama Server
apiURL = f"{inputServer}/api/"

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
    if inputPrompt in ['/exit', '/quit', '/bye']:
        print('\nExiting!')
        sys.exit(0)
    elif inputPrompt in ['/help', '/?']:
        print(HELP_TEXT_CHAT)
        sys.exit(0)
    elif inputPrompt in ['/file', '/f']:
        print('File Path:')
        fileInput = input('> ')
        with open(fileInput, 'r') as file:
            fileContent = file.read()
            inputPrompt = input('Prompt: \n> ')
            systemPrompt = f"You are a helpful assistant. This is the file that the User has uploaded to you: {fileContent} Anylize the file and give a response based on the User's prompt."
    else:
        pass
    
    # File options
    if "-f" in sys.argv:
        fileFlag = sys.argv.index("-f")
        if fileFlag + 1 < len(sys.argv):
            fileInput = sys.argv[fileFlag + 1]
            with open(fileInput, 'r') as file:
                fileContent = file.read()
                systemPrompt = f"You are a helpful assistant. This is the file that the User has uploaded to you: {fileContent} Anylize the file and give a response based on the User's prompt."
        else:
            print("Flag -f expected 1 element, got 0")
    elif '--file' in sys.argv:
        fileOption = sys.argv.index("--file")
        if fileOption + 1 < len(sys.argv):
            fileInput = sys.argv[fileOption + 1]
            with open(fileInput, 'r') as file:
                fileContent = file.read()
                systemPrompt = f"You are a helpful assistant. This is the file that the User has uploaded to you: {fileContent} Anylize the file and give a response based on the User's prompt."
        else:
            print("Option --file expected 1 element, got 0")
    else:
        systemPrompt = "You are a helpful assistant. Anylize the User's prompt and give a response based on the User's prompt."

    # Defines what is sent to the server and sends it (requests.post)
    payload = {
        "model": inputModel,
        "prompt": inputPrompt,
        "system": systemPrompt,
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