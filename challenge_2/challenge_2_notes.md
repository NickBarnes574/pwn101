# Challenge 2 Notes

1. Buffer is `104` bytes long.
2. There is a check to see if badfood == `0xc0ff33` and feeldead == `0xc0d3`
3.

- When examining a function in Ghidra. Understand what each line is doing.
  
- Check the function prologue to verify that the stack frame is the size that you expect it to be.

- If you suspect there may be vulnerabilites for a function but you don't know what they are, research and look up those vulnerabilites

## Looking at a stack frame

base pointer (rbp) - stack pointer (rsp)
`p /d $rbp - $rsp` - gives you the stack frame size
`p /d [stack_frame_size] / 8` - gives you how many giants you want to look at

So for example, if our stack frame was `112` bytes, we would do:
`p /d 112 / 8` which gives us `14`

so to look at the stack frame in hex, we would do:
`x/14gx $rsp`
