nimet = {"Otto" : ["Otto", 7 , "Matikka"],
         "Elina" : ["Elina", 5,  "Historia"],
         "Jarmo" : ["Jarmo", 3 , "Musiikki"],
         "Siiri" : ["Siiri", 8 ,"Liikunta"]}

print(f"Siirin vuosiluokka on {nimet ['Siiri'][1]} Elinan lempiaine on {nimet ['Elina'][2]}")

nimet["Otto"][2] = "Käsityö"

nimet["Nooa"] = ["Nooa", 1, "Välitunti"]

del nimet["Jarmo"]

print(nimet)