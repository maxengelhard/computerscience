#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int n;
    do
    {
        printf("Select start size: ");
        scanf("%d", &n);
    } while (n < 9);
    
    
    // TODO: Prompt for end size
    int end_size;
    do
    {   
        printf("Select end size: ");
        scanf("%d", &end_size);
        /* code */
    } while (end_size < n);
    


    // TODO: Calculate number of years until we reach threshold
    int num_of_years = 0;

    while (n < end_size) {
        // every year n/3 is born
        int born = n/3;
        // every year n/4 die
        int die = n/4;

        num_of_years++;
        n = n + born - die;
    }

    // TODO: Print number of years
    printf("%i \n", num_of_years);
}
