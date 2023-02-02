#include <stdio.h>
int a = 50;
int b = 60;
int c = 70;
void func(void){
    static int a = 200;
    int b = 500;
    a++;
    b++;
    c=a;
}
int main(void){
    func();
    func();
    printf("a = %d, b = %d, c = %d", a, b, c);

}