#include "lists.h"

/**
 *insert_node- jfsljej
 *@head: knjfsds
 *@number: jklejfed
 *Return: kjedds
 */

listint *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp = *head, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!*head)
	{
		*head = new;
		return (new);
	}

	if (temp->n > number)
	{
		node->next = *head;
		*head = new;
	}

	else
	{
		while (temp)
		{
			if (temp->n > number)
				break;
			current = temp;
			temp = temp->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
