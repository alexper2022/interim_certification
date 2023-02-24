set CURDATE=%date%
cd /d "%~dp0"
ren database.lite %CURDATE%_test_database.lite.back
python create_db_test.py