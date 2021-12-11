**思路**
1、所有异或找出两个数不同的位
2、以最小的位将两个数分为两组
3、通过异或得到两数
**代码(C++)**
```C++
实现语言: C++
C++ Code:

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        
// 1. xor(a, a) = 0
//2. xor(a, 0) = xor(0, a) = a
//3. xor(1, 1) = xor(0, 0) = 0
//4. xor(1, 0) = xor(0, 1) = 1
///5. xor(a, b) = c => xor(a, c) = b and xor(b, c) = a  
///     calculate c = a^ b
        int bitTwoNum =0; 
        for(auto & it : nums)
            bitTwoNum =(bitTwoNum ^ it) ; 
        
///  find c right most 
        int rightMost = 1; 
        while(  !(bitTwoNum & rightMost ) )
        {
            rightMost = rightMost << 1; 
        }

//  get a or b.         
        int bitOneNum =0; 
        for(auto & it : nums)
        {
            if( it & rightMost)
            {
                bitOneNum =(bitOneNum ^ it); 
            }
        }
//  get another b or a         
        return {bitOneNum , bitOneNum ^ bitTwoNum} ; 
        
    }
};
```
**复杂度分析**
时间复杂度: O(N)
空间复杂度: (1)