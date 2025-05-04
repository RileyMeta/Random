#include <stdio.h>

float get_num(char *prompt);

int main(int argc, char* argv[]) {
    float sum = 0;
    char buffer[256];

    int num = get_num("How many grades are you averaging? ");

    for (int i = 1; i < num + 1; i++) {
        snprintf(buffer, sizeof(buffer), "Enter grade %i: ", i);
        float grade = get_num(buffer);
        sum += grade;
    }

    float final = sum / num;

    printf("The average of the %i grades is: %.2f\n", num, final);

    return 0;
}

float get_num(char *prompt) {
    char buffer[256];
    float num;

    do {
        printf("%s", prompt);

        if (fgets(buffer, sizeof(buffer), stdin)) {
            if (sscanf(buffer, "%f", &num) == 1) {
                return num;
            } else {
                printf("Invalid Inpuit: Not an Integer\n");
                continue;
            }
        }

    } while (1);
}
