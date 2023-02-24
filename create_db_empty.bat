set CURDATE=%date%
cd /d "%~dp0"
ren database.lite %CURDATE%_database.lite.back
python.exe create_db_empty.py