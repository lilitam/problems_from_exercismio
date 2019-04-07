from heapq import nlargest


class HighScores(object):
    def __init__(self, scores: object) -> object:
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return nlargest(3, self.scores)

    def report(self):
        latest_score = self.latest()
        best_score = self.personal_best()
        if latest_score == best_score:
            return "Your latest score was {}. That's your personal best!".format(latest_score)
        elif latest_score < best_score:
            return "Your latest score was {}. That's {} short of your personal best!".format(latest_score, best_score-latest_score)


