# Jacob Meadows
# February 17th, 2018
"""
Material for Chemistry
"""
periodic_table = {
    ("Hydrogen", "H", 1): (1.0079, 14.3),
    ("Helium", "He", 2): (4.0026, 5.193),
    ("Lithium", "Li", 3): (6.941, 3.57),
    ("Beryllium", "Be", 4): (9.0122, 1.820),
    ("Boron", "B", 5): (10.811, 1.030),
    ("Carbon", "C", 6): (12.011, 0.710),
    ("Nitrogen", "N", 7): (14.0067, 1.040),
    ("Oxygen", "O", 8): (15.9994, 0.919),
    ("Fluorine", "F", 9): (18.9984, 0.824),
    ("Neon", "Ne", 10): (20.1797, 1.030),
    ("Sodium", "Na", 11): (22.9898, 1.230),
    ("Magnesium", "Mg", 12): (24.3050, 1.020),
    ("Aluminum", "Al", 13): (26.9815, 0.904),
    ("Silicon", "Si", 14): (28.085, 0.710),
    ("Phosphorus", "P", 15): (30.9738, 0.770),
    ("Sulfur", "S", 16): (32.065, 0.705),
    ("Chlorine", "Cl", 17): (35.45, 0.478),
    ("Argon", "Ar", 18): (39.948, 0.520),
    ("Potassium", "K", 19): (39.0983, 0.757),
    ("Calcium", "Ca", 20): (40.078, 0.631),
    ("Scandium", "Sc", 21): (44.9559, 0.567),
    ("Titanium", "Ti", 22): (47.867, 0.520),
    ("Vanadium", "V", 23): (50.9415, 0.489),
    ("Chromium", "Cr", 24): (51.9961, 0.448),
    ("Manganese", "Mn", 25): (54.9380, 0.479),
    ("Iron", "Fe", 26): (55.845, 0.449),
    ("Cobalt", "Co", 27): (58.9332, 0.421),
    ("Nickel", "Ni", 28): (58.6934, 0.445),
    ("Copper", "Cu", 29): (63.546, 0.384),
    ("Zinc", "Zn", 30): (65.409, 0.388),
    ("Gallium", "Ga", 31): (69.723, 0.371),
    ("Germanium", "Ge", 32): (72.64, 0.321),
    ("Arsenic", "As", 33): (74.9216, 0.328),
    ("Selenium", "Se", 34): (78.96, 0.321),
    ("Bromine", "Br", 35): (79.904, 0.947),
    ("Krypton", "Kr", 36): (83.798, 0.248),
    ("Rubidium", "Rb", 37): (85.4678, 0.364),
    ("Strontium", "Sr", 38): (87.62, 0.300),
    ("Yttrium", "Y", 39): (88.9059, 0.298),
    ("Zirconium", "Zr", 40): (91.224, 0.278),
    ("Niobium", "Nb", 41): (92.9064, 0.265),
    ("Molybdenum", "Mo", 42): (95.94, 0.251),
    ("Technetium", "Tc", 43): (97.9072, 0.063),
    ("Ruthenium", "Ru", 44): (101.07, 0.238),
    ("Rhodium", "Rh", 45): (102.9055, 0.240),
    ("Palladium", "Pd", 46): (106.42, 0.240),
    ("Silver", "Ag", 47): (107.8682, 0.235),
    ("Cadmium", "Cd", 48): (112.411, 0.230),
    ("Indium", "In", 49): (114.818, 0.233),
    ("Tin", "Sn", 50): (118.710, 0.217),
    ("Antimony", "Sb", 51): (121.760, 0.207),
    ("Tellurium", "Te", 52): (127.60, 0.201),
    ("Iodine", "I", 53): (126.9045, 0.429),
    ("Xenon", "Xe", 54): (131.293, 0.158),
    ("Cesium", "Cs", 55): (132.9055, 0.242),
    ("Barium", "Ba", 56): (137.327, 0.205),
    ("Lanthanum", "La", 57): (138.9055, 0.195),
    ("Cerium", "Ce", 58): (140.116, 0.192),
    ("Praseodymium", "Pr", 59): (140.9077, 0.193),
    ("Neodymium", "Nd", 60): (144.24, 0.190),
    ("Promethium", "Pm", 61): (144.9127, None),
    ("Samarium", "Sm", 62): (150.36, 0.196),
    ("Europium", "Eu", 63): (151.964, 0.182),
    ("Gadolinium", "Gd", 64): (157.25, 0.240),
    ("Terbium", "Tb", 65): (158.9253, 0.182),
    ("Dysprosium", "Dy", 66): (162.50, 0.167),
    ("Holmium", "Ho", 67): (164.9303, 0.165),
    ("Erbium", "Er", 68): (167.259, 0.168),
    ("Thulium", "Tm", 69): (168.9342, 0.160),
    ("Ytterbium", "Yb", 70): (173.04, 0.154),
    ("Lutetium", "Lu", 71): (174.967, 0.154),
    ("Hafnium", "Hf", 72): (178.49, 0.144),
    ("Tantalum", "Ta", 73): (180.9479, 0.140),
    ("Tungsten", "W", 74): (183.84, 0.132),
    ("Rhenium", "Re", 75): (186.207, 0.137),
    ("Osmium", "Os", 76): (190.23, 0.130),
    ("Iridium", "Ir", 77): (192.217, 0.131),
    ("Platinum", "Pt", 78): (195.078, 0.133),
    ("Gold", "Au", 79): (196.9666, 0.129),
    ("Mercury", "Hg", 80): (200.59, 0.139),
    ("Thallium", "Tl", 81): (204.3833, 0.129),
    ("Lead", "Pb", 82): (207.2, 0.127),
    ("Bismuth", "Bi", 83): (208.9804, 0.122),
    ("Polonium", "Po", 84): (208.9824, None),
    ("Astatine", "At", 85): (209.9871, None),
    ("Radon", "Rn", 86): (222.0176, 0.0936),
    ("Francium", "Fr", 87): (223.0197, None),
    ("Radium", "Ra", 88): (226.0254, 0.092),
    ("Actinium", "Ac", 89): (227.0277, 0.120),
    ("Thorium", "Th", 90): (232.0381, 0.118),
    ("Protactinium", "Pa", 91): (231.0359, 0.099),
    ("Uranium", "U", 92): (238.0289, 0.116),
    ("Neptunium", "Np", 93): (237.0482, None),
    ("Plutonium", "Pu", 94): (244.0642, None),
    ("Americium", "Am", 95): (243.0614, None),
    ("Curium", "Cm", 96): (247.0704, None),
    ("Berkelium", "Bk", 97): (247.0703, None),
    ("Californium", "Cf", 98): (251.0796, None),
    ("Einsteinium", "Es", 99): (252.0830, None),
    ("Fermium", "Fm", 100): (257.0951, None),
    ("Mendelevium", "Md", 101): (258.0984, None),
    ("Nobelium", "No", 102): (259.101, None),
    ("Lawrencium", "Lr", 103): (262.1097, None),
    ("Rutherfordium", "Rf", 104): (261.1088, None),
    ("Dubnium", "Db", 105): (262.1141, None),
    ("Seaborgium", "Sg", 106): (266.1219, None),
    ("Bohrium", "Bh", 107): (264.12, None),
    ("Hassium", "Hs", 108): (277, None),
    ("Meitnerium", "Mt", 109): (268.1388, None),
    ("Darmstadtium", "Ds", 110): (247.0704, None),
    ("Roentgenium", "Rg", 111): (280, None),
    ("Copernicium", "Cn", 112): (285, None),
    ("Nihonium", "Nh", 113): (284, None),
    ("Flerovium", "Fl", 114): (289, None),
    ("Moscovium", "Mc", 115): (288, None),
    ("Livermorium", "Lv", 116): (293, None),
    ("Tennessine", "Ts", 117): (294, None),
    ("Oganesson", "Og", 118): (294, None),
}


def molar_mass(x):
    global end_mass
    n = periodic_table.keys()
    for l in n:
        if x in l:
            end_mass = l
            break
        else:
            end_mass = None
    return periodic_table[end_mass][0]


def specific_heat(x):
    global end_mass
    n = periodic_table.keys()
    for l in n:
        if x in l:
            end_mass = l
            break
        else:
            end_mass = None
    return periodic_table[end_mass][1]
