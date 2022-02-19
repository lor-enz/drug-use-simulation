import unittest


class TestDrug(unittest.TestCase):

    def test_basics(self):
        import drug as d
        import settings as s
        for drug in s.set.drugs:
            print(f"""{drug.name} values:
                   Addict rate (male):   {drug.addict_rate_m}
                   Addict rate (female): {drug.addict_rate_f}
                   Dependence Potential: {drug.dependence_potential}
                   Mortality Rate: {round(drug.mortality_rate,8)}
                   Mortality Rate: {drug.mortality_rate}
                   """)

        # self.assertEqual(300, len(agents))

if __name__ == "__main__":
    unittest.main()
