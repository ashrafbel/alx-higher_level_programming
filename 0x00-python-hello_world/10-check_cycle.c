#include"lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * check_cycle - checks if a singly linked list is cycle
 * @list: pointer to the head of the linked list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
listint_t *SLOW_ = list;
listint_t *FAST_ = list;

while (SLOW_ && FAST_ && FAST_->next)
{
SLOW_ = SLOW_->next;
FAST_ = FAST_->next->next;
if (SLOW_ == FAST_)
return (1);
}
return (0);
}
