class Country():
    germany = "germany"
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

    #3 law-categories
    drug_acceptance=1

    citizen_number_f=1
    citizen_number_m=1
    addicts_number=0

    def __init__(self, country):
        if country == self.germany:
            #https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/liste-zensus-geschlecht-staatsangehoerigkeit.html
            citizen_number_f=42109535
            citizen_number_m=41011828

            drug_acceptance = 3

            # https://www.emcdda.europa.eu/system/files/publications/4528/TD0416906ENN.pdf
            cannabis_addict_rate_m = 0.156
            cannabis_addict_rate_f = 0.11
            cocaine_addict_rate_m = 0.013
            cocaine_addict_rate_f = 0.011
            mdma_addict_rate_m = 0.013
            mdma_addict_rate_f = 0.013
            amphetamines_addict_rate_m = 0.019
            amphetamines_addict_rate_f = 0.019

            #https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
            opioid_addict_rate_m = 122968/citizen_number_m
            opioid_addict_rate_f = 41826/citizen_number_f

