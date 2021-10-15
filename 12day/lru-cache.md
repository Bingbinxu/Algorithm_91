**思路**
利用双向链表+hashmap，设计缓存机制
**代码**
```C++
class DLinkedListNode {
public:
    int key;
    int value;
    DLinkedListNode *prev;
    DLinkedListNode *next;
    DLinkedListNode() : key(0), value(0), prev(NULL), next(NULL) {};
    DLinkedListNode(int k, int val) : key(k), value(val), prev(NULL), next(NULL) {};
};
class LRUCache {
public:
    LRUCache(int capacity) :capacity(capacity) {
        dummy_head = new DLinkedListNode();
        dummy_tail = new DLinkedListNode();
        dummy_head->next = dummy_tail;
        dummy_tail->prev = dummy_head;

    }
    
    int get(int key) {
        if(!key_exists(key)){
            return -1;
        }
        DLinkedListNode *node = key_node_map[key];
        move_to_head(node);
        return node->value;

    }
    
    void put(int key, int value) {
         if (key_exists(key)) {
            // key 存在的情况
            DLinkedListNode *node = key_node_map[key];
            node->value = value;
            move_to_head(node);
        } else {
            // key 不存在的情况：
            // 1. 如果缓存空间满了，先删除尾节点，再新建节点
            // 2. 否则直接新建节点
            if (is_full()) {
                DLinkedListNode *tail = dummy_tail->prev;
                remove_node(tail);
                key_node_map.erase(tail->key);
            }

            DLinkedListNode *new_node = new DLinkedListNode(key, value);
            add_to_head(new_node);
            key_node_map[key] = new_node;
        }
    }
private:
    unordered_map<int, DLinkedListNode*> key_node_map;
    DLinkedListNode *dummy_head;
    DLinkedListNode *dummy_tail;
    int capacity;

    void move_to_head(DLinkedListNode *node) {
        remove_node(node);
        add_to_head(node);
    };

    void add_to_head(DLinkedListNode *node) {
        DLinkedListNode *prev_head = dummy_head->next;

        dummy_head->next = node;
        node->prev = dummy_head;

        node->next = prev_head;
        prev_head->prev = node;
    };

    void remove_node(DLinkedListNode *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        node->prev = node->next = NULL;
    };

    bool key_exists(int key) {
        return key_node_map.count(key) > 0;
    };

    bool is_full() {
        return key_node_map.size() == capacity;
    };
};
```
**复杂度**
时间复杂度：各种操作平均都是 O(1)
空间复杂度：链表占用空间 O(N)，哈希表占用空间也是 O(N)，因此总的空间复杂度为 O(N)，其中 N 为容量大小