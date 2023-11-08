#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *cur, *prev, *next;
	prev = NULL;
	next = NULL;
	cur = *head;
	while (cur != NULL)
	{
		/* Store Next Node */
		next = cur->next;
		/* Reverse currrent node pointer */
		cur->next = prev;
		/* Move pointers ahead */
		prev = cur;
		cur = next;
	}
	*head = prev;
	return (*head);
}
size_t list_len(listint_t *h)
{
	int count;
	count = 0;
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}

int is_palindrome(listint_t **head)
{
	listint_t *start, *mid, *new_mid;
	size_t len, i;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	start = mid = *head;
	len = list_len(*head);
	/* Traverse the mid pointer to the middle*/
	for (i = 0; i < (len / 2) - 1; i++)
	{
		mid = mid->next;
	}
	/*if ((len % 2) == 0 && mid->n != mid->next->n)
	  return (0);*/


	/* Reverse the list */
	new_mid = reverse_list(&mid);
	print_listint(*head);
	while (new_mid)
	{
		if (new_mid->n != start->n)
			return (0);
		new_mid = new_mid->next;
		start = start->next;
	}
	reverse_list(&mid);
	return (1);
}
