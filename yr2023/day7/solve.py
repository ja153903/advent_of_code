from collections import Counter
from typing import NamedTuple

from utils.base_solution import BaseSolution

CARD_ORDER = "23456789TJQKA"
CARD_ORDER_PT2 = "J23456789TQKA"


class Hand(NamedTuple):
    hand: str
    bid: int

    def typeof(self) -> int:
        counter = Counter(self.hand)
        most_common = counter.most_common()

        most_common_count = most_common[0][1]

        match most_common_count:
            case 5:
                return 7
            case 4:
                return 6
            case 3:
                # check if we can form a full house
                second_most_common_count = most_common[1][1]
                if second_most_common_count == 2:
                    return 5

                return 4
            case 2:
                second_most_common_count = most_common[1][1]
                if second_most_common_count == 2:
                    return 3

                return 2
            case _:
                return 1

    def hand_to_card_order(self):
        return [CARD_ORDER.index(card) for card in self.hand]


class AugHand(Hand):
    def typeof(self) -> int:
        counter = Counter(self.hand)

        joker_count = counter["J"]
        if joker_count == 4 or joker_count == 5:
            return 7

        del counter["J"]

        most_common = counter.most_common()

        most_common_card = most_common[0][0]
        most_common_count = most_common[0][1]

        counter[most_common_card] += joker_count

        most_common = counter.most_common()
        most_common_count = most_common[0][1]

        match most_common_count:
            case 5:
                return 7
            case 4:
                return 6
            case 3:
                # check if we can form a full house
                second_most_common_count = most_common[1][1]
                if second_most_common_count == 2:
                    return 5

                return 4
            case 2:
                second_most_common_count = most_common[1][1]
                if second_most_common_count == 2:
                    return 3

                return 2
            case _:
                return 1

    def hand_to_card_order(self):
        return [CARD_ORDER_PT2.index(card) for card in self.hand]


def hand_cmp(hand: Hand | AugHand):
    return (hand.typeof(), *hand.hand_to_card_order())


class Solution(BaseSolution):
    def part1(self):
        hands = self.get_hands()
        return sum(hand.bid * rank for rank, hand in enumerate(hands, start=1))

    def part2(self):
        hands = self.get_hands_pt2()
        return sum(hand.bid * rank for rank, hand in enumerate(hands, start=1))

    def get_hands(self) -> list[Hand]:
        result = []
        for line in self.data:
            hand, bid = line.split()
            result.append(Hand(hand, int(bid)))

        result.sort(key=hand_cmp)

        return result

    def get_hands_pt2(self) -> list[AugHand]:
        result = []
        for line in self.data:
            hand, bid = line.split()
            result.append(AugHand(hand, int(bid)))

        result.sort(key=hand_cmp)

        return result
