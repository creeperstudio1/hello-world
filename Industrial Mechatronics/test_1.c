#include <stdio.h>

void compute(float x[6], int a, int b);

int main () 
{
    int a, b;
    float x[6];
    printf("Enter values for a and b to compute:\n");
    scanf("%d", &a);
    scanf("%d", &b);
    // Call to compute function
    compute(x, a, b);
    // Print the results
    printf("%d + %d = %.2f\n", a, b, x[0]);
    printf("%d - %d = %.2f\n", a, b, x[1]);
    printf("%d * %d = %.2f\n", a, b, x[2]);
    if (b != 0) {
        printf("%d / %d = %.2f\n", a, b, x[3]);
    } else {
        printf("Cannot divide by zero.\n");
    }
    printf("(%d + %d)/2 = %.2f\n", a, b, x[4]);
    printf("The greater value between %d and %d is %.2f\n", a, b, x[5]);
    return 0;
}

void compute(float x[6], int a, int b) {
    x[0] = a + b;
    x[1] = a - b;
    x[2] = a * b;
    if (b != 0) {
        x[3] = (float)a / b;
    } else {
        x[3] = 0; 
    }
    x[4] = ((float)a + b) / 2;
    x[5] = (a > b) ? a : b;

    return;
}