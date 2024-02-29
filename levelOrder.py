class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

thirty_three = BinaryNode(33)
forty_one = BinaryNode(41)
seventy_two = BinaryNode(72)
twenty_one = BinaryNode(21)
thirty_eight = BinaryNode(38, thirty_three, forty_one)
sixty = BinaryNode(60, None, seventy_two)
twenty_seven = BinaryNode(27, twenty_one, thirty_eight)
fifty = BinaryNode(50, None, sixty)
forty_two = BinaryNode(40, twenty_seven, fifty)