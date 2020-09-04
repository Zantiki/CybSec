#include "../src/string.h"
#include <stddef.h>
#include <stdint.h>

int LLVMFuzzerTestOneInput(char *data, size_t size) {
    printf("Testing testing");
    string_modifier(data);
    return 0;
}
