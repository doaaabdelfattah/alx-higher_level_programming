#include "lists.h"
/**
 * insert_node - function insert nu into sorted SL list
 * @head: pointer to head pointer
 * @number: number to be intered
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *tmp, *prev;
tmp = prev = *head;
// if (*head == NULL)
// return (NULL);
/* create the new node with the provided number */
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;

/*inserting the new node at the beginning */
if (tmp == NULL || tmp->n >= number)
{
    new_node->next = tmp;
    *head = new_node;
    return (new_node);
}

while (tmp != NULL && tmp->n < number)
{
prev = tmp;
tmp = tmp->next;
}
/* Connect the new node to the list */
prev->next = new_node; /*left side*/
new_node->next = tmp; /* right side*/
return (new_node);
}
