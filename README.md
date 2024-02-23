# Input2SimulinkGenCode

## Objective
1. The objective of repository is to demonstrate that input can be provided externally (Python script) to generated C code of Simulink model. 
2. The output may then be verified for expected behaviour.

## Files
1. ERT generated code from Embedded Coder in Simulink for the model `my_model.slx`. Please note that, the model is kept simple, purely to demonstrate objective of the repository. The scaling up of model in user's case may be attempted separately.
2. This is code is contained in the folder `/my_model_ert_rtw`
3. In this folder, also is the file `my_model_win32.so`, a shared library for generated code from `my_model.slx` is present that is created
using gcc compiler. The step to generate it is outlined in `GenLib.txt`
4. This shared library is used by `helper_my_model.py` to access function contained in the generated C code.
5. `input_py_model.py` serves as external input to the generated code by using `helper_my_model.py`.

## Useful links
https://reptate.readthedocs.io/developers/python_c_interface.html
