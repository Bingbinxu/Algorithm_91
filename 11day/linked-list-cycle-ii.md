**思路**
利用两个指针计算相交点，可以把空间复杂度降为O(1)
**代码**
```C++
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head;
    ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            fast = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return NULL;
        
    }
};
```
**复杂度**
时间复杂度：遍历链表O（N）
空间复杂度：O（1）