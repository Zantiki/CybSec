#include "../src/string_replace.c"
#include <stddef.h>
#include <stdint.h>
#include <string.h>

int LLVMFuzzerTestOneInput(char *data, int size) {
   // int length = strlen((const char *)data);
    string_modifier(data);
    //printf(&res);
    return 0;
}
