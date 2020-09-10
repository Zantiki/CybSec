#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../src/string_replace.c"

int main() {
    char *word3 = ">>>&&<<<";
    char *word3_expected = "&gt&gt&gt&amp&lt&lt&lt";
    char *result3 = string_modifier(word3);
    assert(memcmp(result3, word3_expected, strlen(word3_expected)) == true);

    char *word = "";
    assert(memcmp(string_modifier(word), word, strlen(word) ) == true);

    char *word2 = "Halla";
    char *result2 = string_modifier(word2);
    assert(memcmp(result2, word2, strlen(word2)) == true);

    return 0;
}
