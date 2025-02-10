#!/bin/bash

# Flaskアプリケーションを起動する
gunicorn --chdir . app:app --bind 0.0.0.0:8000