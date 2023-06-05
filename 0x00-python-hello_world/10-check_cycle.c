#include "lists.h"

/**
 * check_cycle - a function that checks if a singly LL has a cycle in it
 * @list: singly linked list
 * Return: 0, no cycle. Else, 1
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (list == NULL)
		return (0);

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;
		if (a == b)
			return (1);
	}
	return (0);
}
