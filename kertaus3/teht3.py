kirjasto = {"Harry Potter" : ["JK Rowling" ,  1997 , "fantasia"],
            "Ajasta ikuisuuteen" : ["Camilla Grebe", 2025, "jännitys"],
            "Hildur" : ["Satu Rämö", 2022, "jännitys"]}



print(f"Harry Potterin kirjoittaja on {kirjasto['Harry Potter'][0]}, Ajasta ikuisuuteen genre on {kirjasto['Ajasta ikuisuuteen'][2]}")

kirjasto["Hildur"][2] = "kauhu"

kirjasto["Houkutus"] = ["Stephenie Meyer", 2008, "fantasia"]

del kirjasto["Hildur"]

print(kirjasto)