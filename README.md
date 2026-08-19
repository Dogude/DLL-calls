## Calling System Level Functions from various Languages
These are experiments about calling low level system functions

# HelloSDL3.asm
* Assembly program that manually writes import address table (IAT)
* for sdl3.dll, msvcrt.dll , user32.dll, kernel32.dll then
* shows how to call a function from these .dlls
* also writes macro for sprintf and messagebox combination
* Compile this code sdl3 must be placed same directory of output executable and requires a Flat Assembler
* ``` fasm.exe HelloSDL3.asm ```

# HelloWindows.py
* Python script that uses cffi for C declarations for Windows types
* then shows how to pass a pointer, integer, wide char, callback functions(WNDPROC) to other functions
* Creates a Win32 Window and Button inside it.
* First Step is : pip install cffi
* Run This code : python HelloWindows.py
* Button looks like modern windows style(not win98/xp) because python.exe itself has manifest file resource
<img width="536" height="294" alt="image" src="https://github.com/user-attachments/assets/a62dd12a-b7a6-431b-8da2-142e8e24fe5a" />

# HelloSDL3.py
* Python script that uses ctypes for loading sdl3.dll
* and also shows how to fill the fields according to functions return value and parameters
* Finally creates a blank sdl3 window
* Run This code : python HelloSDL3.py
* sdl3.dll must be placed in Python's one of sys.path
<img width="797" height="244" alt="image" src="https://github.com/user-attachments/assets/23f09f0c-99b6-439d-82fc-7065beef263d" />

# RegisterClass.py
* Python script uses ctypes for filling WNDCLASSA structure
* then passes Address of WNDCLASSA to RegisterClassA
* also shows how to declare a windows structure and how to fill it
* Run This code : python RegisterClass.py


