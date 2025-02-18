# Ollanect Updates

## v0.2.2
Added file uploading support!

Fixed a bug that would prevent Ollanect from starting. (Commit [d476e6f](https://github.com/isaiahcmichael/Ollanect/commit/d476e6fcbc94b0537fc75b541acf1d9e3c7ea8ce) fixed this bug)

Added HTTPS support for Ollama server. (The config files need to be remade)

Added "This file is part of Ollanect." to every file that didn't have it already.

Added -s and --server option/flag to Ollanect. This allows the user to change the server that Ollanect connects to. When using the flag, the serverInfo file will not be read.

Added support for user addons. Read more in [help/ollanectAddons.md](./help/ollanectAddons.md).

See [Ollanect v0.2.2](https://github.com/isaiahcmichael/Ollanect/tree/v0.2.2) for files.

## v0.2.0
Added Windows [installer](./src/scripts/install-Windows.bat) and [setup](./src/Ollanect/setup-Windows.bat) files!

Fixed URL problem in [updates.md](./updates.md) under `v0.1.8`

Removed commented Line 85 in Ollanect's [main file](./src/Ollanect/ollanect.py)

Added Windows support! (Commit [f6ad518](https://github.com/isaiahcmichael/Ollanect/commit/f6ad5184234206486feb9ad3c47b3a0486dd5f85) brought Windows support to a more stable state!)

Allowed for [Linux install script](./src/scripts/install-Linux) to install requirements.txt file

Removed `#!/bin/python3` at top of [ollanect.py](./src/Ollanect/ollanect.py) to add Windows support

Fixed headers in [README.md](./README.md), removed installing requrements.txt file, and added Windows installation instructions

See [Ollanect v0.2.0](https://github.com/isaiahcmichael/Ollanect/tree/v0.2.0) for files

## v0.1.8
Added `/quit` and `/bye` to chat, both work in same way as `/exit`

Added `--version` and `-v` to Ollanect command. Prints out same output as `--license`.

Added `-h` to Ollanect command. Works the same as `--help`

Changed config files to be correctly held in `~/.config/Ollanect`

Fixed wording error under `v0.1.5` in [updates.md](./updates.md)

See [Ollanect v0.1.8](https://github.com/isaiahcmichael/Ollanect/tree/v0.1.8) for files.

## v0.1.5
Added new warning to [README.md](./README.md)

Added new file, updates.md to keep track of updates. (Also added link to updates.md in [README.md](./README.md))

Added comments to the [Ollanect file](./src/Ollanect/ollanect.py).

Added `/exit`, `/?`, and `/help` to chat menu for help and to exit chat mode.

Changed [install-Linux](./src/scripts/install-Linux) to make a link instead of a new file. Fixes a bug that I found that wouldn't allow the user to enter options and flags.

Added Ollanect's Version to Ollanect help.

See [Ollanect v0.1.5](https://github.com/isaiahcmichael/Ollanect/tree/v0.1.5) for files.

## v0.1.1
Added flags to Ollanect. `--help` shows all of the flags/options that you can use.

Can use flags/options to give prompt - `--prompt`

Can use flags/options to give model - `--model`

Using Ollanect without any flags will open a chat mode. Exit chat by using `CTRL` and `C`.

See [Ollanect v0.1.1](https://github.com/isaiahcmichael/Ollanect/tree/v0.1.1) for files.

## v0.1.0
Original Release of Ollanect.

See [Ollanect v0.1.0](https://github.com/isaiahcmichael/Ollanect/tree/v0.1.0) for files.