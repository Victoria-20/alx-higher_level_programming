#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - a function
 * @head: the list
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr1, *ptr2, *list_inver, *new;

	ptr1 = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (0);
	new->n = ptr1->n;
	new->next = NULL;
	list_inver = new;

	ptr1 = ptr1->next;
	while (ptr1 != NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (0);
		new->next = list_inver;
		list_inver = new;
		ptr1 = ptr1->next;
	}

	ptr1 = *head;
	ptr2 = list_inver;
	while (ptr1->n == ptr2->n && ptr1->next != NULL && ptr2->next != NULL)
	if (ptr1->next != NULL || ptr2->next != NULL)
		return (0);
	else if (ptr1->n != ptr2->n)
		return (0);

	return (1);
}
