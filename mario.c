#include <stdio.h>
#include <string.h>

int main(void)
{
    // Get the input of height for 1 through 8
    int height;
    do 
    {   
        printf("Height: ");
        scanf("%d", &height);
    } while (height < 0 && height >8);

    // this is so I can increment count as well I think it'll make it easier for me
    int line =1;
    while (line <= height) {
        // print out the hashes
        /* 4 as an example
           # #
          ## ##
         ### ###
        #### ####
        */
       // for the first line we took the number 4 minus one spaces and then added 1 hash
       // then we added a space and 1 more hash

       // first let's define hashes and spaces
       char hash[] = {'#'};
       char space[] = {" "};
       char result[50] = {""};
       for (int i = 1; i <= height - line; i++) {
            strcat(result, space);
        }
       
       for (int i = 0; i < line; i++) {
            strcat(result, hash);
        }
       strcat(result, space);
       strcat(result, space);
       for (int i = 0; i < line; i++) {
            strcat(result, hash);
        }

        printf("%s\n",result);
        line++;

    }
    
}