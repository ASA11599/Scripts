#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define BUF_SIZE 100

int main(void)
{
    char buf[BUF_SIZE];
    char * cwd = getcwd(buf, sizeof(buf));
    printf(cwd);
    return 0;
}