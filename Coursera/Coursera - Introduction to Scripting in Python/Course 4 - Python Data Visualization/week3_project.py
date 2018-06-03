"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

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
#newtest = read_csv_as_nested_dict('isp_gdp_new.csv','Country Name', ',', '"')
#print(newtest)







def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
    """
    newtest = read_csv_as_nested_dict(gdpinfo['gdpfile'], 
    gdpinfo['country_name'], gdpinfo['separator'], gdpinfo['quote'])
   
    new_val = {}
    not_in = set()
    zero_set = set()
    


    for ans in plot_countries:
        #C2, C5, C4, C1, C2, C3
        #if int(newtest[plot_countries[plot_countries[ans]][year]) == 0:
        #    zero_set.add(ans)
        if plot_countries[ans] in newtest:
            #print(newtest[plot_countries[ans]][year])
            if newtest[plot_countries[ans]][year] == '' or\
            newtest[plot_countries[ans]][year] == 0 :

                zero_set.add(ans) #C2 must be added to zero_set not working

            #elif:
             #   new_val[ans] = math.log(int(newtest[plot_countries[ans]][year]), 10)
            else:
                new_val[ans] = math.log(float(newtest[plot_countries[ans]][year]), 10)
               
        else:
            not_in.add(ans)

    return new_val, not_in, zero_set


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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES
    #print(gdpinfo)
    #Code
    data = build_map_dict_by_name(gdpinfo, pygal_countries, '2003')
    
    worldmap_chart = pygal.maps.world.World()
    #worldmap_chart.(explicit_size=400,)
    worldmap_chart.title = 'GDP by Country for {} (log scale), unified by common country name' .format(2003)
    worldmap_chart.add('GDP', data[0])
    worldmap_chart.add('Not in List', data[1])
    worldmap_chart.add('No data', data[2])
    worldmap_chart.render_to_file('chart.svg')
    worldmap_chart.render_in_browser()


test_render_world_map()




