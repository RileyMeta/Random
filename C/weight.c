// Simple CLI Weight converter
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char VERSION[] = "0.1";

void help_menu(char *a);
void version_info(char *a);

float metric(float a);
float imperial(float a);

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <I/i/M/m> <weight>\n", argv[0]);
        return 1;
    }

    float weight;

    if (argc > 2)
        weight = atof(argv[2]);

    float result;

    if (strcmp(argv[1], "--help") == 0) {
        help_menu(argv[0]);
    } else if (strcmp(argv[1], "-V") == 0 || strcmp(argv[1], "--version") == 0) {
        version_info(argv[0]);
    } else if (strcmp(argv[1], "-m") == 0 || strcmp(argv[1], "-M") == 0) {
        result = metric(weight);
        printf("%.2flbs is %.2fkg\n", weight, result);
    } else if (strcmp(argv[1], "-i") == 0 || strcmp(argv[1], "-I") == 0) {
        result = imperial(weight);
        printf("%.2fkg is %.2flbs\n", weight, result);
    } else {
        printf("Unknown option: %s\n", argv[1]);
        return 1;
    }

    return 0;
}

void help_menu(char *a) {
    printf("Usage:\n");
    printf(" %s <measurement> <weight>\n", a);
    printf("  -M -m\tConvert measurement to Metric\n");
    printf("  -I -i\tConvert measurement to Imperial\n");
    printf("  -V --version\tShow version info\n");
    printf("     --help\tShow this menu\n");
}

void version_info(char *a) {
    printf("%s Version %s\n", a, VERSION);
}

float metric(float a) {
    return a * 0.453592;
}

float imperial(float a) {
    return a / 2.205;
}
