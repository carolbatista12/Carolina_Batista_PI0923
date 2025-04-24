#include <stdio.h>

int main() {
    char nome[50];
        float valor, desconto, total;
        int percentual;
        printf("Nome do cliente: ");
        scanf(" %[^\n]", nome);
        printf("Valor da compra: ");
        scanf("%f", &valor);
    if (valor <= 200) {
        percentual = 10;
    } else if (valor <= 500) {
        percentual = 15;
    } else {
        percentual = 20;
    }
    desconto = valor * percentual / 100.0;
    total = valor - desconto;
        printf("\nCliente: %s\n", nome);
        printf("Valor da compra: %.2f€\n", valor);
        printf("Desconto: %d%% (%.2f€)\n", percentual, desconto);
        printf("Total a pagar: %.2f€\n", total);
    return 0;
}

