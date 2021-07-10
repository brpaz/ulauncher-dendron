# ulauncher-dendron

> Access your [Dendron](https://www.dendron.so/) notes from [Ulauncher](https://ulauncher.io/).

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-dendron/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-dendron)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-dendron.svg?style=for-the-badge)](LICENSE)


##  Features

* Integrates with Dendron, by reading `.dendron.cache.json` file, located in your Vault(s) folder.
* Find your notes by their title or hierarchy path.
* Multi-vault support.
* Compatible with multiple ways to launch Dendron (VSCode, Codium, separate extensions dir, etc). Just specify the full command to open your Dendron workspace on the Extension settings.
* Open file with [Quickmd](https://github.com/AndrewRadev/quickmd) for quick preview. Requires quickmd to be installed.

### Demo

![demo](docs/assets/demo.gif)



## System Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* [Dendron](https://www.dendron.so/) with [Caching](https://wiki.dendron.so/notes/93022442-b49b-4510-b695-e10d8651ecfe.html) enabled (default).
* Python >= 3

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-dendron
```

## Usage

* By default this extension looks for `dendron` keyword. You can change it to something shorter like `dd` on the extension settings.

* Typing the keyword and then a query, it will filter all your notes matching that query in both title and hierarchy fields.

Before starting using this extension, you must set some settings to match your Dendron install. See section below.

:rotating_light: Dendron cache files are only updated on the initialization of the Dendron Workspace. This means new notes won´t appear unless you reload your Dendron workspace.

### Open with quickmd

Select an item and press `ALT-Enter`

### Configuration

This extension requires the following settings to be set, according your Dendron install:


 Name              	| Description                                                                                                               	| Example                                                                                                                                                          	|
|-------------------	|---------------------------------------------------------------------------------------------------------------------------	|------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| **Dendron Workspace** 	| The absolute path to the Dendron workspace root directory on your system.                                                       	| `/home/bruno/Dendron`                                                                                                                                              	|
| **Dendron Vaults**    	| A Comma separated list of Dendron vaults to be indexed, relative to the Dendron Workspace root.                                   	| `vault.personal,vault.dev`                                                                                                                                         	|
| **Dendron Command**   	| The command to open your Dendron Workspace. Use `%f%` to indicate where the file path of the selected file will be placed. 	| `/usr/bin/codium --user-data-dir=/home/bruno/.config/dendron/data --extensions-dir=/home/bruno/.config/dendron/ext /home/bruno/Dendron/dendron.code-workspace %f%` 	|

### Other commands

* Notes are cached at Uluancher startup. To Refresh the notes cache at any time, run `dendron :reload`.


## Development

```
git clone https://github.com/brpaz/ulauncher-dendron
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev` and follow the instructions.


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)

Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>


## License

MIT &copy; Bruno Paz
