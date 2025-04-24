#include <stdio.h>

int main() {
    float n1, n2, n3, media;

    printf("Digite as 3 notas do aluno:\n");
    scanf("%f %f %f", &n1, &n2, &n3);

    media = (n1*2 + n2*3 + n3*5) / 10;

    printf("Media final: %.2f\n", media);
    if (media >= 6)
        printf("APROVADO\n");
    else
        printf("REPROVADO\n");

    return 0;
}

