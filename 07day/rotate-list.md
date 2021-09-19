**思路**
找到k的位置，进行分割
k后面的尾部挪到头部，k指向null
****
```C++
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        //boundary condition
        if(head == nullptr || head->next == nullptr || k == 0){
            return head;
        }
        ListNode * p = head;
        int len = 0;
        while(p->next != nullptr)
        {
            p = p->next;
            len++;
        }
        k %= len;
        ListNode *fa = head;
        ListNode *sl = head;
        
        while (fa->next != nullptr) {
            if (k-- <= 0) {
                sl = sl->next;
            }
            fa = fa->next;
        }
        fa->next = head;
        ListNode* rehead = sl->next; //make sl->next as the head
        sl->next = nullptr; //make sl-nest as the tail 
        return rehead;
        }
};

```
**复杂度**
时间复杂度：O（N）
空间复杂度：O（1）