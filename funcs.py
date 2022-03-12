
     ##### Calculate flux based on = (membrane diameter (m), time interval (secs), permeate quantity (ml)) #####

import math as m
import numpy as np


def flux_p(a,b,c):

    '''(membrane diameter (m), time interval (secs), permeate quantity (ml))'''

    m_area = (a**2)*m.pi
    l_h = (c/1000)*(3600/b)
    flux_calc = l_h/m_area

    print('Flux (lmh): ''%.2f' % flux_calc)



     ##### Calculate solution needed based on = (membrane radius (m), desntiy (g/cm), thickness (nm), concentration(mg_ml)) #####

def coating(a,b,c,d):

    '''(membrane radius (m), desntiy (g/cm), thickness (nm), concentration(mg_ml))'''

    m_area = m.pi*(float(a)*100)**2
    mass_mg = (m_area*(c/10000))*b
    solution_needed = mass_mg/d

    print('Mass Required (mg): ''%.5f' % mass_mg)
    #print('%.5f' % m_area)
    print('Solution Required (ml): ''%.5f' % solution_needed)





def flux_g():

        '''(membrane radius (m), time (secs), tube radius (cm), permeate height (cm)'''

        d = float(input("Measurement height in cm: "))

        m1 = float(input("1st Measurement: "))
        m2 = float(input("2nd Measurement: "))
        m3 = float(input("3rd Measurement: "))

        mt = (m1+m2+m3)/3


        m_area = ((10/1000)**2)*m.pi
        v = (m.pi*(0.8**2)*d)/1000
        l_h = (3600/mt)*v
        flux_calc = l_h/m_area

        print('Flux (lmh): ''%.2f' % flux_calc)




def tubevol():

    a = float(input("Cm: "))
    vol = a*2.01
    ppm = vol*1000

    print('ml: ''%.2f' % vol)
    print('ppm: ''%.2f' % ppm)
