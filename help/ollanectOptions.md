# Ollanect Options and Flags

Ollanect is a command-line tool that allows you to interact with your Ollama server. You can find the options and flags for Ollanect below.

## Usage

```sh
ollanect [options]
```

## Options

### `--help` or `-h`
Displays the help menu with all available options.

### `--license`
Displays Ollanect's licensing. Ollanect is licensed under the **GNU General Public License v3.0**.

### `--one-prompt`
Opens Ollenect without chat mode.

### `--model` or `-m`
Specifies the model to use. Example:
```sh
ollanect --model phi4:latest
```
or
```sh
ollanect -m phi4:latest
```

### `--prompt` or `-p`
Specifies the prompt to use. Example:
```sh
ollanect --prompt 'When was GitHub created?'
```
or
```sh
ollanect -p 'When was GitHub created?'
```

### `--help-chat`
Displays Ollanect's chat commands. See [**Chat Commands**](#chat-commands) for chat commands.

## `--version` or `-v`
Displays Ollanect's commands and License.

## `--server` or `-s`
Specifies the server to connect to. Ollanect does not read the serverInfo file when run. Example:
```sh
ollanect --server http://localhost:1234
```

## Chat Commands

When in chat mode, you can use the following commands:

### `/help` or `/?`
Displays Ollanect's Chat Help menu.

### `/exit`, `/quit`, or `/bye`
Exits Ollanect.

## Example Usage

To start Ollanect with a specific model and prompt:
```sh
ollanect --model phi4:latest --prompt 'When was GitHub created?'
```

To start Ollanect in single-prompt mode:
```sh
ollanect --one-prompt
```

To start Ollanect in single-prompt mode with specific model and prompt:
```sh
ollanect --one-prompt -m phi4:latest -p 'When was GitHub created?'
```

To display the license information:
```sh
ollanect --license
```

To display the help menu:
```sh
ollanect --help
```
