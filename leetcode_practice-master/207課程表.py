class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return True

        # 步骤1：统计每个顶点的入度
        # 入度数组，记录了指向它的结点的个数，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        print('in_degrees', in_degrees)
        # 邻接表，使用散列表是为了去重
        adj = [set() for _ in range(numCourses)]
        print('adj',adj)

        # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
        # [0, 1] 表示 1 在先，0 在后
        # 注意：邻接表存放的是后继 successor 结点的集合
        print('prerequisites',prerequisites)
        for second, first in prerequisites:
            in_degrees[second] += 1
            print(in_degrees)
            adj[first].add(second)
            print('adj',adj)

        # 步骤2：拓扑排序开始之前，先把所有入度为 0 的结点加入到一个队列中
        # 首先遍历一遍，把所有入度为 0 的结点都加入队列
        print('in_degrees',in_degrees)
        queue = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
            print('1 queue',queue)

        counter = 0
        while queue:
            top = queue.pop(0)
            counter += 1
            print('counter',counter)
            # 步骤3：把这个结点的所有后继结点的入度减去 1，如果发现入度为 0 ，就马上添加到队列中
            print('adj[{}]'.format(top),adj[top])
            for successor in adj[top]:
                in_degrees[successor] -= 1
                print('in_degrees[{}] -= 1'.format(successor),in_degrees)
                if in_degrees[successor] == 0:
                    queue.append(successor)
            print('queue',queue)
        return counter == numCourses
print(Solution().canFinish(3,[[1,0],[1,2]]))
print(Solution().canFinish(2,[[1,0],[0,1]]))