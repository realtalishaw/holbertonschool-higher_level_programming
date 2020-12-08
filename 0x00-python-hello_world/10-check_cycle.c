#include "lists.h"

/**
 * check_cycle - jlfefs
 * @list: jfjfidsj
 * Return: jgfdr
 */

int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *p;

	p2 = list;
	p = list;

	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;
		if (list == p2)
		{
			list = p;
			p = p2;
			while (1)
			{
				p2 = p;
				while (p2->next != list && p2->next != p)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
