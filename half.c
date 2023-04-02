// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <stdlib.h>
#include <stdio.h>

float half(float bill, float tax, int tip);


int main(void)
{
    float bill_amount , tax_percent;
    int tip_percent;
    printf("Enter a bill amount: ");
    scanf("%f", &bill_amount);
    printf("Enter the tax percent: ");
    scanf("%f", &tax_percent);
    printf("Enter the tip percent: ");
    scanf("%d", &tip_percent);

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, int tip)
{
    float percentage;
    percentage = (float)tip;
    float total = (bill * (1 + (tax/100)))*(1 + percentage/100);
    return total/2;
}
