# TODO implement high scores management (load, save, update)
class HighScores:

    def __init__(self) -> None:
        self.scores: dict[str, int] = {}

    def _valid_score(self, score: int) -> bool:
        # TODO implement score validation logic
        return False

    def _valid_player(self, player: str) -> bool:
        # TODO implement player validation logic
        return False

    def load(self, filepath: str) -> None:
        # TODO implement loading high scores from a file
        pass

    def save(self, filepath: str) -> None:
        # TODO implement saving high scores to a file
        pass

    def insert(self, player: str, score: int) -> None:
        # TODO implement updating high scores with a new score
        pass
