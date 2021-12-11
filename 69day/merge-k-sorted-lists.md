**思路**
k路归并
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty())
            return NULL;      
        ListNode* res;
        auto cmp = [](ListNode* n1, ListNode* n2)
        {
            return n1->val > n2->val;
        };
        /* 使用node的val构造一个小顶堆 */
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> nodesQ(cmp);
        for (auto list : lists)
        {
            if (list != NULL)
            {
                nodesQ.push(list);
            }
        }
        ListNode* fakeHead = new ListNode(-1);  /* 创建虚拟头结点 */
        ListNode* cur = fakeHead;
        while (!nodesQ.empty()) 
        {
            cur->next = nodesQ.top();  /* 取出最小值对应的结点指针，挂接在游标指针上 */
            cur = cur->next;
            nodesQ.pop();

            if (cur->next != NULL)  /* 只要挂接点后面还有结点，则将其压入栈，继续从中拿出最小值，循环往复 */
            {
                nodesQ.push(cur->next);
            }
        }
      return fakeHead->next;
    }
};
```
**复杂度分析**
时间复杂度: O(N logN)
空间复杂度: O(N)

**分治思想**
与上面不同
上面维护一个k的小顶堆，不断取最小，将其拿出。
下面分治，先两两合并，然后再两两合并，直到只剩一个
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()) return NULL;
        for(int N = lists.size();N>1;N=(N+1)/2)
        {
            for(int i = 0;i < N /2;i++)
            {
                lists[i] = merge2Lists(lists[i],lists[N - i - 1]);
            }
        }
        return lists[0];
    }
private:
    ListNode* merge2Lists(ListNode* a, ListNode* b) {
        {
             ListNode* fakeHead = new ListNode(-1); 
             ListNode* cur = fakeHead;
             while(a && b)
             {
                 if(a->val < b->val){cur->next = a; a = a->next;}
                 else{cur->next = b; b = b->next;}
                 cur = cur->next;
             }
             cur->next = a?a:b;
             return fakeHead->next;
        }
    }
};