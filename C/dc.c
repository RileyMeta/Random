// Distance Converter (Kilometers/Miles)
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char VERSION[] = "0.1";

float miles(float distance);
float kilos(float distance);

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <M/m/K/k> <distance>\n", argv[0]);
        return 1;
    }

    float distance;
    float result;

    if (argv[2]) {
        float distance = atof(argv[2]);
    }

    if (strcmp(argv[1], "-m") == 0 || strcmp(argv[1], "-M") == 0) {
        result = miles(distance);
        printf("%.1f km is %.1f miles\n", distance, result);
    } else if (strcmp(argv[1], "-k") == 0 || strcmp(argv[1], "-K") == 0) {
        result = kilos(distance);
        printf("%.1f miles is %.1f km\n", distance, result);
    } else if (strcmp(argv[1], "-V") == 0 || strcmp(argv[1], "--version") == 0) {
        printf("%s Version %s\n", argv[0], VERSION);
        return 0;
    } else if (strcmp(argv[1], "--help") == 0) {
        printf("%s\n", argv[0]);
        printf("     --help\t Display this menu\n");
        printf("  -M -m \t Convert to Miles\n");
        printf("  -K -k \t Convert to Kilometers\n");
        printf("  -V --version\t Display the version info\n");
        return 0;
    } else {
        printf("Unknown Input: %s\n", argv[1]);
        return 1;
    }

    return 0;
}

float miles(float distance) { // Return Miles (from Km)
    return distance / 1.60934;
}

float kilos(float distance) { // Return Km (from miles)
    return distance * 1.60934;
}
