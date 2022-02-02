/* Nama : Rafi Adi Pramana 
   NIM : 3.34.21.2.20 
   Kelas : IK-1C */

#include<stdio.h>

int main() {

    /* Deklarasi Variabel */
    int a, b;
    char operator;

    /* Memasukan Inputan Angka */
    printf("Input angka pertama = ");
    scanf("%d",&a);
    printf("Input angka kedua = ");
    scanf("%d",&b);

    /* Memasukan Inputan Operator */
    printf("Input simbol operator = ");
    scanf(" %c", &operator);

    /* Menjakankan Switch dari Beberapa Syntax */
    switch(operator) {
        case '+' : printf("Hasil adalah %d", a+b); break;
        case '-' : printf("Hasil adalah %d", a-b); break;
        case '/' : printf("Hasil adalah %d", a/b); break;
        case '*' : printf("Hasil adalah %d", a*b); break;
        case '%' : printf("Sisa bagi adalah %d", a%b); break;
        default: printf("Operasi tidak dikenal");
    }
}