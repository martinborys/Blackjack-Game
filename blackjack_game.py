from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer = Dealer()
        self.player_list = []
        for i in player_names:
            self.player_list.append(Player(i, self.dealer))
        self.results = []

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """

        for i in range(num_rounds):
            self.dealer.shuffle_deck()
#Deal initial cards
            for b in range(2):
                for e in self.player_list:
                    self.dealer.signal_hit(e)
                self.dealer.signal_hit(self.dealer)
#Natural Blackjack Case
            if self.dealer.card_sum == 21:
                for q in self.player_list:
                    if q.card_sum() == 21:
                        q.record_tie()
                    else:
                        q.record_loss()
                self.results.append("Round {}".format(i + 1))
                self.results.append(str(self.dealer))
                for k in self.player_list:
                    self.results.append(str(k))
                self.dealer.hand = []
                for y in self.player_list:
                    y.hand = []
                continue

#Play each round and calculate winners
            self.dealer.play_round()
            dscore = self.dealer.card_sum
            for j in self.player_list:
                j.play_round()
                if j.card_sum > 21 or j.card_sum < dscore:
                    j.record_loss()
                elif j.card_sum > dscore:
                    j.record_win()
                elif j.card_sum == dscore:
                    j.record_tie()
#Fill list to print results
            self.results.append("Round {}".format(i+1))
            self.results.append(str(self.dealer))
            for k in self.player_list:
                self.results.append(str(k))
#Reset Hands
            self.dealer.hand = []
            for y in self.player_list:
                y.hand = []


        fresults = ''
        for h in self.results:
            fresults += h+"\n"
        return fresults[:-1]

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """

        for t in self.player_list:
            t.reset_stats()
            t.hand = []
        self.dealer.hand = []
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
