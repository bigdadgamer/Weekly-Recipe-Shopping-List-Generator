ECHO ON
REM A batch script to execute a Python script
SET PATH=%PATH%;%~dp0
python weeklyRecipes.py
PAUSE
