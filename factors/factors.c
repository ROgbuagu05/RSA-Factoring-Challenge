#include <stdio.h>
/**
 * find_divisor - finds the smallest divisor of a number.
 * @num: number to find the smallest divisor for.
 * Return: smallest divisor if found, or 0 if the number is prime.
 */
int find_divisor(long int num)
{
	long int factor;

	if (num % 2 == 0)
	{
		printf("%lu = %lu * 2\n", num, num / 2);
		return (2);
	}

	factor = 3;
	while (factor * factor <= num)
	{
		if (num % factor == 0)
		{
			 printf("%lu = %lu * %lu\n", num, num / factor, factor);
			 return (factor);
		}
		else
		{
			factor += 2;
		}
	}

	printf("%lu = %lu * 1\n", num, num);
	return (0);
}
