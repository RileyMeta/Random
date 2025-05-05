#include <stdio.h>

void selection_sort(int arr[], int size);
void print_array(int arr[], int size);

int main(int argc, char* argv[]) {
    int grades[] = {98, 80, 100, 59, 75, 94, 60, 99}; // Generated via RNG
    int size = sizeof(grades) / sizeof(grades[0]);

    printf("Original Array:\n");
    print_array(grades, size);

    printf("Sorted Array:\n");
    selection_sort(grades, size);
    print_array(grades, size);

    return 0;
}

void selection_sort(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        int min_index = i;

        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }

        if (min_index != i) {
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }

    }
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
