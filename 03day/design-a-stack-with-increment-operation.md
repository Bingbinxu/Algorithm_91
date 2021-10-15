**思路**
确定好边界条件，利用top实时更新大小
**代码**
```C++
class CustomStack {
    vector<int> stack;
    int top;
public:
    CustomStack(int maxSize) {
       stack.resize(maxSize);
       top = -1;

    }   
    void push(int x) {
        if(top != stack.size() - 1)
        {
            top++;
            stack[top] = x;

        }
    }
    int pop() {
        if(top == -1)
        {
            return -1;
        }
        top--;
        return stack[top + 1];
    }
    void increment(int k, int val) {
        int limit = min(k, top + 1);
        for(int i = 0;i < limit;i++)
        {
            stack[i] += val;
        }
    }
};

```
**复杂度**
时间复杂度：push和pop是O（1），incresement是O(k,top+1)
空间复杂度：O（1）