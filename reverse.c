#include <stdio.h>
#include <stdlib.h>

int str_len(char * str)
{
    int len = 0;
    while (*str != '\0') {
        str++;
        len++;
    }
    return len;
}

char * str_rev(char * str)
{
    int size = str_len(str);
    char * cpy = (char *) malloc(sizeof(char) * size);
    for (int i = 0 ; i < size ; i++) cpy[i] = str[size-i-1];
    return cpy;
}

int main(int argc, char * argv[])
{
    for (int i = 1 ; i < argc ; i++) {
        printf("%s\n", str_rev(argv[i]));
    }
    return 0;
}