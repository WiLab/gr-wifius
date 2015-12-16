INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_WIFIUS wifius)

FIND_PATH(
    WIFIUS_INCLUDE_DIRS
    NAMES wifius/api.h
    HINTS $ENV{WIFIUS_DIR}/include
        ${PC_WIFIUS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    WIFIUS_LIBRARIES
    NAMES gnuradio-wifius
    HINTS $ENV{WIFIUS_DIR}/lib
        ${PC_WIFIUS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WIFIUS DEFAULT_MSG WIFIUS_LIBRARIES WIFIUS_INCLUDE_DIRS)
MARK_AS_ADVANCED(WIFIUS_LIBRARIES WIFIUS_INCLUDE_DIRS)

