class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = [-1] * 1000001
        min_consec_cards = float('inf')
        for i in range(len(cards)):
            if last_index[cards[i]] != -1:
                min_consec_cards = min(min_consec_cards, i - last_index[cards[i]] + 1)
            last_index[cards[i]] = i
        
        if min_consec_cards != float('inf'):
            return min_consec_cards
        else:
            return -1