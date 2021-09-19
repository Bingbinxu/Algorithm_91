**思路**
一次处理四个节点，只交换中间两个节点，两边的节点用于保证链表顺序
**代码**
```C++
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *prenode = new ListNode(-1, head);
        ListNode *prev = prenode;
        ListNode *cur = prev->next;

        while(cur != nullptr && cur->next != nullptr){
            ListNode *next = cur->next;
            cur->next = next->next;
            next->next = cur;
            prev->next = next;
            prev = cur;
            cur = cur->next;
        }
        return prenode->next;
    }
};
```
**复杂度**
时间复杂度：遍历链表O（N）
空间复杂度：O（1）