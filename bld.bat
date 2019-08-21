git clone https://github.com/jejabour/adhtestingrevised.git
git fetch
git checkout -b adh_v45_mul origin/adh_v45_mul
python setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1