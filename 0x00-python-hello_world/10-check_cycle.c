#include "lists.h"
/**
*check_cycle - check cycle
*@list: pointer to node
*Return: 0 if no cycle, 1 if else
*/

int check_cycle(listint_t *list)
{
listint_t *start;
listint_t *temp;
if (list == NULL || list->next == NULL)
return (0);
start = list->next;
temp = list->next->next;

while (start != NULL && temp != NULL && temp->next != NULL)
{
if (start == temp)
return (1);

start = start->next;
temp = temp->next->next;
}
return (0);
}
