#include <stdio.h>

float input(char *prompt);
float add(float a, float b);
float subtract(float a, float b);
float multiply(float a, float b);
float divide(float a, float b);


int main() {
    float a = input("Enter number One: ");
    float b = input("Enter numbser Two: ");
    float sum;

    do {
        char op = getchar();
        if (op == 'a') {
            sum = add(a, b);
        } else if (op == 's') {
            sum = subtract(a, b);
        } else if (op == 'm') {
            sum = multiply(a, b);
        } else if (op == 'd') {
            sum = divide(a, b);
        } else {
            printf("Invalid input: %c", op);
            break;
        }

        printf("%.3f", sum);
        break;

    } while (1);

    return 0;
}

float input(char *prompt) {
    char buffer[256];
    int number;

    do {
        printf("%s", prompt);
        if (fgets(buffer, sizeof(buffer), stdin)) {

            if (sscanf(buffer, " %d %c", &number, (char[1]){}) == 1) {
                return number;
            } else {
                printf("Invalid input: Not an Integer\n");
            }
        }
    } while (1);

    return number;
}

float add(float a, float b) {
    return a + b;
}

float subtract(float a, float b) {
    return a - b;
}

float multiply(float a, float b) {
    return a * b;
}

float divide(float a, float b) {
    return a / b;
}
