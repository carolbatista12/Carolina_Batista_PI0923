#include <stdio.h>

int main() {
    float notas[10], soma = 0, media;
    int i, acima = 0;
    for (i = 0; i < 10; i++) {
        printf("Nota do aluno %d: ", i + 1);
        scanf("%f", &notas[i]);
        soma += notas[i];
    }
    media = soma / 10;
    for (i = 0; i < 10; i++) {
        if (notas[i] >= media)
            acima++;
    }
    printf("Media da turma: %.2f\n", media);
    printf("Alunos com nota igual ou acima da media: %d\n", acima);
    return 0;
}

