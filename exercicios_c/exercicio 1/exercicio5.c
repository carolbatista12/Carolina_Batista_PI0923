#include <stdio.h>

int main() {
    int num1, num2, num3, maior, meio, menor;

    printf("Digita tres numeros inteiros:\n");
    scanf("%d %d %d", &num1, &num2, &num3);
    if (num1 <= num2 && num1 <= num3) {
    menor = num1;
    if (num2 <= num3) {
        meio = num2;
        maior = num3;
    } else {
        meio = num3;
        maior = num2;
    }
} else if (num2 <= num1 && num2 <= num3) {
    menor = num2;
    if (num1 <= num3) {
        meio = num1;
        maior = num3;
    } else {
        meio = num3;
        maior = num1;
    }
} else {
    menor = num3;
    if (num1 <= num2) {
        meio = num1;
        maior = num2;
    } else {
        meio = num2;
        maior = num1;
    }
}
    printf("Crescente: %d, %d, %d\n", menor, meio, maior);
    printf("Decrescente: %d, %d, %d\n", maior, meio, menor);

    return 0;
}

