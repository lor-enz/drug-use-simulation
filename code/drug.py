class Drug():
    def __init__(self, name, addictiveness):
        self.name = name
        self.addictiveness = addictiveness

    # https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(07)60464-4/fulltext
    heroin_dependence_potential = 3
    cocaine_dependence_potential = 2.39
    amphetamine_dependence_potential = 1.67
    cannabis_dependence_potential = 1.51
    #mdma_dependence_potential = 1.13
    #barbiturates_dependence_potential = 2.01

    # https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsstand/Tabellen/liste-zensus-geschlecht-staatsangehoerigkeit.html
    germany_citizens = 83121363
    citizen_number_f = 42109535
    citizen_number_m = 41011828

    #mortality rates in Germany taken for all simulations

    cannabis_addict_rate_m = 0.156
    cannabis_addict_rate_f = 0.11

    cocaine_addict_rate_m = 0.013
    cocaine_addict_rate_f = 0.011

    amphetamines_addict_rate_m = 0.019
    amphetamines_addict_rate_f = 0.019

    #mdma_addict_rate_m = 0.013
    #mdma_addict_rate_f = 0.013



    #https://www.bundesgesundheitsministerium.de/fileadmin/Dateien/5_Publikationen/Drogen_und_Sucht/Berichte/AbschlussberichtOpiS-Bericht_150518.pdf
    opiod_addict_rate_m = 122968/citizen_number_m
    opiod_addict_rate_f = 41826/citizen_number_f

    #https://www.bundesdrogenbeauftragter.de/assets/Presse/2021/CDR_2020_Bula_Rauschgifttote_nach_Todesursachen_-_Ver%C3%A4nderung_2019-2020.pdf
    opiod_mortality_rate = 572/((opiod_addict_rate_m+opiod_addict_rate_f)/2*germany_citizens)
    cocaine_mortality_rate = 107/((cocaine_addict_rate_m+cocaine_addict_rate_f)/2*germany_citizens)
    amphetamine_mortality_rate = 129/(amphetamines_addict_rate_m*germany_citizens)
    cannabis_mortality_rate = 0 #?

    # Numbers not based on anything, completely made up.
weed_example = Drug('cocaine', 0.2)
cocaine_example = Drug('cocaine', 0.6)
heroin_example = Drug('cocaine', 0.8)
