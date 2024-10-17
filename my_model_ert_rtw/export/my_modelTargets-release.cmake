#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "my_model::my_model_objects" for configuration "Release"
set_property(TARGET my_model::my_model_objects APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(my_model::my_model_objects PROPERTIES
  IMPORTED_COMMON_LANGUAGE_RUNTIME_RELEASE ""
  IMPORTED_OBJECTS_RELEASE "${_IMPORT_PREFIX}/my_model_ert_rtw/objects-Release/my_model_objects/my_model.c.obj"
  )

list(APPEND _IMPORT_CHECK_TARGETS my_model::my_model_objects )
list(APPEND _IMPORT_CHECK_FILES_FOR_my_model::my_model_objects "${_IMPORT_PREFIX}/my_model_ert_rtw/objects-Release/my_model_objects/my_model.c.obj" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
