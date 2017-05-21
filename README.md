# NPL-Miniproject

A web-app that I built for my networking lab miniproject.

A lightweight remote command execution tool, with an easy to use GUI, built on top of the SSH Protocol tied with a Djago Server.

## Features

-A lightweight remote command execution tool, with an easy to use GUI.

-Scans the subnet for machines with port 22 open.

-Communicates with them using the SSH Protocol to remotely execute commands and pipe back response on the web-interface.

-Allows mass execution of commands.

## Currently Available Commands:

-Update package lists.

-Install particular packages

-List all known running proceses.

-Print home-directory

-List all network interfaces

## Adding more commands:

The command execution has been modularized, and any command to be executed has to be simply passed to the  `execute_command(command)` function in `views.py` in the app. 
Submit a pull request if you want to add more commands/functionalities.





