#include <stdio.h>
#include <stdbool.h>
#include <string.h>


bool isEndOfSentence(char l)
{
    if (l=='!' || l=='.' || l=='?') {
        return true;
    }
    else {
        return false;
    }

}

int calcLevel(float L, float S) 
{
    // where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
    return 0.0588 * L - 0.296 * S - 15.8;
}

int main(void) 
{
    char text[255];
    do 
    {   
        printf("Text: ");
        scanf("%s", &text[255]);
    } while (strlen(text) < 0);

    printf("%s\n", text);
    // 
    int countLetters = 0;
    int countWords = 0;
    int countSentences = 0;
    for (int i=0; i <strlen(text) ; i++) {
        char l = text[i];

        if (isEndOfSentence(l) == true) {
            countSentences +=1;
        }
        else if (l ==' ') {
            countWords += 1;
        }
        else {
            countLetters+=1;
        }

    }
    printf("%d, %d, %d\n", countLetters,countSentences , countWords);
    // average number of letters per 100 words
    float avgWordPer100 = countWords/100;
    float L = countLetters / avgWordPer100;
    float S = countSentences / avgWordPer100;

    int level = calcLevel(L,S);

    printf("%d", level);
    
}

