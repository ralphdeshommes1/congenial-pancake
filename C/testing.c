#include <stdio.h>
#include <ctype.h>
#include <string.h>

void remove_non_alpha(char *input, char *output) {
    int j = 0;
    for (int i = 0; i < strlen(input); i++) {
        if (isalpha(input[i])) {
            output[j++] = input[i];
        }
    }
    output[j] = '\0';  // Null-terminate the output string
}

int main() {
    char input[31];   // Buffer for input, allowing up to 30 characters + null terminator
    char output[31];  // Buffer for output

    printf("Welcome to the Alpha Cleaner program!\n");

    while (1) {
        printf("Please enter a string (up to 30 characters): ");
        fgets(input, sizeof(input), stdin);

        // Manually remove the newline character at the end of the string if present
        int len = strlen(input);
        if (input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }

        // Check if the input length exceeds 30 characters (excluding null terminator)
        if (strlen(input) > 30) {
            printf("Input exceeds 30 characters. Please try again.\n");
            continue;
        }

        remove_non_alpha(input, output);
        printf("Output after removing non-alpha characters: %s\n", output);

        char repeat[4];  // Buffer for repeat response
        printf("Do you want to repeat? (yes/no): ");
        fgets(repeat, sizeof(repeat), stdin);

        // Manually remove the newline character in the repeat response if present
        len = strlen(repeat);
        if (repeat[len - 1] == '\n') {
            repeat[len - 1] = '\0';
        }

        if (strcmp(repeat, "yes") != 0) {
            printf("Thank you for using the Alpha Cleaner program. Goodbye!\n");
            break;
        }
    }

    return 0;
}
