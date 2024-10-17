# Software Unit Validation

## Objective
1. The objective of repository is to demonstrate that for purpose of unit validation (SWE.4), input can be provided externally (Robot framework & Python) to generated C code from Simulink model.
   1. This method can help in creating a common unit validation (SWE.4) approach for features where the development happen in various platforms like model based or code based. 
   2. It also eliminates need of licenses (if any) since specific platform based tool that need license, are not involved in the process.
2. The output may be verified for expected behaviour through generated report.

## Prerequisite
1. Appropriate gcc compiler is installed (for e.g. MINGW).
2. Python 3.8 installed with required packages (for e.g. Robot framework 7.0, gcovr).
   1. Make sure path is added to environment variable in Windows 
   2. Make sure python interpretor path is set correctly incase an IDE is being used. (E.x VS Code)

## Files
1. ERT generated code from Embedded Coder in Simulink for the model `my_model.slx`, is available in the folder `/my_model_ert_rtw`. Please note that a CI job may be alternatively used to help retrieve this generated artifact.
2. A shared library for generated code from `my_model.slx` can be generated using gcc compiler. The step to generate it is outlined in the file `GenLib.txt`
3. This shared library is used by `helper_my_model.py` to access function contained in the generated C code.
4. `interface_my_model.py` hosts the python based interface equivalent of generated code (`interfaces`). This may be auto-generated using CI. Refer the folder `c2py` for more info.
5. The folder `tests` contain test folders corresponding to SURS (unit requirements). This folder contains
    1. The Robot framework test suite file which serves as input to the SURS test. 
    2. Keyword file which runs the assertion check by referring to relevant validation file in library.
    3. The test function file which defines the validation for the SURS and recieves input from above files.
6. ```test_REQ.py``` serves as the json format holder for interpreting test results for reporting (in CodeBeamer) as per REQ ID (referred through 'tag' in tests). The script takes input as ```output.xml``` report which is generated from test run. 

## How to Run tests
1. Generate shared library using steps in `GenLib.txt`.
2. In Powershell or Git bash, enter below instruction. 
    1. `robot tests` - In general, provide robot framework, the path to folder where test suites reside.
    2. This step runs tests in ```tests``` folder, generates log and report in html format and also generates ```output.xml```.
    3. For test REQ summary in json format, run ```test_REQ.py```. (This file needs ```output.xml``` as input).
         1. The json can serve as a traceability file which can be read by CI scripts to load information in REQ tools like CodeBeamer.
         2. This helps with requirements traceability.

## How to run Coverage
1. Refer `GenCoverage` to run coverage.

## Additional Files
1. `UserTypeArray.py` provides example of array of user data type defined as class/structure.

## Useful links
1. https://robotframework.org/
2. https://reptate.readthedocs.io/developers/python_c_interface.html
3. https://docs.python.org/3/library/ctypes.html
4. https://stackoverflow.com/questions/54888242/passing-nested-ctypes-structure-with-array-to-c-library-function-not-as-expected
5. https://stackoverflow.com/questions/1546355/using-enums-in-ctypes-structure
6. https://robotframework.org/robotframework/2.1.2/libraries/Collections.html#:~:text=Use%20Append%20To%20List%20to,be%20converted%20to%20an%20integer.
7. https://gcovr.com/en/5.1/guide/compiling.html
8. https://pypi.org/project/gcovr/
9. https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
10. https://stackoverflow.com/questions/973146/how-to-include-header-files-in-gcc-search-path


