# Common Software Volunarbilities
# General:
Always assume that user-input is unsafe
Some definitions apply across the board:
* Vulnerability: weakness that be exploited
* security bug: vurlnerability as a result of
error
* Attack vector: specfic attack-point
* Attack surface: sum of attack vectors
* Zero-day: unkown bug or vulnerability that can
be exploited by an attacker.
  
The following list contains common security
bugs:
* memory safety
* Race condition
* input and output validation/handeling
* improper API usage
* improper use-cases
* improper exception handling
* resource leaks.

For engineers and develoers OWASP top ten are
by far the most important.

## Web-file inclusion and SQL-injection:
Depending on the type of server you can sometimes
access files intended to be hidden. This
and SQL-injections can be put into URL-parameters.
as so:
> url.com?param=0&param=1

## Command injection
Where there are input-fields, you can sometimes
inject commands buy studying how the endpoint
responds.

## Arbitrary file read:
use iperf to measure who reads a file.

## CSRF
short for cross-site request forgery, where you
trick a user to send http requests that often have
unintended consequences.

## Bug reporting:
Generally, disclosure should be coordinated,  
where critical security-vulnerabilities are exposed
if they are not fixed within a set timeframe or
expose on fix. 

Use full disclosure if vendor is non-responsive
and urgency is key.
Found vulnerabilities can be scored with CVSS
(Common Vulnerability Scoring System)
# Native:
## Buffer overflow
Overflow a given array/string etc. to expose other
parts of the address space. 
There are some migitations working against buffer
overflows:
* Address space layout randomisation: ASLR
* Stack canary for detecting stack smashing
* Non-executable stack heap NX
* Position independent executable (PIE).

It is possible to use buffer overflows to execute shellcode
it is however very difficult to on an NX-stack.

## Dangeling pointers:
Occurs when pointers are left unitinilized
after free() or on exited scope. These
can also be used to access restriced areas of
memory.

## Format string vulnerability:
Can occur when user strings are passed
directly to printf as certain types of formatting
can provide the value at a given address.
%10$p will f.ex print the next 10 addresses.

## ROT (Return Oriented Programming)
Part of non-executable stack, where we can
inject shellcode, but not run it. We can however
jump to locations in the code as the program runs.
As such, if we want anything executed we need
to override the address at ret-instructions

# Reverse engineering:
Reverse engineering is useful for many things:
* recreating old software or protocols
* Software freedom
* understanding malicious code
* exploiting vulnerabilities
* DRM
* curiosity and research.
## Techniques:
Comprises of these parts:

Analysis:
* Obervation of information exchange
* Bus analysers, packet sniffers
* JTAG on embedded
* low-lvel debugger.

Dissasembly:
* study machine-code

Decompilation:
* reconstruct source-code from disassebled binary.

## Tools:
Disassemblers:

* objdump: get info from object-files
* redare2: commandline hexidecimal editor
* IDA Pro: dissasemble on multipe archs, 
can also debug and decompile.
* ghidra: NSA tool for multi-architcture dissasembly
and decompiler