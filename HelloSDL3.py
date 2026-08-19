from ctypes import windll , WinDLL, c_char_p, c_void_p, c_int, c_uint, c_uint8 , c_ulong ,c_uint32
from ctypes import Structure, POINTER, create_string_buffer

sdl = WinDLL(r"SDL3.dll")

buffer = create_string_buffer(256)

windll.kernel32.GetModuleFileNameA(None,buffer,256)

print(buffer.value)

sdl.SDL_GetVersion.restype = c_int

ver = sdl.SDL_GetVersion()

sdl.SDL_Log.argtype = [c_char_p,c_int]

sdl.SDL_Log(b"%d",3)

print(f"SDL Version: {ver}")

sdl.SDL_Init.argtype = [c_uint32]

SDL_INIT_VIDEO = 0x00000020

result = sdl.SDL_Init(SDL_INIT_VIDEO);

sdl.SDL_CreateWindow.argtypes = [c_char_p, c_int, c_int, c_uint32]
sdl.SDL_CreateWindow.restype = c_void_p

SDL_WINDOW_SHOWN = 0x00000004

title = b"My First SDL Window"
width, height = 800, 600

window = sdl.SDL_CreateWindow(title, width, height, SDL_WINDOW_SHOWN)

class SDL_Event(Structure):
    _fields_ = [("type", c_uint32)]

SDL_QUIT = 0x100

sdl.SDL_PollEvent.argtypes = [POINTER(SDL_Event)]
sdl.SDL_PollEvent.restype = c_int

event = SDL_Event()

sdl.SDL_CreateRenderer.argtypes = [c_void_p, c_char_p, c_uint32]
sdl.SDL_CreateRenderer.restype = c_void_p

renderer = sdl.SDL_CreateRenderer(window, None, 0)

sdl.SDL_SetRenderDrawColor.argtypes = [c_void_p, c_uint8, c_uint8, c_uint8, c_uint8]
sdl.SDL_SetRenderDrawColor.restype = c_int

sdl.SDL_RenderClear.argtypes = [c_void_p]
sdl.SDL_RenderClear.restype = c_int

sdl.SDL_RenderPresent.argtypes = [c_void_p]
sdl.SDL_RenderPresent.restype = None

running = True

while running:
    while sdl.SDL_PollEvent(event):
        if event.type == SDL_QUIT:
            running = False
       
    sdl.SDL_SetRenderDrawColor(renderer, 0, 128, 55, 255)
    sdl.SDL_RenderClear(renderer)
    sdl.SDL_RenderPresent(renderer)
        
sdl.SDL_DestroyRenderer.argtypes = [c_void_p]
sdl.SDL_DestroyRenderer.restype = None
sdl.SDL_DestroyRenderer(renderer)

sdl.SDL_DestroyWindow.argtypes = [c_void_p]
sdl.SDL_DestroyWindow.restype = None
sdl.SDL_DestroyWindow(window)

sdl.SDL_Quit()
