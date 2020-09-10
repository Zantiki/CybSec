#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *string_modifier(char *text){
    int original_length = strlen(text);
    int result_length = original_length;
    // printf("String before modification: %s\n", text);
    //exit(0);

    for (int i = 0; i < original_length; i++){
        // Check if refrence contains the char append to result_length
        if (memcmp(&text[i], "&", 1) == 0){
            result_length += strlen("&amp");
        }
        else if (memcmp(&text[i], "<", 1) == 0){
            result_length += strlen("&lt");
        }
        else if (memcmp(&text[i], ">", 1) == 0){
            result_length += strlen("&gt");
        }
        else{
            result_length++;
        }
    }

    // Allocate memory for string
   //char *res = (char *)malloc(sizeof(char) * result_length);
    //char *res = (char *)malloc(sizeof(char) * result_length);
    char res[result_length+1];

    int y = 0;
    // Copy string to allocated memory
    for (int i = 0; i < original_length; i++){

        if (memcmp(&text[i], "&", 1) == 0){
            memcpy(&res[y], "&amp", strlen("&amp"));
            y += strlen("&amp");
        }
        else if (memcmp(&text[i], "<", 1) == 0){
            memcpy(&res[y], "&lt", strlen("&lt"));
            y += strlen("&lt");
        }
        else if (memcmp(&text[i], ">", 1) == 0){
            memcpy(&res[y], "&gt", strlen("&gt"));
            y += strlen("&gt");
        }
        else{
            memcpy(&res[y], &text[i], sizeof(char));
            y++;
        }
    }
    //printf("String after modification: %s\n", res);
    return res;
}
