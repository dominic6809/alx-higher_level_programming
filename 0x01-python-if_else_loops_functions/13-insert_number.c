#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to point to the head of the linked list
 * @number: Number to insert
 * Return: Address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;    /* Pointer to new node */
	listint_t *current;     /* Pointer to current node */

	/* Allocate memory for new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);  /* Return NULL if memory allocation failed */

	/* Initialize new node */
	new_node->n = number;
	new_node->next = NULL;

	/* If list = empty or new node should be inserted at the beginning */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse list to find appropriate position to insert new node */
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	/* Insert the new node */
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
