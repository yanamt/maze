import numpy as np
import copy


class generator:
    def __init__(self, size) -> None:
        self.size = size
        self.start_pos = 1, size
        self.goal_pos = None
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
        self.ini_maze = copy.deepcopy(maze)
        # ゴール地点の決定
        flag = True
        while(flag):
            num = np.random.randint(0, self.size**2)
            pos_x, pos_y = num % self.size, num//self.size
            if maze[pos_y+1][pos_x+1] == 1:
                maze[pos_y+1][pos_x+1] = 3
                flag = False
        # トラップ地点の決定
        flag = True
        while(flag):
            num = np.random.randint(0, self.size**2)
            pos_x, pos_y = num % self.size, num//self.size
            if maze[pos_y+1][pos_x+1] == 0 and num != self.size*(self.size-1)+1:
                maze[pos_y+1][pos_x+1] = 2
                flag = False
        # クリア可能か判定し，クリア可能な迷路ができるまで生成を繰り返す
        if self._is_possible():
            self.maze = maze
            return self.ini_maze, self.maze
        else:
            self.generate()

    def _is_possible(self):
        possible = True
        return possible


if __name__ == "__main__":
    x = generator(5)
    before, after = x.generate()
    for line in before:
        print(line)
    print("=====================")
    for line in after:
        print(line)
