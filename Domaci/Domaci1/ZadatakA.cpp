#include<stdio.h>

int main()
{
	bool found = false;
	long long counter = 0;
	int num1, num2, num3, num4;

	for (num1 = 0; num1 < 712; num1++)
	{
		for (num2 = 0; num2 < 712; num2++)
		{
			for (num3 = 0; num3 < 712; num3++)
			{
				for (num4 = 0; num4 < 712; num4++)
				{
					counter++;

					if ((num1 + num2 + num3 + num4) == 711 &&
						(num1 * num2 * num3 * num4) == 711000000)
					{
						found = true;
						break;
					}
				}
				if (found)
					break;
			}
			if (found)
				break;
		}
		//printf("%lld\n", counter);
		if (found)
			break;
	}

	if (found) {
		printf("%lld\n", counter);
		printf("Cene su: %d, %d, %d, %d", num1, num2, num3, num4);
	}
}