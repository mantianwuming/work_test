#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL) 
            return true;   //空链表表或链表只有一个元素
        ListNode *node = head;
        int nums = 0;
        while (node != NULL){
            nums += 1;
            node = node->next;
        }
        int mid = nums/2;
        int i = 0;
        node = head;
        ListNode* before_node = NULL;
        ListNode* next_node;
        while (i < mid){
            next_node = node->next;
            node->next = before_node;
            before_node = node;
            node = next_node;
            i += 1;
        }
        ListNode* l;
        ListNode* r;
        if(nums % 2 == 0){
            l = before_node;
            r = node;
        }
        else{
            l = before_node;
            r = node->next;
        }
        while (l != NULL and r != NULL){
            if (l->val != r->val)
                return false;
            l = l->next;
            r = r->next;
        return true;
        }
    }
};
