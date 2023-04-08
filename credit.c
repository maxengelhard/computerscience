#include <stdio.h>
#include <string.h>

int main(void)
{
    char card[100] = "";

    printf("Card Number: ");
    scanf("%s", card);

    // run the algorythm
    int count =0;
    int sum = 0;
    for (int i = strlen(card)-2; i --> 0;) {
        printf("%d\n", (int)card[i]);
        char number = card[i];
        int new_num = (int)number;
        if (count%2 ==0) {
            new_num = new_num*2;
            if (new_num>9) {
                // make will be 9*2 = 18 we then want 1 + 8
                new_num = 1 + (new_num-10);
            }
            sum += new_num;
        } else {
            sum += new_num;
        }

        // printf("%d , %d\n" , new_num , sum);
        count++;
    }

    printf("%d" , sum);

    if (sum % 10 == 0) {
        printf("Valid");
    } else {
        printf("Not Valid \n");
    }
    
    return 0;

}