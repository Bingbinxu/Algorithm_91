**方法**
利用横坐标区分，横坐标相同，map不存入
对横坐标排序输出
**代码**
```C++
实现语言: C++
oid bfs(Tree* root, map<int, int>& dict) {
    queue<pair<Tree*, int>> q;
    q.push(make_pair(root, 0));  // queue中存放的是 pair<Tree*, 横向坐标>
    while (!q.empty())
    {
        Tree* node = nullptr;
        int x = 0;
        auto kvp = q.front();
        node = kvp.first;
        x = kvp.second;      
        if (dict.find(x) == dict.end()) //找不到，添加到map
            dict[x] = node->val; // 横向坐标和值建立map (x, val)
        q.pop();
        if (node->left != nullptr) q.push(make_pair(node->left, x - 1));
        if (node->right != nullptr) q.push(make_pair(node->right, x + 1));
    }
}

vector<int> solve(Tree* root) {
    map<int, int> dict;  // 哈希表, 映射: (x, val)
    bfs(root, dict);
    vector<int> res;
    for (auto& kvp : dict)
        res.push_back(kvp.second);
    return res;
}
```
**复杂度分析**
时间复杂度: O(NlogN)，N为树的节点数
空间复杂度: O(N)
