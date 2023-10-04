#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check cycles in list
 * @list: list to be checked
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *node1 = list;
  listint_t *node2 = list;

  if (list == NULL || list->next == NULL)
    return (0);
  while (node2 != NULL && node2->next != NULL)
  {
    node1 = node1->next;
    node2 = node2->next->next;
    if (node1 == node2)
      return (1);
  }
  return (0);
}
