#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../src/string_replace.c"

int main() {
    char *word3 = ">>>&&<<<";
    char *word3_expected = "&gt&gt&gt&amp&lt&lt&lt";
    char *result3 = string_modifier(word3);
    memcmp(word3, word3_expected, strlen(word3));
    int expression = strcmp(result3, word3_expected);
    assert(expression == 0);

    return 0;
}
