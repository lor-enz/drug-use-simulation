import unittest


class TestCountry(unittest.TestCase):

    def test_basics(self):
        import country as cntry
        for c_dict in cntry.all_country_dicts:
            new_country = cntry.Country(c_dict)
            print(f"{new_country.name} initialized")


if __name__ == "__main__":
    unittest.main()
