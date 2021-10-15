**思路**
利用快慢指针每次取中点作为二叉树的节点，利用递归到叶子节点
**代码**
```C++
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if(head == nullptr) return nullptr;
        return sortedListToBST(head, nullptr);

    }
    TreeNode* sortedListToBST(ListNode* head, ListNode* tail)
    {
        if(head == tail) return nullptr;
        ListNode* fast = head;
        ListNode* slow = head;
        while(fast != tail && fast->next != tail){
            slow = slow->next;
            fast = fast->next->next; 
        }

        TreeNode* root = new TreeNode(slow->val);
        root->left = sortedListToBST(head, slow);
        root->right = sortedListToBST(slow->next, tail);
        return root;
    }
};
```
**复杂度**
时间复杂度：遍历链表O（NlogN）
空间复杂度：O（logN）