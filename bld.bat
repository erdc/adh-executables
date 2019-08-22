git clone https://github.com/jejabour/adhtestingrevised.git
git fetch
git checkout -b adh_v5_win64 origin/adh_v5_win64
python setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1