import copy


class World:
    def __init__(self, pos: tuple, map: list):
        self.block_type = {
            "N": 0,
            "W": 1,
            "G": 2,
            "T": 3
        }

        self.actions = {
            "up": 0,
            "down": 1,
            "left": 2,
            "right": 3
        }
        self.map = map
        self.start_pos = pos
        self.agent_pos = copy.deepcopy(self.start_pos)

    def step(self, action):
        # 行動の実行
        # 報酬・ゴールの判定
        to_x, to_y = copy.deepcopy(self.agent_pos)
        # 移動可能かどうか確認
        if self._is_possible_action(to_x, to_y, action) == False:
            return self.agent_pos, -1, False

        if action == self.actions["up"]:
            to_y += -1
        elif action == self.actions["down"]:
            to_y += 1
        elif action == self.actions["left"]:
            to_x += -1
        elif action == self.actions["right"]:
            to_x += 1

        is_goal = self._is_end_episode(to_x, to_y)
        reward = self._compute_reward(to_x, to_y)
        self.agent_pos = to_x, to_y

        return self.agent_pos, reward, is_goal

    def _is_end_episode(self, x, y):
        # エピソードが終了か確認
        if self.map[y][x] == self.block_type["G"]:
            return True
        elif self.map[y][x] == self.block_type["T"]:
            return True
        else:
            return False

    def _is_wall(self, x, y):
        # 壁かどうか確認
        if self.map[y][x] == self.block_type["W"]:
            return True
        else:
            return False

    def _is_possible_action(self, x, y, action):
        # 実行可能かどうか
        to_x = x
        to_y = y

        if action == self.actions["up"]:
            to_y += -1
        elif action == self.actions["down"]:
            to_y += 1
        elif action == self.actions["left"]:
            to_x += -1
        elif action == self.actions["right"]:
            to_x += 1

        if len(self.map) <= to_y or 0 > to_y:
            return False
        elif len(self.map[0]) <= to_x or 0 > to_x:
            return False
        elif self._is_wall(to_x, to_y):
            return False

        return True

    def _compute_reward(self, x, y):
        if self.map[y][x] == self.block_type["N"]:
            return 0
        elif self.map[y][x] == self.block_type["G"]:
            return 100
        elif self.map[y][x] == self.block_type["T"]:
            return -100

    def reset(self):
        self.agent_pos = self.start_pos
        return self.start_pos
