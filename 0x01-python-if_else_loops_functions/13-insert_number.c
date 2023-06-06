#include "lists.h"

/**
 * insert_node - inserts numbers into a sorted singly LL
 * @head: the head of the singly LL
 * @number: data of the new node
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nnode, *x = *head, *y = *head, *z = *head;
	unsigned int a = 0, index = 0;

	nnode = malloc(sizeof(listint_t));
	if (nnode == NULL)
		return (NULL);
	nnode->n = number;
	nnode->next = NULL;

	if (*head == NULL)
	{	nnode->next = *head;
		*head = nnode;
		return (nnode);	}

	while (x->next)
	{	index++;
		z = z->next;
		if (x->n > number)
		{	index--;
			break;	}
		else if (x->next->next == NULL && z->n < number)
		{	index++;
			break;	}
		x = x->next;	}
	if (index == 0)
	{	nnode->next = *head;
		*head = nnode;
		return (nnode);	}
	while (y != NULL && a < index - 1)
	{	y = y->next;
		a++;	}
	if (a == index - 1)
	{	nnode->next = y->next;
		y->next = nnode;
		return (nnode);
	}
	return (NULL);
}
