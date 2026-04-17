cmake_minimum_required(VERSION 3.30)

# 必须在 project() 之前
set(CMAKE_EXPERIMENTAL_CXX_IMPORT_STD "451f2fe2-a8a2-47c3-bc32-94786d8fc91b")
set(CMAKE_CXX_STDLIB_MODULES_JSON
    "/opt/homebrew/opt/llvm/lib/c++/libc++.modules.json")

project(demo CXX)

set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_MODULE_STD ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_compile_options(-stdlib=libc++)
add_link_options(-stdlib=libc++)

add_executable(app)

# 你自己的模块（.cppm 文件）走 FILE_SET CXX_MODULES
target_sources(app
    PRIVATE
        main.cpp
    PRIVATE FILE_SET CXX_MODULES FILES
        math.cppm
        geo.cppm
)
