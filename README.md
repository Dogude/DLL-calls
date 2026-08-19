## Calling System Level Functions from various Languages
These are experiments about calling low level system functions

# HelloSDL3.asm
* Assembly program that manually writes import address table (IAT)
* for sdl3.dll, msvcrt.dll , user32.dll, kernel32.dll then
* shows how to call a function from these .dlls
* also writes macro for sprintf and messagebox combination

# HelloWindows.py
* Python script that uses cffi for C declarations for Windows types
* then shows how to pass a pointer, integer, wide char, callback functions(WNDPROC) to other functions
* Creates a Win32 Window and Button inside it.

# HelloSDL3.py
* Python script that uses ctypes for loading sdl3.dll
* and also shows how to fill the fields according to functions return value and parameters
* Finally creates a blank sdl3 window



