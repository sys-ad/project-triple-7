#!/bin/bash

tmux new-session -d -s flask 'flask run --host=0.0.0.0'

