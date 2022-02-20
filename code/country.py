class Country():
    germany = "germany"
    portugal = "portugal"
    cannabis_addict_rate_m = 0
    cannabis_addict_rate_f = 0
    cocaine_addict_rate_m = 0
    cocaine_addict_rate_f = 0
    mdma_addict_rate_m = 0
    mdma_addict_rate_f = 0
    amphetamines_addict_rate_m = 0
    amphetamines_addict_rate_f = 0
    opioid_addict_rate_m = 0
    opioid_addict_rate_f = 0

    # 3 law-categories
    drug_acceptance = 0
    law_level = 1

    citizens = 1
    citizen_number_f = 1
    citizen_number_m = 1

    def __init__(self, country):
        if country == self.germany:
            # https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/liste-zensus-geschlecht-staatsangehoerigkeit.html
            self.citizen_number_f = 42109535
            self.citizen_number_m = 41011828
            self.citizens = 83121363

            self.law_level = 3

            # https://www.emcdda.europa.eu/system/files/publications/11334/germany-cdr-2019_0.pdf
            self.cannabis_addict_rate_m = 0.156
            self.cannabis_addict_rate_f = 0.11
            self.cocaine_addict_rate_m = 0.013
            self.cocaine_addict_rate_f = 0.011
            self.mdma_addict_rate_m = 0.013
            self.mdma_addict_rate_f = 0.013
            self.amphetamines_addict_rate_m = 0.019
            self.amphetamines_addict_rate_f = 0.019

            # https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
            self.opioids_addict_rate_m = 122968 / self.citizen_number_m
            self.opioids_addict_rate_f = 41826 / self.citizen_number_f
        if country == self.portugal:
            # https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&contecto=pi&indOcorrCod=0011166&selTab=tab0
            self.citizen_number_f = 5423632
            self.citizen_number_m = 4921170
            self.citizens = 10344802

            self.law_level = 1

            # https://www.emcdda.europa.eu/system/files/publications/11331/portugal-cdr-2019_0.pdf
            self.cannabis_addict_rate_m = 0.109
            self.cannabis_addict_rate_f = 0.05
            self.cocaine_addict_rate_m = 0.004
            self.cocaine_addict_rate_f = 0.003
            self.mdma_addict_rate_m = 0.004
            self.mdma_addict_rate_f = 0.001
            self.amphetamines_addict_rate_m = 0.0
            self.amphetamines_addict_rate_f = 0.0

            # only height risk number avaible, not devided by gender
            self.opioids_addict_rate_m = 33290 / self.citizens
            self.opioids_addict_rate_f = 33290 / self.citizens
        rate_sum = self.cannabis_addict_rate_m + self.cannabis_addict_rate_f + self.cocaine_addict_rate_m + self.cocaine_addict_rate_f + self.mdma_addict_rate_m + self.mdma_addict_rate_f + self.amphetamines_addict_rate_m + self.amphetamines_addict_rate_f + self.opioids_addict_rate_m + self.opioids_addict_rate_f
        self.drug_acceptance = (rate_sum / 10) / self.law_level

