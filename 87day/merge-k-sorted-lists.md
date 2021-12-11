**思路**
构建一个小顶堆，重写排序方法，将每个链表的第一个元素放到小顶堆
依次取出最小值，直到没有next
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty())
        return nullptr;
        ListNode *res;
        //重定义比较方式
        auto cmp = [](ListNode* n1, ListNode* n2)
        {
            return n1->val>n2->val;
        }
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> k(cmp);
        for (auto& list : lists)
        {
            if (list != nullptr)
            {
                k.push(list);
            }
        }
        ListNode* fakeHead = new ListNode(-1);  /* 创建虚拟头结点 */
        ListNode* cur = fakeHead;
        while (!k.empty()) 
        {
            cur->next = k.top();  
            cur = cur->next;
            k.pop();

            if (cur->next != nullptr)  
            {
                k.push(cur->next);
            }
        }
        return fakeHead->next;
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
