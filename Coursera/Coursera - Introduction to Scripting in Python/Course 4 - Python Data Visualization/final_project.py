"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.
Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table
#newtest = read_csv_as_nested_dict('test.csv','ISO3166-1-Alpha-2', ',', '"')
#print(newtest)
#print(newtest['AF']['ISO3166-1-Alpha-3'])  # AF
#print(newtest['ISO3166-1-Alpha-2']['ISO3166-1-Alpha-3'])  # AFG
#print(codeinfo['codefile'])




def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary
    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    #newtest = read_csv_as_nested_dict('test.csv','ISO3166-1-Alpha-2', ',', '"')
    newtest = read_csv_as_nested_dict(codeinfo['codefile'],
    codeinfo['plot_codes'], codeinfo['separator'], codeinfo['quote'])
    #print(newtest['Afghanistan']['ISO3166-1-Alpha-2'])
    dictionary = {}
    #table[rowid] = row
    #dictionary['AF'] = newtest['AF']['ISO3166-1-Alpha-3']
    for item in newtest:
      #print(item) #AF, AL, DZ, AS, AD
        dictionary[item] = newtest[item][codeinfo['data_codes']]
    #print(dictionary)
    #read_csv_as_nested_dict(codefile,'plot_codes', 'separator', '"')
    return dictionary
#build_country_code_converter({'plot_codes': 'Code1', 'codefile': 
# 'code1.csv', 'quote': "'", 'data_codes': 'Code2', 'separator': ','},)
#print(build_country_code_converter({'plot_codes': 'ISO3166-1-Alpha-2', 
# 'codefile': 'test.csv', 'quote': "'", 'data_codes': 'ISO3166-1-Alpha-3', 
# 'separator': ','},) )
# {'Ab': 'Cd', 'ST': 'UV', 'Gh': 'Ij', 'MN': 'OP'}


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data
    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.
      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    valid_countries = {}
    invalid_countries = set()

    lis = build_country_code_converter(codeinfo)
    #print(lis)
    #print(plot_countries['us'])

    for items in plot_countries:
        #print(items) items = us, pr, no

        if items.upper() in lis:  #US, PR, NO
          #print(lis[items.upper()]) #USA, PRI, NOR
            new = lis[items.upper()]
          #print(new)
            if new in gdp_countries:
            #print("yes") USA is in gdp_countries
                valid_countries[items] = new
            else:
            #print('No')
                invalid_countries.add(items)

        else:
          #print(items)
          #print('no')
            invalid_countries.add(items)
        #    valid_countries[countries] = plot_countries[countries]
        #else:
        #   invalid_countries.add(countries)

    #print(valid_countries)
    #print(invalid_countries)

    return (valid_countries, invalid_countries)

#print(reconcile_countries_by_code({'plot_codes': 'ISO3166-1-Alpha-2', 
# 'codefile': 'code4.csv', 'quote': '"', 'data_codes':
#  'ISO3166-1-Alpha-3', 'separator': ','}, #codeinfo
# {'us': 'United States', 'pr': 'Puerto Rico', 'no': 
# 'Norway', 'za': 'South Africa'}, #Plot Countries
# {'NOR': {'Country Code': 'NOR', 'Country Name': 'Norway'}, #gdp_countries
# 'USA': {'Country Code': 'USA', 'Country Name': 'United States'}, 
# 'PRI': {'Country Code': 'PRI', 'Country Name': 'Puerto Rico'}}))
#expected ({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}, set())

def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping
    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    #print(gdpinfo)
    newtest = read_csv_as_nested_dict(gdpinfo['gdpfile'],
    gdpinfo['country_code'], gdpinfo['separator'], gdpinfo['quote'])
    #print(newtest['USA']['1973'])
   
    new = reconcile_countries_by_code(codeinfo, plot_countries, newtest)
    #list_countries = new[0] 
    #print(list_countries)

    valid_countries = {}
    invalid_countries = set()
    zero_set = set()
    lis = build_country_code_converter(codeinfo)
    #print(lis)
    print(newtest['AND']['1960'])
    
    for items in plot_countries:
        #print(items) items = us, pr, no

        if items.upper() in lis:  #US, PR, NO
          #print(lis[items.upper()]) #USA, PRI, NOR
            new = lis[items.upper()]
          #print(new)
            if new in newtest:
              #print(new) #ASA
              if newtest[new][year] == '' or newtest[new][year] == 0:
                zero_set.add(items)
                #print(zero_set)

              else:
                 #print("yes") USA is in gdp_countries
                valid_countries[items] = math.log(float(newtest[new][year]), 10)
                #new_val[ans] = math.log(float(newtest[plot_countries[ans]][year]), 10)
            else:
              invalid_countries.add(items)
            #print('No')
                #invalid_countries.add(items)

        else:
          #print(items)
          #print('no')
            invalid_countries.add(items)
        #    valid_countries[countries] = plot_countries[countries]
        #else:
        #   invalid_countries.add(countries)

    #print(valid_countries)
    #print(invalid_countries)
    #print(zero_set)

    return  (valid_countries , invalid_countries ,  zero_set)

#build_map_dict_by_code({'country_code': 'Country Code', 'quote': '"', 'separator': ',', 'max_year': 2000, 'gdpfile': 'isp_gdp.csv', 'country_name': 'Country Name', 'min_year': 2000}, 
#{'plot_codes': 'ISO3166-1-Alpha-2', 'codefile': 'isp_country_codes.csv', 'quote': '"', 'data_codes':'ISO3166-1-Alpha-3', 'separator': ','}, 
#{'us': 'United States', 'pr': 'Puerto Rico', 'no':'Norway', 'za': 'South Africa', 'iq': 'Iraq'}, 
#'2001')

def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }
    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES
    #print(gdpinfo)
    #Code def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    data = build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '1960')
    
    worldmap_chart = pygal.maps.world.World()
    #worldmap_chart.(explicit_size=400,)
    worldmap_chart.title = 'GDP by Country for {} (log scale), unified by common country name' .format(20)
    worldmap_chart.add('GDP', data[0])
    worldmap_chart.add('Not in List', data[1])
    worldmap_chart.add('No data', data[2])
    worldmap_chart.render_to_file('chart2.svg')
    worldmap_chart.render_in_browser()


test_render_world_map()


