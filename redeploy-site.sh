#!/bin/bash

### needs testing as of 02/18/2023


tmux kill-server

cd ~/portfolio_template_with_picocss/project-triple-7/

git fetch && git reset origin/main -hard

source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s mysession
