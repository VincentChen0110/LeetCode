class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode *dummy = new ListNode(0, head);
        ListNode *prev = dummy;
        for(int i = 0; i<left-1; i++) prev = prev->next;
        ListNode* cur = prev->next;
        ListNode* node = NULL;
        for(int i= 0; i<right-left; i++){
            ListNode* nxt = prev->next;
            prev->next = cur->next;
            cur->next = cur->next->next;
            prev->next->next = nxt;
        }

        return dummy->next;
    }
};