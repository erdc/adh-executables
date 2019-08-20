from setuptools import setup

setup(
    name='adh_v45_win64',
    version='4.5',
    packages=[],
    data_files=[('Lib/site-packages/adh_v45_win64', ['adh_V4.5-WIN64.exe']),
                ('Lib/site-packages/adh_v45_win64', ['pre_adh_V4.5-WIN64.exe'])],
    url='https://github.com/jejabour/adhtestingrevised',
    author='Joseph Jabour',
    author_email='joseph.e.jabour@erdc.dren.mil',
    description='Executable for ERDC CHL computational AdH model',
    install_requires=[]
)
