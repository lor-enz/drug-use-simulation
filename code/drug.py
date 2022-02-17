# https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(07)60464-4/fulltext
heroin_dependence_potential = 3
cocaine_dependence_potential = 2.39
amphetamine_dependence_potential = 1.67
cannabis_dependence_potential = 1.51
# mdma_dependence_potential = 1.13
# barbiturates_dependence_potential = 2.01

# https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/liste-zensus-geschlecht-staatsangehoerigkeit.html
citizen_number_f = 42109535
citizen_number_m = 41011828
germany_citizens = citizen_number_f + citizen_number_m  # 83121363
# mortality rates in Germany taken for all simulations

cannabis_addict_rate_m = 0.156
cannabis_addict_rate_f = 0.11

cocaine_addict_rate_m = 0.013
cocaine_addict_rate_f = 0.011

amphetamines_addict_rate_m = 0.019
amphetamines_addict_rate_f = 0.019

# mdma_addict_rate_m = 0.013
# mdma_addict_rate_f = 0.013

# https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
opiod_addict_rate_m = 122968 / citizen_number_m
opiod_addict_rate_f = 41826 / citizen_number_f

# https://www.bundesdrogenbeauftragter.de/assets/Presse/2021/CDR_2020_Bula_Rauschgifttote_nach_Todesursachen_-_Ver%C3%A4nderung_2019-2020.pdf
opiod_mortality_rate = 572 / ((opiod_addict_rate_m + opiod_addict_rate_f) / 2 * germany_citizens)
cocaine_mortality_rate = 107 / ((cocaine_addict_rate_m + cocaine_addict_rate_f) / 2 * germany_citizens)
amphetamine_mortality_rate = 129 / (amphetamines_addict_rate_m * germany_citizens)
cannabis_mortality_rate = 0  # ?


class Drug:
    def __init__(self, name, addict_rate_f, addict_rate_m, dependence_potential, mortality_rate):
        self.name = name
        self.dependence_potential = dependence_potential
        self.addict_rate_m = addict_rate_m
        self.addict_rate_f = addict_rate_f
        self.mortality_rate = mortality_rate

    def __str__(self):
        return f"""{self.name} values:
                   Addict rate (male):   {self.addict_rate_m}
                   Addict rate (female): {self.addict_rate_f}
                   Dependence Potential: {self.dependence_potential}
                   Mortality Rate: {self.mortality_rate}
                   """

cannabis = Drug("cannabis", cannabis_addict_rate_f, cannabis_addict_rate_m, cannabis_dependence_potential, cannabis_mortality_rate)
cocaine = Drug("cocaine", cocaine_addict_rate_f, cocaine_addict_rate_m, cocaine_dependence_potential, cocaine_mortality_rate)
amphetamines = Drug("amphetamines", amphetamines_addict_rate_f, amphetamines_addict_rate_m, amphetamine_dependence_potential,
                    amphetamine_mortality_rate)

drugs = [cannabis, cocaine, amphetamines]


def missing_data(dont_run_this):
    heroin = Drug("heroin", heroin_addict_rate_f, heroin_addict_rate_m, heroin_dependence_potential, heroin_mortality_rate)
    opiod = Drug("opiod", opiod_addict_rate_f, opiod_addict_rate_m, opiod_dependence_potential, opiod_mortality_rate)
