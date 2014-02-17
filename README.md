# i3minator

i3minator is a simple "workspace manager" for i3.
It allows to quickly manage workspaces defining windows and their layout.
The project is inspired by [tmuxinator](https://github.com/aziz/tmuxinator) and uses [i3-py](https://github.com/ziberna/i3-py).

# Install

i3minator can be installed with pip

```shell
$ sudo pip install i3minator
```

# Project description

All project file are stored in `~/.i3minator/` and are in yaml format.
An example:

```yaml
# /home/carlesso/.i3minator/default.yml

# The Name of the project
name: default

# If needes, where the project lives. If present, all terminal will be opened here
# and all commands are relative to this path.
root: ~/projects/my_project/

# The name of the workspace to open the project.
# If not present, current workspace is used
workspace_name: MyProject

# Chain of commands to populate workspace.
# Every element can be either a node (see below), or a command between:
#   go_vertical, vertical, v:      change split mode into vertical
#   go_horizontal, horizontal, h:  change split mode into vertical
#   go_stacked, stacked:           set the layout to stacked
#
# Example for a rails application:
window_chain:
  - gvim
  - console
  - go_vertical
  - server
  - logs

# Nodes. Each node represent a window. The available parameters are:
#   command:  the command to execute
#   terminal: whatever the command should be run in a terminal window
#   timeout:  A window can take a while to be placed, if your layout does not come as you want,
#             inceremnt the timeout for slow windows. default: 0.1
nodes:
    gvim:
        terminal: false
        command: gvim .
        timeout: 0.3
    console:
        terminal: true
        command: bundle exec rails c
    server:
        terminal: true
        command: bundle exec rails s
    logs:
        terminal: true
        command: tailf log/development.log
```

# List of commands

i3minator supports the following commands:

```
i3minator commands:
    i3minator commands                  # Lists commands available in i3minator
    i3minator copy [EXISTING] [NEW]     # Copy an existing project to a new project and open it in your editor
    i3minator edit [PROJECT]            # Edit given project
    i3minator delete [PROJECT]          # Deletes given project
    i3minator impolode                  # Delete all i3minator project, as well as the ~/.i3minator folder
    i3minator list                      # List all i3minator projects
    i3minator new [PROJECT]             # Create a new project and open in your text editor
    i3minator start [PROJECT]           # Start a i3minator project
    i3minator version                   # Display installed i3minator version
```

# Terminal and Editor

Editor is read from shell's defaults:

```bash
echo $SHELL
```

Terminal is found by i3-sensible-terminal command.

Right now has been tested only with xterm and zsh

# Timeouting node spawn
Some windows may take more time to be insert in the workspace. If you experience this, and yout layout get messed up, try to play with `timeout` value in the node.

# About
Author: Enrico Carlesso
License: [WTFPL](http://www.wtfpl.net/about/)

Thanks:

 - [i3 window manager](http://i3wm.org/) and its author Michael Stapelberg
 - [i3-py](https://github.com/ziberna/i3-py)and its author Jure Žiberna

i3minator was tested with Python 3.3.2

Dependencies:

- i3-wm
- i3-py
- Python
