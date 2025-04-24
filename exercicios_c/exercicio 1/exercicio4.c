#include <stdio.h>

int main() {
    float saldo, cheque;

    printf("Digite o saldo do cliente: ");
    scanf("%f", &saldo);
    printf("Digite o valor do cheque: ");
    scanf("%f", &cheque);

    if (cheque > saldo) {
        printf("Cheque NA pode ser descontado. Saldo insuficiente.\n");
    } else {
        saldo -= cheque;
        printf("Cheque descontado. Novo saldo: %.2f\n", saldo);
    }

    return 0;
}

