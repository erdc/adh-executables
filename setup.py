from setuptools import setup

setup(
    name='adh_v45_mul',
    version='4.5',
    packages=[],
    data_files=[('Lib/site-packages/adh_v45_mul', ['adh_V4.5-MUL.exe']),
                ('Lib/site-packages/adh_v45_mul', ['pre_adh_V4.5-MUL.exe'])],
    url='https://github.com/jejabour/adhtestingrevised',
    author='Joseph Jabour',
    author_email='joseph.e.jabour@erdc.dren.mil',
    description='Executable for ERDC CHL computational AdH model',
    install_requires=[]
)
