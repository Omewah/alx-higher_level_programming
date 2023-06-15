#include "lists.h"

/**
 * check_cycle - a function that checks if a singly LL has a cycle in it
 * @list: singly linked list
 * Return: 0 no cycle. Else, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cat = list, *mice = list;

	while (cat && mice)
	{
		if (mice->next == NULL)
			return (0);
		cat = cat->next;
		mice = mice->next->next;
		if (cat == mice)
			return (1);
	}

	return (0);
}
