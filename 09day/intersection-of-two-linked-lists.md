**思路**
利用两个指针走A+B+C长度一定会相交，找出那个相交点
**代码**
```C++
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA == NULL || headB == NULL){
            return NULL;
        }
        ListNode *hA = headA;
        ListNode *hB = headB;
        while(hA != hB)
        {
            hA = hA == NULL ? headB : hA->next;
            hB = hB == NULL ? headA : hB->next;
        }
        return hA;
    }
};
```
**复杂度**
时间复杂度：遍历链表O（N）
空间复杂度：O（1）