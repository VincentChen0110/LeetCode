class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode;
        dummy->next = head;
        ListNode* cur = dummy;
        while (cur->next){
            if(cur->next->val==val){
                cur->next = cur->next->next;
            }
            else{
                cur = cur->next;
            }
        }
        return dummy->next;
    }
};