import numpy as np
import copy
from typing import Tuple
from collections import deque


class Generator:
    def __init__(self, size: int) -> None:
        self.size = size
        self.start_pos = 1, size
        self.ini_maze = None
        self.maze = None

    def generate(self):
        # 迷路のランダム生成
        maze = [[1 for _ in range(self.size+2)]]
        for _ in range(self.size):
            maze.append([1]+[np.random.randint(0, 2)
                        for _ in range(self.size)]+[1])
        maze.append([1 for _ in range(self.size+2)])
        # スタート地点を0にする
        maze[self.start_pos[1]][self.start_pos[0]] = 0
        # ゴール地点の決定
        flag = True
        while(flag):
            num = np.random.randint(0, self.size**2)
            pos_x, pos_y = num % self.size, num//self.size
            if maze[pos_y+1][pos_x+1] == 0 and num != self.size*(self.size-1)+1:
                maze[pos_y+1][pos_x+1] = 2
                flag = False
                #self.goal_pos = pos_x+1, pos_y+1
        self.ini_maze = copy.deepcopy(maze)
        # トラップ地点の決定
        flag = True
        while(flag):
            num = np.random.randint(0, self.size**2)
            pos_x, pos_y = num % self.size, num//self.size
            if maze[pos_y+1][pos_x+1] == 1:
                maze[pos_y+1][pos_x+1] = 3
                flag = False
        possible, num_step = self._is_possible()
        # クリア可能か判定し，クリア可能な迷路ができるまで生成を繰り返す
        if possible and num_step > 10:
            self.maze = [maze[i][1:-1] for i in range(1, self.size+1)]
            return self.ini_maze, self.maze, num_step
        else:
            return self.generate()

    def _is_possible(self):
        # 幅優先探索
        # スタート地点をキューにセット
        pos = deque([[self.start_pos[1], self.start_pos[0], 0]])
        while(len(pos) > 0):
            x, y, depth = pos.popleft()
            # ゴールについた時点で終了
            if self.ini_maze[x][y] == 2:
                return True, depth
            # 探索済みとしてブロックの値を9に変更
            self.ini_maze[x][y] = 9

            # 上下左右を探索
            if self.ini_maze[x-1][y] in [0, 2]:
                pos.append([x-1, y, depth + 1])
            if self.ini_maze[x+1][y] in [0, 2]:
                pos.append([x+1, y, depth + 1])
            if self.ini_maze[x][y-1] in [0, 2]:
                pos.append([x, y-1, depth + 1])
            if self.ini_maze[x][y+1] in [0, 2]:
                pos.append([x, y+1, depth + 1])
        return False, -1


if __name__ == "__main__":
    a = Generator(10)
    before, after, step = a.generate()
    for line in before:
        print(line)
    print("=================================")
    for line in after:
        print(line)
    print(step)
