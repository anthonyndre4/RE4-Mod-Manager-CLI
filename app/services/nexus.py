from app.services.auth import BaseNexusClient
from app.models.nexus import Game


class NexusClient(BaseNexusClient):

    def get_nexus_game(self, game_name: str) -> Game:
        return self.get(f"/v1/games/{game_name}.json", Game)
