# POSIX
POSIX is an IEEE standard for OS-compatibility
.and is implemented as part of most larger
operating systems.

Generally POSIX is heavy, and therefore not implemented
for smaller cores.

Some of the standards covered in POSIX are:
* processes
* threads
* asynchronous IO
* commandline interpretation
* C libraries
* Handling memory violations
* Builtin tools (kill, grep, etc).
# POSIX Compilers
There are a few options:
* gcc: most common
* clang: standard for MacOS and supported on windows.

GCC is the GNU Compiler Collection, while clang is
part of LLVM (Low Level Virtual Machine). LLVM
æis used by the _Rust_ compiler, and comes built in
with several debuggers.
# Sanitizers
Address sanitizers come built into gcc and clang.
These tools can be used to find illegal memory
operations that may have otherwise flown under
the radar. Sanitizers are only used when testing,
due to increased resource usage. Below are some
of the faults an address-sanitizer
(seperated into thread-sanitizers, 
adress sanitizers and unfined behavior sanitizers) can detect:

* buffer owerflow/overread 
* data races in threads
* integer overflow
* conversion overflow
* Division by 0.
# Undefined behaviors
## Integer Overflow
Typical example is to initialize or increment
an integer out of bounds. Languages like rust
do not accept these kinds of behaviours and will
terminate the program on encountering one.

Some languages support arbitrary-precicion artihmetic
where these sorts of problems are avoided. This
is usually very resource-heavy.
# Range types
Range types are used to pre-define the numeric range
a numeric value can have. Defined like this
in C++:
```c++
bounded::ineger<0, 10> num(5);
```
C++ ranges are generally safer than Ada-ranges.
# Contracts
Allows to predefine certain characteristics of
the input of a function. This is not yet implemented
for C++, but is implemented in Ada which is 
the language of choice for many critical-systems
# Buffer Overflow
Buffer overflow is when you go outside the memory
range to a given variable and risk overrwring another
if the overflow is within the memory range of it's
function, then this will not necessarily be detected on build.
Classic example is to have a predefined string
of a certain length, when going above that length
the next variable in the stack will have it's value
overwritten with the address of the char that
is not within the sting-range.

## Avoiding buffer overflow
Generally you should be writing source-code in a
high-level fashion to isolate the different areas
potetially affected buy an overflow.
You should also make use of address sanitizers and
read the compiler warnings.
# Buffer overrun
In simple terms it involves tricking   a give program
to output further than it's defined memory-range.
i.e claiming asking a server for the sting "hat" with
500 letters and recieving all 497 other values
in memory after the HAT-string
# Fuzzing
Fuzzing is used to test overruns and overflows by
generating input-paramaters for a specific function.
This is the brute-force method of testing parameters.
fuzzing tools work well with sanitizers, and usually
has more advanced functionality for generating
permutations of input that maximize coverage.
libFuzzer is a popular example of a fuzzingTool.
