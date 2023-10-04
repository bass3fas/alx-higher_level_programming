#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - node in sorted list
 * @head: first node pointer
 * @number: number to add
 * Return: ptr to the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    if (*head == NULL || number < (*head)->n)
    {
        // Insert at the beginning
        new->next = *head;
        *head = new;
        return *head;
    }

    new->n = number;
    new->next = NULL;
    while (current->next != NULL && current->next->n < number)
	current = current->next;
    new->next = current->next;
    current->next = new;
    return(*head);
}
