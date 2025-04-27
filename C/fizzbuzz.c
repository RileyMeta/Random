#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int times = 100;

    if (argc > 1) {
        times = atoi(argv[1]);
    }

    for (int i = 1; i < times; ++i) {
        if (i % 3 == 0 && i % 5 == 0) {
            printf("FizzBuzz\n");
        } else if (i % 3 == 0) {
            printf("Fizz\n");
        } else if (i % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%d\n", i);
        }
    }
    return 0;
}
