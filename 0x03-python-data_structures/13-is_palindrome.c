#include "lists.h"

/**
 * rev_list - a function that reverses the LL
 * @h: head of the second half
 */

void rev_list(listint_t **h)
{
	listint_t *prev = NULL;
	listint_t *curr = *h;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	*h = prev;
}

/**
 * com_list - compares the elements of the LL
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if equal, Else 0
 */

int com_list(listint_t *h1, listint_t *h2)
{
	listint_t *ls1 = h1;
	listint_t *ls2 = h2;

	while (ls1 != NULL && ls2 != NULL)
	{
		if (ls1->n == ls2->n)
		{
			ls1 = ls1->next;
			ls2 = ls2->next;
		}
		else
		{
			return (0);
		}
	}

	if (ls1 == NULL && ls2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if singly LL is palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, Else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *s, *f, *ps, *lst2, *mid;
	int pel = 1;

	s = f = ps = *head;
	mid = NULL;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (f != NULL && f->next != NULL)
		{
			f = f->next->next;
			ps = s;
			s = s->next;
		}

		if (f != NULL)
		{
			mid = s;
			s = s->next;
		}

		lst2 = s;
		ps->next = NULL;
		rev_list(&lst2);
		pel = com_list(*head, lst2);

		if (mid != NULL)
		{
			ps->next = mid;
			mid->next = lst2;
		}
		else
		{
			ps->next = lst2;
		}
	}

	return (pel);
}
