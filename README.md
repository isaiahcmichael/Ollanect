# Ollanect - A Terminal Application

## Overview

Ollanect is an open-source terminal-based application designed to connect to an Ollama server (or any other AI server that works similar to Ollama\*) of your choice. 

You can see updates at [updates.md](./updates.md)

**NOTE**: Ollanect is something that I do as a personal hobby, so it may be something that I quit at any time.

\* - Ollama is the only currently supported AI runner. Take caution when using with anything other than Ollama.

## Features

- Connect to your Ollama servers
- Run models on your servers
- Save up to 5 servers and ports at a time for easy access!

## Installation

### Requirements
Ensure you have Python installed. You can install Python at [python.org](https://www.python.org/downloads/) if you don't have it installed.

### Install (Linux - Official ZIP)
To install Ollanect on Linux using the official ZIP, you must unzip the ZIP file. You can download the ZIP file from the [releases page](https://github.com/isaiahcmichael/ollanect/releases/latest). After unzipping the zip file, you will run the following commands:

```sh
cd OllanectV{version} # Replace {version} with the version number
chmod +x ./install-Linux
./install-Linux
```

### Install (Linux (All Users) - Offical ZIP)
To install Ollanect on Linux using the Offical ZIP for all users, you must unzip the ZIP file. You can download the ZIP file from the [releases page](https://github.com/isaiahcmichael/ollanect/releases/latest). After unzipping the zip file, you will run the following commands:

```sh
cd OllanectV{version} # Replace {version} with the version number
chmod +x ./install-Linux-root
sudo ./install-Linux-root
```

### Install (Windows - Official ZIP)
To install Ollanect on Windows using the official ZIP, you must unzip the ZIP file. You can download the ZIP file from the [releases page](https://github.com/isaiahcmichael/ollanect/releases/latest). After unzipping the zip file, you will need to run `install-Windows.bat` as Admin.

### Install (`git clone`)
To install OLlanect using `git clone`, you will need to run the following command in your terminal:

```
git clone https://github.com/isaiahcmichael/Ollanect.git
```

#### Installing Cloned Files (Linux)
After cloning the files, you will need the following files in a directory together:
- `src/Ollanect/ollanect.py`
- `src/Ollanect/setup-Linux`
- `src/scripts/install-Linux` or `src/scripts/install-Linux-root`
- `requirements.txt`
- `LICENSE`

After putting all of the files above into a directory, you will need to run the following commands:

```sh
chmod +x ./install-Linux
./install-Linux # You can run ./install-Linux-root if you want to install for all users
```

#### Installing Cloned Files (Windows)
After cloning the files, you will need the following files in a directory together:
- `src/Ollanect/ollanect.py`
- `src/Ollanect/setup-Windows.bat`
- `src/scripts/install-Windows.bat`
- `requirements.txt`
- `LICENSE`

After putting all of the files above into a directory, you will need to run `install-Windows.bat` as Admin.

### Install (Windows - WSL)
If you want to use Windows Subsystem for Linux (or WSL) to install Ollanect, you can login to your WSL terminal and follow the instructions shown in the [Install (Linux - Official ZIP)](#install-linux---official-zip) or [Install (`git clone`)](#install-git-clone) sections.

## Running Ollanect

To start the application, run:

```sh
ollanect
```

### Options
There are options/flags that you can choose from. The general format of these are `ollanect {flag/option} {input}`. To see all options, run: 
```sh
ollanect --help
```
You can see Ollanect's help page for [Flags and Options](help/ollanectOptions.md) for the full list of Flag and Options.

## License

Ollanect is licensed under the **GNU General Public License v3.0**.

This program comes with ABSOLUTELY NO WARRANTY. It is free software, and you are welcome to redistribute it under certain conditions. See the full license in the [LICENSE](./LICENSE) file or at [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.html).

Ollanect uses dependances which have their own licenses. You can find the licenses in the [Licenses](./Licenses) directory or in the [Dependencies](#dependencies) section.


## Dependencies

- `requests` ([Apache 2.0 License](./Licenses/requests-LICENSE))
- Python Standard Library - `json`, `os`, `platform`, `zipfile` ([Python Software Foundation License](./Licenses/py-standardlib-LICENSE))

## Mirrors

If you need or require the use of a mirror (or a different website), you can find official Ollanect packages at the below locations.

- [GitHub](https://github.com/isaiahcmichael/ollanect), the main source.
- [Bitbucket](https://bitbucket.org/isaiahcmichael/ollanect/src/main/), updated by GitHub actions as a commit is pushed to GitHub.
- [Gitea](https://gitea.com/isaiahcmichael/Ollanect), updated by GitHub actions as a commit is pushed to GitHub.

You may see the GitHub Actions file at [`.github/workflows/mirrors.yml`](./.github/workflows/mirrors.yml) to see how the mirrors are updated.