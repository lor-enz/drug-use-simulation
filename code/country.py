class Country:

    def __init__(self, country_dict):
        self.name = country_dict['name']
        self.citizen_number_f = country_dict['citizen_number_f']
        self.citizen_number_m = country_dict['citizen_number_m']
        self.citizens = country_dict['citizens']

        self.law_level = country_dict['law_level']

        self.cannabis_addict_rate_m = country_dict['cannabis_addict_rate_m']
        self.cannabis_addict_rate_f = country_dict['cannabis_addict_rate_f']
        self.cocaine_addict_rate_m = country_dict['cocaine_addict_rate_m']
        self.cocaine_addict_rate_f = country_dict['cocaine_addict_rate_f']
        self.mdma_addict_rate_m = country_dict['mdma_addict_rate_m']
        self.mdma_addict_rate_f = country_dict['mdma_addict_rate_f']
        self.amphetamines_addict_rate_m = country_dict['amphetamines_addict_rate_m']
        self.amphetamines_addict_rate_f = country_dict['amphetamines_addict_rate_f']

        self.opioids_addict_rate_m = country_dict['opioids_addict_rate_m_dividend'] / self.citizen_number_m
        self.opioids_addict_rate_f = country_dict['opioids_addict_rate_f_dividend'] / self.citizen_number_f

        rate_sum = self.cannabis_addict_rate_m + self.cannabis_addict_rate_f + self.cocaine_addict_rate_m + self.cocaine_addict_rate_f + self.mdma_addict_rate_m + self.mdma_addict_rate_f + self.amphetamines_addict_rate_m + self.amphetamines_addict_rate_f + self.opioids_addict_rate_m + self.opioids_addict_rate_f
        self.drug_acceptance = (rate_sum / 10) / self.law_level


germany_dict = {
    "name": "Germany",
    "citizen_number_f": 42109535,
    "citizen_number_m": 41011828,
    "citizens": 83121363,
    "law_level": 3,

    # https://www.emcdda.europa.eu/system/files/publications/11334/germany-cdr-2019_0.pdf
    "cannabis_addict_rate_m": 0.156,
    "cannabis_addict_rate_f": 0.11,
    "cocaine_addict_rate_m": 0.013,
    "cocaine_addict_rate_f": 0.011,
    "mdma_addict_rate_m": 0.013,
    "mdma_addict_rate_f": 0.013,
    "amphetamines_addict_rate_m": 0.019,
    "amphetamines_addict_rate_f": 0.019,

    # https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
    "opioids_addict_rate_m_dividend": 122968,
    "opioids_addict_rate_f_dividend": 41826
}

portugal_dict = {
    "name": "Portugal",
    # https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&contecto=pi&indOcorrCod=0011166&selTab=tab0
    "citizen_number_f": 5423632,
    "citizen_number_m": 4921170,
    "citizens": 10344802,
    "law_level": 1,

    # https://www.emcdda.europa.eu/system/files/publications/11331/portugal-cdr-2019_0.pdf
    "cannabis_addict_rate_m": 0.109,
    "cannabis_addict_rate_f": 0.05,
    "cocaine_addict_rate_m": 0.004,
    "cocaine_addict_rate_f": 0.003,
    "mdma_addict_rate_m": 0.004,
    "mdma_addict_rate_f": 0.001,
    "amphetamines_addict_rate_m": 0.0,
    "amphetamines_addict_rate_f": 0.0,

    # only high risk number available, not divided by gender
    "opioids_addict_rate_m_dividend": 33290,
    "opioids_addict_rate_f_dividend": 33290
}

italy_dict = {
    "name": "Italy",

    "citizen_number_f": 30393478,
    "citizen_number_m": 28864088,
    "citizens": 59257566,
    "law_level": 1,

    # https://www.emcdda.europa.eu/system/files/publications/11329/italy-cdr-2019_0.pdf
    "cannabis_addict_rate_m": 0.242,
    "cannabis_addict_rate_f": 0.175,
    "cocaine_addict_rate_m": 0.018,
    "cocaine_addict_rate_f": 0.017,
    "mdma_addict_rate_m": 0.01,
    "mdma_addict_rate_f": 0.006,
    "amphetamines_addict_rate_m": 0.004,
    "amphetamines_addict_rate_f": 0.002,

    #
    "opioids_addict_rate_m_dividend": 235000,
    "opioids_addict_rate_f_dividend": 235000
}

netherlands_dict = {
    "name": "Netherland",

    "citizen_number_f": 8788879,
    "citizen_number_m": 8686536,
    "citizens": 17475415,
    "law_level": 3,

    # https://www.emcdda.europa.eu/system/files/publications/11347/netherlands-cdr-2019.pdf
    "cannabis_addict_rate_m": 0.223,
    "cannabis_addict_rate_f": 0.126,
    "cocaine_addict_rate_m": 0.058,
    "cocaine_addict_rate_f": 0.031,
    "mdma_addict_rate_m": 0.083,
    "mdma_addict_rate_f": 0.06,
    "amphetamines_addict_rate_m": 0.049,
    "amphetamines_addict_rate_f": 0.028,

    # only high risk number available, not divided by gender
    "opioids_addict_rate_m_dividend": 7000,
    "opioids_addict_rate_f_dividend": 7000
}

czech_dict = {
    "name": "Czech",

    "citizen_number_f": 5455655,
    "citizen_number_m": 5259961,
    "citizens": 10715617,
    "law_level": 1,

    # https://www.emcdda.europa.eu/system/files/publications/4511/TD0416912ENN.pdf
    "cannabis_addict_rate_m": 0.256,
    "cannabis_addict_rate_f": 0.117,
    "cocaine_addict_rate_m": 0.0,
    "cocaine_addict_rate_f": 0.006,
    "mdma_addict_rate_m": 0.044,
    "mdma_addict_rate_f": 0.026,
    "amphetamines_addict_rate_m": 0.019,
    "amphetamines_addict_rate_f": 0.025,

    # only high risk number available, not divided by gender
    "opioids_addict_rate_m_dividend": 6350,
    "opioids_addict_rate_f_dividend": 6350
}

all_country_dicts = [portugal_dict, italy_dict,germany_dict,netherlands_dict,czech_dict]

germany = Country(germany_dict)
germany.law_level = 1
portugal = Country(portugal_dict)
italy = Country(italy_dict)
