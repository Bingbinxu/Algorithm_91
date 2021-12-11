**思路**
跳表查询，插入和删除
**代码(C++)**
```C++
实现语言: C++
struct Node {
    Node *right, *down;
    int val;
    Node(Node* right, Node* down, int val): right(right), down(down), val(val) {}
};

class Skiplist {
    Node* head;
    vector<Node*> insertPoints;    
    
public:
    Skiplist() { 
        head = new Node(nullptr, nullptr, 0); 
    }    
    bool search(int target) {
        Node* p = head;
        while (p)
        {
            while (p->right && p->right->val < target) /* 找当前层的1个适合的区间: 如果p->right变成NULL或target <= p->right结点的值时说明找到合适位置了, 否则继续右移 */
                p = p->right;
            if (!p->right || p->right->val > target) // 没找到, 就继续到下1层去找
                p = p->down;
            else
                return true;
        }
        return false;
    }
    void add(int num)
    {
        insertPoints.clear();
        Node* p = head;
        while (p)
        {
            while (p->right && p->right->val < num)
                p = p->right;
            insertPoints.push_back(p);
            p = p->down;
        }

        Node* downNode = nullptr;
        bool insertUp = true;
        while (insertUp && insertPoints.size())
        {
            Node* ins = insertPoints.back();
            insertPoints.pop_back();

            ins->right = new Node(ins->right, downNode, num);
            downNode = ins->right;

            insertUp = (rand() & 1) == 0; // 50% 的可能性
        }
        if (insertUp) // 创建一个新的layer
        {
            head = new Node(new Node(nullptr, downNode, num), head, 0);
        }
    }
    bool erase(int num)
    {
        Node* p = head;
        bool seen = false;  // 跳表中是否存在要删的值
        while (p)
        {
            while (p->right && p->right->val < num)
                p = p->right;
            if (!p->right || p->right->val > num) // 没找到要删的值, 就继续到下1层去找
                p = p->down;
            else  /* 找到了要删的值, 就删除这个结点 */
            {
                seen = true;
                p->right = p->right->right;
                p = p->down;
            }
        }
        return seen;
    }
};
```
**复杂度分析**
时间复杂度: O(logN)
空间复杂度: O(N）
