# Part 1:
Probable locations of vulnerability:
main, line 8. Outputting user-input, risk of address exposure.
```c
undefined8 main(void)

{
  char local_28 [32];
  
  printf("Enter your name: ");
  fgets(local_28,0x20,stdin); // <- Here
  printf("Hello ");
  printf(local_28); // <- Here
  putchar(10);
  return 0;
}
```
# Part 2:
See https://ctf.hacker101.com/ctf/hints/2