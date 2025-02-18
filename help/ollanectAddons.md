# Ollanect Addons

You can add new features to Ollanect by installing addons. You can install addons using the following command:

```bash
ollanect --addon install {addon-URL}
```

For example, if I were to have an Ollanect addon called OllanectPlus, you would replace `{addon-URL}` with the URL of the OllanectPlus info file. You can find the URL of the info file in the addon's README file or website. For example, if I had OllanectPlus's info file located at the root of a GitHub repository named OllanectPlus, the URL of the file could be "https://raw.githubusercontent.com/isaiahcmichael/OllanectPlus/refs/heads/main/ollanectplus".

## Options

### `install`

Use `ollanect --addon install {addon-URL}` to install an addon.

### `run`

Use `ollanect --addon run {addon-name}` to run an installed addon.

### `list`

Use `ollanect --addon list` to list all installed addons.

### `remove`

Use `ollanect --addon remove {addon-name}` to remove an installed addon.

## Developer Guide

To create an addon, you need to make sure that your main file is named `main.py`. That is the only Python file that you will need. You will zip `main.py` along with all of your other files inside of a zip file. Make note of the download URL. You will need to provide this URL to users who want to install your addon. In a URL, you need to have a file named `{addon-name}`. It will be a plaintext file that contains your addon's info. The first line will contain the name of the addon. The second line will contain the URL of the zip file. The third line will contain the version of the addon. The fourth line will contain the author's name. The fifth line will contain the repository of the addon. Here is an example of an addon info file:

```plaintext
OllanectPlus
https://example.com/isaiahcmichael/OllanectPlus/ollanectplus.zip
1.0.0
Isaiah Michael
https://example.com/git/isaiahcmichael/OllanectPlus
```

### The ZIP File

The info file should have a link on Line 2 that links to a file in ZIP format. The ZIP file should contain the files that your addon needs. In the root of the ZIP file, a file named `main.py` should exist. It'll be the file that Ollanect runs. You can include your other files in other places (i.e. subfolders) as long as you import them correctly in `main.py`. For compatibility reasons, it is recommended that you use Python 3 for your scripts, although other types of scripts may work. Do **NOT** add the info file to the ZIP file. Ollanect automatically downloads the info file when the addon is installed.