#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head; /* Current node pointer */
	int i, count, j;
	int elements[2048]; /* Array to store elements of the list */

	if (current_node == NULL) /* If the list is empty, it's a palindrome */
		return (1);

	/* Counting the number of elements in the list */
	for (count = 0; current_node != NULL; count++,
			current_node = current_node->next)
		;

	/* If the list has only one element, it's a palindrome */
	if (count == 1)
		return (1);

	current_node = *head; /* Resetting the current node pointer */

	/* Storing the elements of the first half of the list in an array */
	for (i = 0; i < count / 2; i++, current_node = current_node->next)
		elements[i] = current_node->n;

	/* Checking if the list has odd number of elements */
	if (count % 2 != 0)
		current_node = current_node->next;

	for (j = i - 1; j >= 0; j--, current_node = current_node->next)
		if (elements[j] != current_node->n)
			return (0);

	return (1); /* If it passes all conditions, it's a palindrome */
}
