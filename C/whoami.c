#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

void info_menu();
void help_menu();
void invalid(char *arg);

const char VERSION[] = "0.1";

int main(int argc, char* argv[]) {
    char *username = getlogin();
    if (username == NULL) {
        perror("getlogin");
        return 1;
    }

    if (argc >= 2) {
        if (strcmp(argv[1], "--version") == 0 || strcmp(argv[1], "-V") == 0) {
            info_menu();
            return 0;
        } else if (strcmp(argv[1], "--help") == 0) {
            help_menu();
            return 0;
        } else {
            invalid(argv[1]);
            return 1;
        }
    }

    printf("%s\n", username);
    return 0;
}

void info_menu(void) {
    printf("whoami (Riley's coreutils) %s\n", VERSION);
    printf("Copyright (C) 2025 Riley Ava\n");
    printf("License MIT: <put the link here, dingus>\n");
    printf("This is free software: you are free to change and redistribute it.\n");
    printf("There is NO WARRANTY, to the extent permitted by law.");
    printf("\n\nWritten by Riley Ava.\n");
}

void help_menu(void) {
    printf("Usage: whoami [OPTION]...\n");
    printf("Print the user name associated with the current effective user ID.\n");
    printf("Same as id -un\n");
    printf("\n\t--help\t\tdisplay this help and exit");
    printf("\n\t--version, -V\toutput version information and exit\n");
    printf("\n\nOnline Help: <I'll update this later>\n");
}

void invalid(char *arg) {
    printf("whoami: invalid option -- \'%s\'\n", arg);
    printf("Try \'whoami --help\' for more information.\n");
}
