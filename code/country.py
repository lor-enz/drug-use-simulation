germany = {
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

portugal = {
    "citizen_number_f": 5423632,
    "citizen_number_m": 4921170,
    "citizens": 10344802,
    "law_level": 1,

    # https://www.emcdda.europa.eu/system/files/publications/11334/germany-cdr-2019_0.pdf
    "cannabis_addict_rate_m": 0.109,
    "cannabis_addict_rate_f": 0.05,
    "cocaine_addict_rate_m": 0.004,
    "cocaine_addict_rate_f": 0.003,
    "mdma_addict_rate_m": 0.004,
    "mdma_addict_rate_f": 0.001,
    "amphetamines_addict_rate_m": 0.0,
    "amphetamines_addict_rate_f": 0.0,

    # https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
    "opioids_addict_rate_m_dividend": 33290,
    "opioids_addict_rate_f_dividend": 33290
}


class Country:

    def __init__(self, countr_dict):
        self.citizen_number_f = countr_dict['citizen_number_f']
        self.citizen_number_m = countr_dict['citizen_number_m']
        self.citizens = countr_dict['citizens']

        self.law_level = countr_dict['law_level']

        self.cannabis_addict_rate_m = countr_dict['cannabis_addict_rate_m']
        self.cannabis_addict_rate_f = countr_dict['cannabis_addict_rate_f']
        self.cocaine_addict_rate_m = countr_dict['cocaine_addict_rate_m']
        self.cocaine_addict_rate_f = countr_dict['cocaine_addict_rate_f']
        self.mdma_addict_rate_m = countr_dict['mdma_addict_rate_m']
        self.mdma_addict_rate_f = countr_dict['mdma_addict_rate_f']
        self.amphetamines_addict_rate_m = countr_dict['amphetamines_addict_rate_m']
        self.amphetamines_addict_rate_f = countr_dict['amphetamines_addict_rate_f']

        self.opioids_addict_rate_m = countr_dict['opioids_addict_rate_m_dividend'] / self.citizen_number_m
        self.opioids_addict_rate_f = countr_dict['opioids_addict_rate_f_dividend'] / self.citizen_number_f

        rate_sum = self.cannabis_addict_rate_m + self.cannabis_addict_rate_f + self.cocaine_addict_rate_m + self.cocaine_addict_rate_f + self.mdma_addict_rate_m + self.mdma_addict_rate_f + self.amphetamines_addict_rate_m + self.amphetamines_addict_rate_f + self.opioids_addict_rate_m + self.opioids_addict_rate_f
        self.drug_acceptance = (rate_sum / 10) / self.law_level
