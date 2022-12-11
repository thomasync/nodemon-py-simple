# nodemon-py-simple

## Nodemon like for python, very simple and without dependencies

This script watches a directory for file changes and executes a process when a file is modified or added. The process can also be killed if necessary. Additionally, the script can be configured to only watch files with specific extensions and to clear the console before executing the process.

And why this package when nodemon exists? Because I no longer want to install node, npm... just for nodemon on my docker images and I haven't found an alternative in python without dependencies.

# Installation

```
pip install nodemon-py-simple
```

# Usage

To use this script, use the following command line:

```
python script.py directory [options] command
```


The available options are as follows:

- `-e`, `--extensions`: a list of file extensions to watch, separated by commas
- `-k`, `--kill`: the process name of the process to kill when a file is modified or added
- `-m`, `--modified-time`: update modified time of the file (like modd)
- `-c`, `--clear`: clear the console before executing the command

# Contributing

Thank you for considering contributing to this project!

To contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them to your branch
4. Push your branch to your forked repository
5. Create a pull request to the original repository

Note: Before creating a pull request, please make sure that your changes are consistent with the overall code style and structure of the project. Thank you for your contribution!
