from app.modules.game.init_players_strategy import InitPlayerStrategyABC
from app.modules.game import GameABC


class OppositeSidesInitPlayerStrategy(InitPlayerStrategyABC):
    def init_players(self, game: GameABC) -> None:
        step = game.width // len(game.players)
        x = step // 2
        for n, p in enumerate(game.players, start=1):
            if n % 2 == 0:
                y = 90
                reversed_body = True
            else:
                y = game.height - 90
                reversed_body = False

            p.create_start_body(x=x, y=y, reversed_body=reversed_body)
            x += step
