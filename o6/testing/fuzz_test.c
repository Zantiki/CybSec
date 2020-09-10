#include "../src/string_replace.c"
#include <stddef.h>
#include <stdint.h>
#include <string.h>

int LLVMFuzzerTestOneInput(char *data, int size) {
    string_modifier(data);
    return 0;
}
