# Ollanect - A Terminal Application

## Overview

Ollanect is an open-source terminal-based application designed to connect to an Ollama server (or any other AI server that works similar to Ollama\*) of your choice.

\* - Ollama is the only currently supported AI runner. Take caution when using with anything other than Ollama.

## Features

- Connect to your Ollama server
- Run models on your server
- Save your server and port so you don't need to re-enter them every time!

## Installation

### Requirements

Ensure you have Python installed. You can install dependencies using:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file can be found at the source of the [GitHub Page](https://github.com/isaiahcmichael/ollanect), along with the release in "Releases" on the GitHub Page.

### Getting Packages

Ensure that you got the packages for Ollanect from either cloning the repo or by going to the Releases tab on the GitHub Page.
**IMPORTANT:** All of the files (`install-Linux`, `ollanect.py`, `setup-Linux`, and `LICENSE`) need to be in the same directory! You may need to run `chmod +x ./install-Linux` before running the following command: 
```sh
sh ./install-Linux
```
### Running Ollanect

To start the application, run:

```sh
ollanect
```

## License

Ollanect is licensed under the **GNU General Public License v3.0**.

This program comes with ABSOLUTELY NO WARRANTY. It is free software, and you are welcome to redistribute it under certain conditions. See the full license in the [LICENSE](./LICENSE) file or at [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html).


## Dependencies

- `requests` (Apache 2.0 License)
- Python Standard Library (`json`, `os`, `platform`)