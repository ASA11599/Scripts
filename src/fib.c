#include <stdio.h>
#include <stdlib.h>


unsigned long fib(const int n, unsigned long * memo)
{
    if (n == 1) return 0;
    if (n == 2) return 1;
    else {
        if (memo[n - 1] != -1) return memo[n - 1];
        else {
            unsigned long result = fib(n-1, memo) + fib(n-2, memo);
            memo[n - 1] = result;
            return result;
        }
    }
}

int main(int argc, char * argv[])
{
    if (argc != 2) exit(EXIT_FAILURE);
    else {
        int n = atoi(argv[1]);
        if (n < 1) exit(EXIT_FAILURE);
        else {
            unsigned long cache[n];
            cache[0] = 0;
            cache[1] = 1;
            for (int i = 2 ; i < n ; i++) {
                cache[i] = -1;
            }
            printf("%d", fib(n, cache));
            exit(EXIT_SUCCESS);
        }
    }
    return 0;
}