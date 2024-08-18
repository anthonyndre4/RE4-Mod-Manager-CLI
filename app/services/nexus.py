from app.services.auth import BaseNexusClient
from app.models.nexus import Game, LatestMods


class NexusClient(BaseNexusClient):

    def get_nexus_game(self, game_name: str) -> Game:
        return self.get(f"/v1/games/{game_name}.json", Game)

    def get_nexus_game_latest_added_mods(self, game_name: str) -> LatestMods:
        return self.list(f"/v1/games/{game_name}/mods/latest_updated.json", LatestMods)
