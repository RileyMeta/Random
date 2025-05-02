#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

const char VERSION[] = "0.1";

// Actual Functions
double ctof(char *temp);
double ftoc(char *temp);

// Command line args
void help_menu(char *name);
void version_info(char *name);

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <F/C> <temperature>\n", argv[0]);
        printf("For more info, try %s --help\n", argv[0]);
        return 1;
    }

    if (strcmp(argv[1], "--help") == 0) {
        help_menu(argv[0]);
    } else if (strcmp(argv[1], "--version") == 0 || strcmp(argv[1], "-V") == 0) {
        version_info(argv[0]);
    } else if (strcmp(argv[1], "-F") == 0 || strcmp(argv[1], "-f") == 0) {
        if (argv[2]) {
            ctof(argv[2]);
        } else {
            printf("Error! Missing temperature value for %s\n", argv[1]);
            return 1;
        }
    } else if (strcmp(argv[1], "-C") == 0 || strcmp(argv[1], "-c") == 0) {
        if (argv[2]) {
            ftoc(argv[2]);
        } else {
            printf("Error! Missing temperature value for %s\n", argv[1]);
            return 1;
        }
    } else {
        printf("Error! Unknown argument: %s\n", argv[1]);
        return 1;
    }

    return 0;
}

double ctof(char *temp) {
    double c = atof(temp);
    double return_temp = (c * 9.0 / 5.0) + 32;
    printf("%sC is %.2fF\n", temp, return_temp);
    return return_temp;
}

double ftoc(char *temp) {
    double f = atof(temp);
    double return_temp = (f - 32) * 5.0 / 9.0;
    printf("%sF is %.2fC\n", temp, return_temp);
    return return_temp;
}

void help_menu(char *name) {
    printf("Usage: %s <F/C> <temperature>\n", name);
    printf("  -F will convert to Fahrenheit\n");
    printf("  -C will convert to Celsius\n");
}

void version_info(char *name) {
    printf("%s Version %s\n", name, VERSION);
}
