#include <stdio.h>

int main() {
    int num1, num2;

    printf("Digite o primeiro numero: ");
        scanf("%d", &num1);
    printf("Digite o segundo numero: ");
        scanf("%d", &num2);
    printf("Ordem crescente: ");
    if (num1 < num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }
    printf("Ordem decrescente: ");
    if (num1 > num2) {
        printf("%d, %d\n", num1, num2);
    } else {
        printf("%d, %d\n", num2, num1);
    }
    return 0;
}
