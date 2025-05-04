#include <stdio.h>

int main(int argc, char* argv[]) {
    int numbers[] = {1, 10, 20, 50, 100, 500, 1000};

    for (int i = 0, n = sizeof(numbers) / sizeof(numbers[0]); i < n; i++) {

        if (numbers[i] == 50) {
            printf("Found!\n");
            return 0;
        }
        printf("%i\n", i);
    }

    printf("Not Found!\n");
    return 1;
}
