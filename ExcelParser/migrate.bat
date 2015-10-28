set PYTHONPATH=%PYTHONPATH%;lib
echo %1
python migrateExcelTestSuite.py --filename %1 --sheet %2 --start %3 --end %4 --suite %5 --output %6