**思路**
采用官方思路：利用单调栈存储
遇到一个数小于栈的最大值，只保留最大值，否则就相当于增加一个块
弹出递增的，以前的递增会因为一个低值而必须把这个低值包含进去
**代码**
```C++
class Solution {
public:
     int maxChunksToSorted(vector<int>& arr) {
        stack<int> stack;
        for(int i =0;i<arr.size();i++){
            if(!stack.empty()&&stack.top()>arr[i]){
                //遇到一个数小于栈的最大值，只保留最大值，否则就相当于增加一个块
                int max = stack.top();
                //弹出递增的，以前的递增会因为一个低值而必须把这个低值包含进去
                while(!stack.empty()&&stack.top()>arr[i]){
                    stack.pop();
                }
                stack.push(max);
            }else{
                stack.push(arr[i]);
            }
        }
        return stack.size();
    }
};

```
**复杂度**
时间复杂度：遍历O（N）
空间复杂度：栈存储，最大O（N）