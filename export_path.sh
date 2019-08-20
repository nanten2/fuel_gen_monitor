#!/bin/bash
# pyenv
# -----
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
export PYTHONPATH=${PYTHONPATH}:$HOME/ros/src/necst/scripts/controller:$HOME/ros/src/necst/lib
