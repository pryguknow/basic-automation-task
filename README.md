# Basic Python test task by Hlib Pryhunov

API and UI automation tests written in Python using Pytest, Requests, and Playwright.

## Setup

### Create the environment
python -m venv venv

### Activate on macOS:
source venv/bin/activate

### Install Project Dependencies
pip install -r requirements.txt 

playwright install

### Run preparations
Set "YOUR_TOKEN" as your API token in conftest.py

### Test Run
pytest tests/api

pytest tests/ui 

