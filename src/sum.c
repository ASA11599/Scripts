#include <stdlib.h>
#include <stdio.h>

int sum(int * nums, int size)
{
    int res = 0;
    for (int i = 0 ; i < size ; i++) {
        res += nums[i];
    }
    return res;
}

// TODO: write function to convert char * to int

int main(int argc, char * argv[])
{
    int nums[argc];
    for (int i = 0 ; i < argc ; i++) {
        nums[i] = atoi(argv[i]);
    }
    printf("%d", sum(nums, argc));
    return 0;
}