#include "lists.h"

/**
 *insert_node- jfsljej
 *@head: knjfsds
 *@number: jklejfed
 *Return: kjedds
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nxt, *newnode;
	listint_t *prev = NULL;

	if (!head)
		return (NULL);

	newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);

	newnode->n = number;

	if (!(*head))
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}

	if (number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}

	nxt = *head;

	while (nxt && nxt->n <= number)
	{
		prev = nxt;
		nxt = nxt->next;
	}

	newnode->next = nxt;
	prev->next = newnode;
	return (newnode);
}
