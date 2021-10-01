**思路**
官方思路：根据每个点作为回旋镖的定点，然后迭代地去找所有的距离，并用map取存储，这样就是惟一的
然后遍历所有的map的value，并用n*(n-1)计算所有的可能性
**代码**
```C++
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int length = points.size();

        if(points.empty() || length <= 2)
        {
            return 0;
        }
        int res = 0;
        map<int,int> ec;
        for(int i = 0;i < length;i++)
        {
            for(int j = 0;j < length;j++)
            {
                int dis = getdis(points[i],points[j]);
                ec[dis] += 1;
            }
            map<int, int>::iterator it;
            for(it = ec.begin(); it != ec.end(); it++)
            {
                res += it->second * (it->second - 1);
            }
            ec.clear();
        }
        return res;
    }

private:
    int getdis(vector<int> x, vector<int> y)
    {
        int x1 = y[0] - x[0];
        int y1 = y[1] - x[1];
        return x1*x1 +y1*y1;
    }

};
```
**复杂度**
时间复杂度：排序算法O（N2）
空间复杂度：存储所有的节点O（N）