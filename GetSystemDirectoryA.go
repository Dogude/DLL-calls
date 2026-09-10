package main

import (
	"fmt"
	"syscall"
	"unsafe"
)

var kernel32 = syscall.NewLazyDLL("kernel32.dll")
var GetSystemDirectoryA = kernel32.NewProc("GetSystemDirectoryA")

func main() {

	buffer := make([]byte, 256)

	GetSystemDirectoryA.Call(uintptr(unsafe.Pointer(&buffer[0])), 256)

	fmt.Println(string(buffer))

}
