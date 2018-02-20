# Jacob Meadows
# February 18th, 2018
"""
Formulas for Chemistry
"""
import Chemistry_Material


def heat_formula(m, e, ti, tf):
    d = (m * Chemistry_Material.specific_heat(e) * (tf - ti))
    return d
