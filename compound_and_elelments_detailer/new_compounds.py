from elements import element_list  # Ensure you import the correct dictionary

compounds = {
    "water": [element_list["hydrogen"], element_list["hydrogen"], element_list["oxygen"]],  # H2O
    "trifluoride": [element_list["fluorine"]] * 3,  # F3
    "ammonia": [element_list["nitrogen"], element_list["hydrogen"], element_list["hydrogen"]],  # NH3
    "carbon dioxide": [element_list["carbon"], element_list["oxygen"]] * 2,  # CO2
    "methane": [element_list["carbon"]] + [element_list["hydrogen"]] * 4,  # CH4
    "sodium chloride": [element_list["sodium"], element_list["chlorine"]],  # NaCl
    "sulfuric acid": [element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # H2SO4
    "acetic acid": [element_list["carbon"]] * 2 + [element_list["hydrogen"]] * 4 + [element_list["oxygen"]],  # C2H4O2
    "sodium phosphate": [element_list["sodium"]] * 3 + [element_list["phosphorus"]],  # Na3PO4
    "potassium chloride": [element_list["potassium"], element_list["chlorine"]],  # KCl
    "magnesium sulfate": [element_list["magnesium"], element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # MgSO4
    "barium sulfate": [element_list["barium"], element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # BaSO4
    "calcium hydroxide": [element_list["calcium"]] + [element_list["oxygen"]] * 2,  # Ca(OH)2
    "sodium thiosulfate": [element_list["sodium"]] * 2 + [element_list["sulfur"]] * 2 + [element_list["oxygen"]] * 3,  # Na2S2O3
    "ammonium nitrate": [element_list["nitrogen"], element_list["hydrogen"]] * 4 + [element_list["oxygen"]],  # NH4NO3
    "titanium dioxide": [element_list["titanium"]] + [element_list["oxygen"]] * 2,  # TiO2
    "silicon dioxide": [element_list["silicon"]] + [element_list["oxygen"]] * 2,  # SiO2
    "caffeine": [element_list["carbon"]] * 8 + [element_list["hydrogen"]] * 10 + [element_list["nitrogen"]] * 4 + [element_list["oxygen"]] * 2,  # C8H10N4O2
    "hydrochloric acid": [element_list["hydrogen"], element_list["chlorine"]],  # HCl
    "calcium carbonate": [element_list["calcium"], element_list["carbon"], element_list["oxygen"]],  # CaCO3
    "sodium bicarbonate": [element_list["sodium"], element_list["hydrogen"], element_list["carbon"], element_list["oxygen"]],  # NaHCO3
    "potassium nitrate": [element_list["potassium"], element_list["nitrogen"], element_list["oxygen"]],  # KNO3
    "calcium sulfate": [element_list["calcium"], element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # CaSO4
    "glucose": [element_list["carbon"]] * 6 + [element_list["hydrogen"]] * 12 + [element_list["oxygen"]] * 6,  # C6H12O6
    "lactic acid": [element_list["carbon"]] * 3 + [element_list["hydrogen"]] * 6 + [element_list["oxygen"]] * 3,  # C3H6O3
    "sodium sulfate": [element_list["sodium"]] * 2 + [element_list["sulfur"], element_list["oxygen"]] * 4,  # Na2SO4
    "ammonium sulfate": [element_list["nitrogen"], element_list["sulfur"], element_list["oxygen"]] * 4,  # (NH4)2SO4
    "copper sulfate": [element_list["copper"], element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # CuSO4
    "iron(III) oxide": [element_list["iron"]] * 2 + [element_list["oxygen"]] * 3,  # Fe2O3
    "zinc oxide": [element_list["zinc"], element_list["oxygen"]],  # ZnO
    "sodium acetate": [element_list["sodium"], element_list["carbon"]] * 2 + [element_list["oxygen"]] * 2,  # C2H3NaO2
    "fructose": [element_list["carbon"]] * 6 + [element_list["hydrogen"]] * 12 + [element_list["oxygen"]] * 6,  # C6H12O6
    "sucrose": [element_list["carbon"]] * 12 + [element_list["hydrogen"]] * 22 + [element_list["oxygen"]] * 11,  # C12H22O11
    "citric acid": [element_list["carbon"]] * 6 + [element_list["oxygen"]] * 7,  # C6H8O7
    "sodium nitrite": [element_list["sodium"], element_list["nitrogen"], element_list["oxygen"]],  # NaNO2
    "potassium permanganate": [element_list["potassium"], element_list["manganese"]] + [element_list["oxygen"]] * 4,  # KMnO4
    "sodium sulfite": [element_list["sodium"]] * 2 + [element_list["sulfur"]] + [element_list["oxygen"]] * 3,  # Na2SO3
    "sodium fluoride": [element_list["sodium"], element_list["fluorine"]],  # NaF
    "sodium iodide": [element_list["sodium"], element_list["iodine"]],  # NaI
    "sodium carbonate": [element_list["sodium"]] * 2 + [element_list["oxygen"]] * 3,  # Na2CO3
    "calcium nitrate": [element_list["calcium"]] + [element_list["nitrogen"]] * 2,  # Ca(NO3)2
    "potassium carbonate": [element_list["potassium"]] * 2 + [element_list["oxygen"]] * 3,  # K2CO3
    "ammonium phosphate": [element_list["nitrogen"]] * 3 + [element_list["phosphorus"]],  # (NH4)3PO4
    "sodium hypochlorite": [element_list["sodium"], element_list["chlorine"], element_list["oxygen"]],  # NaClO
    "sodium chlorate": [element_list["sodium"], element_list["chlorine"], element_list["oxygen"]] * 3,  # NaClO3
    "sodium perchlorate": [element_list["sodium"], element_list["chlorine"], element_list["oxygen"]] * 4,  # NaClO4
    "barium hydroxide": [element_list["barium"]] + [element_list["oxygen"]] * 2,  # Ba(OH)2
    "calcium sulfide": [element_list["calcium"], element_list["sulfur"]],  # CaS
    "magnesium hydroxide": [element_list["magnesium"]] + [element_list["oxygen"]] * 2,  # Mg(OH)2
    "iron(II) sulfate": [element_list["iron"], element_list["sulfur"]] + [element_list["oxygen"]] * 4,  # FeSO4
    "iron(III) chloride": [element_list["iron"], element_list["chlorine"]] * 3,  # FeCl3
    "copper(II) oxide": [element_list["copper"], element_list["oxygen"]],  # CuO
    "potassium iodide": [element_list["potassium"], element_list["iodine"]],  # KI
    "calcium iodide": [element_list["calcium"], element_list["iodine"]] * 2,  # CaI2
    "sodium selenite": [element_list["sodium"], element_list["selenium"], element_list["oxygen"]],  # Na2SeO3
    "sodium thiocyanate": [element_list["sodium"], element_list["nitrogen"], element_list["carbon"], element_list["sulfur"]],  # NaSCN
    "calcium fluoride": [element_list["calcium"], element_list["fluorine"]],  # CaF2
    "potassium sulfate": [element_list["potassium"]] * 2 + [element_list["sulfur"]],  # K2SO4
    "potassium dichromate": [element_list["potassium"]] + [element_list["chromium"]] + [element_list["oxygen"]] * 4,  # K2Cr2O7
    "ammonium chloride": [element_list["nitrogen"], element_list["chlorine"]],  # NH4Cl
    "potassium bromide": [element_list["potassium"], element_list["bromine"]],  # KBr
    "sodium citrate": [element_list["sodium"], element_list["carbon"]] * 3 + [element_list["oxygen"]] * 7,  # C6H5Na3O7
    "sodium phosphite": [element_list["sodium"], element_list["phosphorus"]] * 3 + [element_list["oxygen"]],  # Na3PO3
}

