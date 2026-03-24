@echo off
call .\.venv\Scripts\activate
start "Fragment" "http://localhost:5000/"
py web_app.py