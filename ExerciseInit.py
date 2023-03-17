class inventory:
    def __init__(self):
        self.stones = []
        self.max = 5
    def getStone(self,stone):
        if len(self.stones) >= 5:
            self.stones.pop(0)
        self.stones.append(stone)
    def checkStones(self):
        for stone in self.stones:
            print(stone)

pocket = inventory()
pocket.getStone("amethyst")
pocket.getStone("quartz")
pocket.getStone("iron")
pocket.getStone("copper")
pocket.getStone("obsidian")
pocket.checkStones()
pocket.getStone("silver")
pocket.checkStones()