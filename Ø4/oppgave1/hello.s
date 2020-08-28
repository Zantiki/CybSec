section .data                 ; This section is for declaring initialized data
  msg: db "Hello World from Trondheim!", 10

section .text                 ; This is where the actual assembly code is written

  global _start               ; The .text section must begin with the declaration global _start,
                              ; which just tells the kernel where the program execution begins

_start:                       ; Execution begins here
  mov rcx, 3                 ; Set counter to 10

top:
  push rcx                    ; put counter on stack

  ; Set parameters for kernel system call:
  mov rax, 1                  ; The system call for write
  mov rdi, 2                  ; File descriptor 1 - standard output
  mov rsi, msg                ; Memory address of message
  mov rdx, 29                ; The length of message
  syscall                     ; Call the kernel

  pop rcx                     ; Restore counter from the stack
  dec rcx                     ; Decrease counter
  jnz top                     ; If counter is not 0, jump to top:

  mov rax, 60                 ; The system call for exit (sys_exit)
  mov rdi, 1                  ; Exit with return code of 0 (no error)
  syscall                     ; Call the kernel
