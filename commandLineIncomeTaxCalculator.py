#!/usr/bin/python

import sys

incomeTaxPaidBefore = 0.00
finalIncomeTax = 0.00


def CPPDeductionFunc(yearNum):
    global cpp
    if yearNum >= 58700:
        cpp = 2898.00
    elif yearNum < 58700:
        cpp = (yearNum - 3500) * 0.0525
    return cpp



def EIDeductionFunc(yearNum):
    global ei
    if yearNum >= 54200:
        ei = 856.36
    elif yearNum < 54200:
        ei = yearNum * 0.0158
    return ei   



def federalTax(yearNum):
    global federalIncomeTax
    if yearNum >= 214368:
        federalIncomeTax = (48535 * 0.15) + (48534 * 0.205) + (53404 * 0.26) + (63895 * 0.29) + ((yearNum - 214368) * 0.33)
    elif yearNum >= 150473:
        federalIncomeTax = (48535 * 0.15) + (48534 * 0.205) + (53404 * 0.26) + ((yearNum - 150473)* 0.29)
    elif yearNum >= 97069:
        federalIncomeTax = (48535 * 0.15) + (48534 * 0.205) + ((yearNum - 97069) * 0.26)
    elif yearNum >= 48535:
        federalIncomeTax = (48535 * 0.15) + ((yearNum - 48535) * 0.205)
    elif yearNum < 48535:
        federalIncomeTax = yearNum * 0.15
    return federalIncomeTax



def provincialTax(yearNumA):
    global provincialIncomeTax
    if yearNumA >= 220000:
        provincialIncomeTax = (44740 * 0.0505) + (44742 * 0.0905) + (60518 * 0.1116) + (70000 * 0.1216) + ((yearNumA - 220000) * 0.1316)
    elif yearNumA >= 150000:
        provincialIncomeTax = (44740 * 0.0505) + (44742 * 0.0905) + (60518 * 0.1116) + ((yearNumA - 150000)* 0.1216)
    elif yearNumA >= 89482:
        provincialIncomeTax = (44740 * 0.0505) + (44742 * 0.0905) + ((yearNumA - 89482) * 0.1116)
    elif yearNumA >= 44740:
        provincialIncomeTax = (44740 * 0.0505) + ((yearNumA - 44740) * 0.0905)
    elif yearNumA < 44740:
        provincialIncomeTax = yearNumA * 0.0505
    return provincialIncomeTax

if len(sys.argv) > 2:
    print("Invalid Input")

income = float(sys.argv[1].replace(' ', ''))

finalIncomeTax = federalTax(income) + provincialTax(income) + CPPDeductionFunc(income) + EIDeductionFunc(income)
netIncome = income - finalIncomeTax

print("Final Income Tax Owed: " + str(round(finalIncomeTax, 2)) + "\nFederal Tax: " + str(round(federalIncomeTax, 2)) + "\nProvincial Tax: "
      + str(round(provincialIncomeTax, 2)) + "\nCPP Deduction: " + str(round(cpp, 2)) + "\nEI Deduction: " + str(round(ei, 2)) + "\nNet Income: " + str(round(netIncome, 2)))

#Income Tax Calculator for Ontario, Canada. Note: The numbers are for 2019-2020 season.
#*****************Does not take into account Tax Credits***********











