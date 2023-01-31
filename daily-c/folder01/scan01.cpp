#include <stdio.h>

int main()
{
	int n, i=0;
	scanf("%d", &n);
//	if(n < 10)
//	{
//		printf("1");
//		return 0;
//	}
	while(n/10)
	{
		i++;
		n = n / 10;
	}
	printf("%d\n", i+1);
	printf("%d\n", 1/10);
	return 0;

}
