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

	while (a && b)
	{
		if (b->next == NULL)
			return (0);
		a = a->next;
		b = b->next;
		if (a == b)
			return (1);
	}
	return (0);
}
