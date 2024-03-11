#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *chameleon, *cheatah;

	if (list == NULL)
	return (0);

	chameleon = list;
	cheatah = list->next;

	while (cheatah != NULL && cheatah->next != NULL)
	{
	if (cheatah == chameleon)
	return (1);
	chameleon = chameleon->next;
	cheatah = cheatah->next->next;
	}

	return (0);
}
