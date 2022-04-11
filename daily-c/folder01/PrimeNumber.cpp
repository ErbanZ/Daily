#include <stdio.h>

int main()
{
    int flag = 1;
    int p;
    scanf("%d", &p);
    for(int i = 2; i*i <= p; i++)
    {
	if(p % i) continue;
	flag = 0;
        printf("%d isn't Prime Number\n", p);
	return 0;
    }
    printf("%d is Prime Number\n", p);
    return 0;
}



