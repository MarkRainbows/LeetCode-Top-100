
# 解题思路
# 要将链表 1 -> 2 -> 3 -> 4 -> Null 反转为 4 -> 3 -> 2 -> 1 -> Null ，
# 需要一个 cur 指针表示当前遍历到的节点；一个 pre 指针表示当前节点的前驱节点；
# 在循环中还需要一个中间变量 temp 来保存当前节点的后驱节点。

# 算法流程：
# 首先 pre 指针指向 Null，cur 指针指向 head；
# 当 cur != Null，执行循环。
# 先将 cur.next 保存在 temp 中防止链表丢失：temp = cur.next
# 接着把 cur.next 指向前驱节点 pre：cur.next = pre
# 然后将 pre 往后移一位也就是移到当前 cur 的位置：pre = cur
# 最后把 cur 也往后移一位也就是 temp 的位置：cur = temp
# 当 cur == Null，结束循环，返回 pre。


class Solution:
    def reverseList(self, head):
        pre = None
        cur = head

        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

















