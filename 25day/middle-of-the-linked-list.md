**思路**
利用双指针负责找到中点，快指针每次2格，慢指针每次一格，快指针到终点，慢指针到中点
**代码**
```C++
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast != nullptr && fast->next != nullptr)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;

    }
};
```
**复杂度**
时间复杂度：遍历数组O(N)
空间复杂度：O(1)
