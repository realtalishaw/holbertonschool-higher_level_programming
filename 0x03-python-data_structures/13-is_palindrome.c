#include "lists.h"

/**
 * is_palindrome - fjjfs
 * @head: dfsd
 *
 * Returns: fdsd
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	char buffer[10000];
	int i = 0;
	int end = 0;


	if (!*head || !head)
		return (1);

	tmp = *head;
	if (!tmp->next)
		return (1);

	while (tmp)
	{
		buffer[end] = tmp->n;
		tmp = tmp->next;
		end++;
	}

	end = end - 1;
	for (; end >= 0 && i <= end; end--, i++)
	{
		if (buffer[end] != buffer[i])
			return (0);
	}
	return (1);
}
