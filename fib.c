#include <stdio.h>
#include <stdlib.h>

int fib(const int n)
{
    if (n == 1) return 0;
    if (n == 2) return 1;
    else {
        return fib(n-1) + fib(n-2);
    }
}

int main(int argc, char * argv[])
{
    if (argc != 2) exit(EXIT_FAILURE);
    else {
        int n = atoi(argv[1]);
        if (n < 1) exit(EXIT_FAILURE);
        else {
            printf("%d", fib(n));
            exit(EXIT_SUCCESS);
        }
    }
    return 0;
}