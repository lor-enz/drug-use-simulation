
class Drug:
    def __init__(self, name, addictiveness, availability):
        self.name = name
        self.addictiveness = addictiveness
        self.availability = availability


# Numbers not based on anything, completely made up.
weed_example = Drug('cocaine', 0.2, 0.6)
cocaine_example = Drug('cocaine', 0.6, 0.3)
heroin_example = Drug('cocaine', 0.8, 0.2)
