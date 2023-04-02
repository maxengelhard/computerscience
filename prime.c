#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool prime(int number);

int main(void)
{
    int min;
    printf("Minimum: ");
    scanf("%d", &min);
    
    int max;
    printf("Maximum: ");
    scanf("%d", &max);
    
    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // TODO
    if (number == 1) {
        return false;
    }

    for (int divider = 2; divider <  number; divider++) {
        // printf("%i , %i , %i\n", number, divider, number % divider);
        if (number % divider == 0) {
            return false;
        }
    }

    return true;
}
