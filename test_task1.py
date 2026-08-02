import unittest

from Task1 import search_mashinalar, search_model_info


class SearchMashinaTests(unittest.TestCase):
    def test_search_returns_matching_models(self):
        results = search_mashinalar("camry")
        self.assertTrue(results)
        self.assertIn("Toyota Camry", [item["model"] for item in results])

    def test_search_is_case_insensitive(self):
        results = search_mashinalar("CIVIC")
        self.assertTrue(results)
        self.assertIn("Honda Civic", [item["model"] for item in results])

    def test_model_lookup_returns_damas_info(self):
        result = search_model_info("Damas")
        self.assertTrue(result["model"].lower().startswith("daewoo") or "damas" in result["model"].lower())
        self.assertIn("narx", result)
        self.assertIn("tavsif", result)

    def test_search_finds_broader_model_queries(self):
        results = search_mashinalar("audi a4")
        self.assertTrue(results)
        self.assertIn("Audi A4", [item["model"] for item in results])


if __name__ == "__main__":
    unittest.main()
