#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import Fore
class DreamHousing:
    def __init__(self):
        self.apartments = [
            ['The Henry' , 'Downtown', 2550,['walk','bike', 'car'], True, 1989], 
            ['Anchor Apartments', 'Downtown',  2621, ['walk', 'bike', 'car'], True, 2451],
            ['The Jade Apartments', 'Downtown', 2802, ['bike', 'car'], True, 1720],
            ['South Willow Flats', 'Downtown',1200, ['walk', 'bike', 'car'], False, 1400],
            ['220 Madison Apartments', 'Downtown', 1300, ['walk', 'bike', 'car'], True, 1349],
            ['Novel Apartments', 'Midtown', 2103, ['bike', 'car'], True, 3206],
            ['Cora Midtown', 'Midtown', 2350, ['bike', 'car'], False, 37000],
            ['Element Tampa', 'Midtown', 2290, ['bike', 'car'], True, 3425],
            ['Urban Place', 'Uptown', 1374, ['car'], True, 2650],
            ['On 50', 'Uptown', 1479, ['car'], True, 939],
            ['Union on Fletcher', 'Uptown', 2085, ['car'], True, 1150],
            ['Varela Westshore Apartments', 'Westshore', 2435, ['car'], False, 2996],
            ['Novus Westshore', 'Westshore', 2137, ['car'], True, 2646],
            ['Mosaic Westshore', 'Westshore', 1930, ['car'], True, 3453],
            ['Society Westshore', 'Westshore', 1850, ['car'], True, 3200],
            ['The Mav Channelside', 'Channelside', 2130, ['bike', 'car'], True, 3750],
            ['Sky House', 'Channelside', 2218, ['bike', 'car'], True, 4397]
            ]
    def suggestion (self):
        print (Fore.MAGENTA + 'Welcome to DREAM HOUSING ! The most innovativate tool for off-campus housing')
        location_pref = input (Fore.CYAN + 'Please select your preffered location: Downtown, Midtown, Westshore, Channelside ')
        max_budget = float(input (Fore.MAGENTA + 'What is you max budget: '))
        fav_transportation = input (Fore.MAGENTA + 'Please choose your preffered method of transportation: walk , bike or car: ')
        international_student= input (Fore.YELLOW + 'Are you an International Student: (yes/no): ').lower()
        roommates_option = input (Fore.RED + 'Would you like to have roommates: (yes/no): ').lower()
    
        suggested_apartments = []
        for apartment in self.apartments:
            name, location, price, transport, is_international_friendly, roommates_price = apartment
            if (
                location.lower() == location_pref.lower() and
                (roommates_option == 'yes' or price <= max_budget) and
                fav_transportation.lower() in transport and
                (international_student == 'yes' and is_international_friendly or international_student == 'no')
            ):
                suggested_price = price if roommates_option == 'no' else roommates_price
                if suggested_price <= max_budget:
                    suggested_apartments.append((name, suggested_price))
                    
        if suggested_apartments:
            print (" Suggested apartments for you: ")
            for apartment, price in suggested_apartments:
                print('After looking through our database, we determine this will be the best fit for you', f"{apartment} - Price: {price}")
        else:
            print('Sorry, at the moment we do not have a match for you')
                    
finder = DreamHousing()
finder.suggestion()