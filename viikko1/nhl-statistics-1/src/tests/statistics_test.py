import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        # Kovakoodattu lista pelaajista
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_found_player(self):
        result = self.stats.search("Lemieux")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Lemieux")
        self.assertEqual(result.team, "PIT")

    def test_search_player_not_found(self):
        result = self.stats.search("Nonexistent Player")
        self.assertIsNone(result)

    def test_players_in_team(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)
        self.assertTrue(all(player.team == "EDM" for player in result))

    def test_top_by_points(self):
        result = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(str(result[0]), "Gretzky EDM 35 + 89 = 124")

    def test_top_by_goals(self):
        result = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(result[0]), "Lemieux PIT 45 + 54 = 99")

    def test_top_by_assists(self):
        result = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(result[0]), "Gretzky EDM 35 + 89 = 124")

if __name__ == '__main__':
    unittest.main()
