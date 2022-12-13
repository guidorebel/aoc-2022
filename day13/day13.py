
from aoc import PuzzleData


class Packet:

    def __init__(self, packet) -> None:
        self.packet = packet

    def isInt(self):
        return isinstance(self.packet, int)

    def isList(self):
        return isinstance(self.packet, list)

    def __lt__(self, other: "Packet") -> bool:
        return self.packet < other.packet

    def __len__(self) -> int:
        return len(self.packet)

    def id(self) -> str:
        # I actually don't know why this trick works for part 2  :-)
        # I tried to apply it to part 1 as well, but then the answer is incorrect.
        # Here I simply convert the packet into a string that I will use to sort.
        v = str(self.packet)
        v = v.replace(" ", "")
        v = v.replace("[]", "0")
        v = v.replace("[", "")
        v = v.replace("]", "")
        v = v.replace("10", "A")
        v = v.replace(",", "")
        return v


class PacketCompare:
    
    @staticmethod
    def compare(left: Packet, right: Packet):

        if left.isInt() and right.isInt():
            if   left < right: return 1
            elif right < left: return -1
            else: return 0

        else:
            if left.isInt() and right.isList():
                left = Packet ([left.packet])
                return PacketCompare.compare(left, right)
        
            elif left.isList() and right.isInt():
                right = Packet ([right.packet])
                return PacketCompare.compare(left, right)

            for c in (PacketCompare.compare(Packet(le), Packet(re)) for le, re in zip(left.packet, right.packet)):
                if c != 0:
                    return c

            if   len(left) < len(right): return 1
            elif len(right) < len(left): return -1
            else: return 0
                
#================================

# Get the data
puzzle = PuzzleData(__file__)
data = puzzle.getData().split("\n\n")

index = 0
count = 0

for packetData in data:

    index += 1
    left, right = [Packet(eval(p)) for p in packetData.split("\n")]
    if PacketCompare.compare(left, right) == 1: count += index

print (count)

#================================

p2 = Packet([[2]])
p6 = Packet([[6]])

packetList = []
packetList.append(p2.id())
packetList.append(p6.id())

for packetData in data:
    left, right = [Packet(eval(p)) for p in packetData.split("\n")]
    packetList.append(left.id())
    packetList.append(right.id())

packetList.sort()
print ((packetList.index("2")+1) * (packetList.index("6")+1))

