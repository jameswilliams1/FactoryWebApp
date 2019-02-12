:: Activate the venv and run tests
echo off
call venv/scripts/activate.bat
cls
cd project/tests
pytest -vv test_api.py
