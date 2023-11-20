#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: 1 if it is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first_half = *head;
	/* If list is null or one node only so it's Palindrome */
	if (!*head || !(*head)->next)
		return (1);

	slow = *head;
	fast = *head;
	/* STEP 1: Traverese to the middle of the link */
	while (fast != NULL && fast->next != NULL)
		/* Iterate untill the fast pointer reach the last or next to last node*/
	{
		/* FAST pointer move by two steps */
		fast = fast->next->next;
		/* SLOW pointer move by one step */
		slow = slow->next;
	}
	/* if fast reach to null, this means even linked list */
	/* We have to move the slow one more step to point to the next half */
	/* STEP 2: Reverse the second half */
    if (fast)
		slow = reverse_list(&slow);
	else
	{
		slow = slow->next;
		slow = reverse_list(&slow);
	}
    /* STEP 3: Check if two halfs are palindrome */
	while (slow != NULL)
	{
		if (first_half->n != slow->n)
			return (0);

		first_half = first_half->next;
		slow = slow->next;
	}

	return (1);
}
/**
 * reverse_list - reverse linked list
 * @head: pointer to the head of the linked list.
 * Return: pointer to the new reversed list
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
