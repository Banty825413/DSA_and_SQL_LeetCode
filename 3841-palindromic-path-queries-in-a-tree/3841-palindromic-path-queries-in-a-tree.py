class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        # Iterative DFS: Euler Tour and parent/depth information
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1
                order.append(u)

                stack.append((u, p, 1))

                for v in graph[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        # Binary lifting table for LCA
        up = [parent[:]]

        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # A character is represented by one bit
        def char_mask(c):
            return 1 << (ord(c) - ord('a'))

        chars = list(s)
        masks = [char_mask(c) for c in chars]

        # Fenwick Tree for range XOR updates and point queries
        bit = [0] * (n + 1)

        def add(i, value):
            i += 1
            while i <= n:
                bit[i] ^= value
                i += i & -i

        def prefix_xor(i):
            i += 1
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        # XOR value over Euler interval [l, r)
        def range_xor(l, r, value):
            add(l, value)
            if r < n:
                add(r, value)

        # Each node's character affects its entire subtree's
        # root-to-node XOR masks.
        for u in range(n):
            range_xor(tin[u], tout[u], masks[u])

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                new_mask = char_mask(new_char)
                delta = masks[u] ^ new_mask

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    masks[u] = new_mask
                    chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                # XOR of characters on the path u -> v
                path_mask = (
                    prefix_xor(tin[u])
                    ^ prefix_xor(tin[v])
                    ^ masks[ancestor]
                )

                # At most one character may have odd frequency
                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer
