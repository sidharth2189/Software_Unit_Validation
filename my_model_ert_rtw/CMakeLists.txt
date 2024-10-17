######################################################################
# CMakeLists.txt generated for component my_model
# Product type: executable
######################################################################
cmake_minimum_required(VERSION 3.12)
project(my_model)
if(DEFINED ENV{CMAKE_EXPORT_COMPILE_COMMANDS} AND NOT DEFINED CMAKE_EXPORT_COMPILE_COMMANDS)
    set(CMAKE_EXPORT_COMPILE_COMMANDS $ENV{CMAKE_EXPORT_COMPILE_COMMANDS})
endif()


######################################################################
## Path variables
######################################################################
get_filename_component(START_DIR .. ABSOLUTE)
set(MATLAB_ROOT C:/Program\ Files/MATLAB/R2022b CACHE PATH "")
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
if(${CMAKE_CURRENT_BINARY_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
    set(BUILDING_IN_SOURCE_DIR TRUE)
    set(BINARY_START_DIR "${START_DIR}")
else()
    set(BUILDING_IN_SOURCE_DIR FALSE)
    set(BINARY_START_DIR "${CMAKE_BINARY_DIR}")
endif()

######################################################################
## Target definition and commands
######################################################################
add_library(my_model_objects OBJECT ${START_DIR}/my_model_ert_rtw/my_model.c)
set_target_properties(my_model_objects PROPERTIES
    PREFIX ""
    POSITION_INDEPENDENT_CODE ON)
target_compile_features(my_model_objects PUBLIC c_std_99)
target_compile_definitions(my_model_objects PRIVATE -DMODEL=my_model
    -DNUMST=1
    -DNCSTATES=0
    -DHAVESTDIO
    -DMODEL_HAS_DYNAMICALLY_LOADED_SFCNS=0
    -DCLASSIC_INTERFACE=0
    -DALLOCATIONFCN=0
    -DTID01EQ=0
    -DTERMFCN=1
    -DONESTEPFCN=1
    -DMAT_FILE=0
    -DMULTI_INSTANCE_CODE=0
    -DINTEGER_CODE=0
    -DMT=0)
target_link_libraries(my_model_objects PRIVATE -static
    -m64)
target_include_directories(my_model_objects PUBLIC $<BUILD_INTERFACE:${START_DIR}>
    $<INSTALL_INTERFACE:$<INSTALL_PREFIX>>
    $<BUILD_INTERFACE:${START_DIR}/my_model_ert_rtw>
    $<INSTALL_INTERFACE:$<INSTALL_PREFIX>/my_model_ert_rtw>
    $<BUILD_INTERFACE:${MATLAB_ROOT}/extern/include>
    $<BUILD_INTERFACE:${MATLAB_ROOT}/simulink/include>
    $<BUILD_INTERFACE:${MATLAB_ROOT}/rtw/c/src>
    $<BUILD_INTERFACE:${MATLAB_ROOT}/rtw/c/src/ext_mode/common>
    $<BUILD_INTERFACE:${MATLAB_ROOT}/rtw/c/ert>)
find_library(FOUND_LIBM m)
if(FOUND_LIBM)
   target_link_libraries(my_model_objects PUBLIC m)
endif()

add_executable(my_model  ${START_DIR}/my_model_ert_rtw/ert_main.c)
set_target_properties(my_model PROPERTIES
    PREFIX ""
    POSITION_INDEPENDENT_CODE ON)
if(CMAKE_CXX_COMPILER)
    set_target_properties(my_model PROPERTIES LINKER_LANGUAGE CXX)
endif()
target_compile_features(my_model PUBLIC c_std_99)
target_compile_definitions(my_model PRIVATE -DMODEL=my_model
    -DNUMST=1
    -DNCSTATES=0
    -DHAVESTDIO
    -DMODEL_HAS_DYNAMICALLY_LOADED_SFCNS=0
    -DCLASSIC_INTERFACE=0
    -DALLOCATIONFCN=0
    -DTID01EQ=0
    -DTERMFCN=1
    -DONESTEPFCN=1
    -DMAT_FILE=0
    -DMULTI_INSTANCE_CODE=0
    -DINTEGER_CODE=0
    -DMT=0)
target_link_libraries(my_model PRIVATE -static
    -m64)
target_include_directories(my_model PRIVATE ${START_DIR}
    ${START_DIR}/my_model_ert_rtw
    ${MATLAB_ROOT}/extern/include
    ${MATLAB_ROOT}/simulink/include
    ${MATLAB_ROOT}/rtw/c/src
    ${MATLAB_ROOT}/rtw/c/src/ext_mode/common
    ${MATLAB_ROOT}/rtw/c/ert)
target_link_libraries(my_model PRIVATE my_model_objects)
find_library(FOUND_LIBM m)
if(FOUND_LIBM)
   target_link_libraries(my_model PRIVATE m)
endif()
if(WIN32)
   target_link_libraries(my_model PRIVATE kernel32
       ws2_32
       mswsock
       advapi32)
endif()

######################################################################
## Extract debug symbols
######################################################################
if(APPLE AND (CMAKE_C_COMPILER_ID STREQUAL "AppleClang"))
    string(APPEND _dsymutilcmd "$<IF:$<CONFIG:DEBUG,RELWITHDEBINFO>,"
                "xcrun;dsymutil;$<TARGET_FILE:my_model>;--flat,"
                "true"
        >)
    add_custom_command(TARGET my_model
            POST_BUILD
            COMMAND "${_dsymutilcmd}"
            COMMAND_EXPAND_LISTS
            BYPRODUCTS my_model.dwarf)
    install(FILES $<TARGET_FILE_DIR:my_model>/my_model.dwarf DESTINATION . OPTIONAL CONFIGURATIONS Debug RelWithDebInfo)
endif()
if(CMAKE_C_LINKER_SUPPORTS_PDB)
    install(FILES $<TARGET_PDB_FILE:my_model> DESTINATION . OPTIONAL CONFIGURATIONS Debug RelWithDebInfo)
endif()


######################################################################
## Target install and export rules
######################################################################
install(TARGETS my_model_objects EXPORT my_modelTargets OBJECTS DESTINATION my_model_ert_rtw)
install(TARGETS my_model RUNTIME DESTINATION . OPTIONAL)
install(EXPORT my_modelTargets NAMESPACE my_model:: DESTINATION my_model_ert_rtw/export)
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/my_model.cmake 
 "include(\"\${CMAKE_CURRENT_LIST_DIR}/my_modelTargets.cmake\")" \n
    "target_include_directories(my_model::my_model_objects INTERFACE \n"
    "    \${MATLAB_ROOT}/extern/include" \n 
    "    \${MATLAB_ROOT}/simulink/include" \n 
    "    \${MATLAB_ROOT}/rtw/c/src" \n 
    "    \${MATLAB_ROOT}/rtw/c/src/ext_mode/common" \n 
    "    \${MATLAB_ROOT}/rtw/c/ert)" \n )
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/my_model.cmake DESTINATION my_model_ert_rtw/export)

######################################################################
## Build success message
######################################################################
add_custom_command(TARGET my_model POST_BUILD
     COMMAND ${CMAKE_COMMAND} -E cmake_echo_color --cyan "\\#\\#\\# Created executable: $<TARGET_FILE:my_model>")

######################################################################
## Call toolchain hook function if defined
######################################################################
if(COMMAND toolchain_target_hook)
    toolchain_target_hook(my_model)
endif()
