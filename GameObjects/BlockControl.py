from GameObjects.Block import Block


class BlocksControl:
    def __init__(self, blocks_num, mapW, mapH, path):
        self.blocks_num = blocks_num
        self.blocks = []
        self.mapH = mapH
        self.mapW = mapW

        self.create_blocks(path)

    def create_blocks(self, path):
        for i in range(self.blocks_num):
            new_block = Block(self.mapW, self.mapH, path)
            self.blocks.append(new_block)
