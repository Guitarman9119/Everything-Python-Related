"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
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

#newtest = read_csv_as_nested_dict('isp_gdp.csv','Country Name', ',', '"')
#newtest = read_csv_as_nested_dict('isp_gdp_new.csv','Country Name', ',', '"')

#print(newtest)
#print(newtest.keys)

#country_names = (newtest.keys())  #Die gee vir my n list van die CSV file wat keys is

#print(country_names)


def build_plot_values(gdpinfo, gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.

    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    maximum_year = (gdpinfo.get('max_year'))
    min_year = (gdpinfo.get('min_year'))
    #print(min_year)

    year_gdp = []
    
    for year in gdpdata:
        if not year.isdigit(): 
            continue
        elif gdpdata[year] == ' ' or gdpdata[year] == '' :
            continue
        elif int(year) < min_year or int(year) > maximum_year:
            continue
        else:
            gdp = gdpdata[year]
            gdp_converted = float(gdp)
            year_gdp.append((int(year), gdp_converted))

    year_gdp_sorted = sorted(year_gdp , key = lambda x:x[0]) 
    
    #print(year_gdp_sorted)
    return year_gdp_sorted

#build_plot_values(newtest, newtest['Andorra'])
#Als werk nog hier
#build_plot_values({'quote': '', 'separator': ',', 'max_year': 2000, 'gdpfile': 'isp_gdp_new.csv', 
# 'min_year': 1980, 'country_code': 'Code', 'country_name':
#  'Country Name'},{'1990': '20', '2020': '20' })


#build_plot_values(newtest, )


def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    newtest = read_csv_as_nested_dict(gdpinfo['gdpfile'], 
    gdpinfo['country_name'], gdpinfo['separator'], gdpinfo['quote'])
    
    print(newtest)
    ans = {}

    for country in country_list:
        if country not in newtest:
            ans[country] = []
        else:  
            gdp_list_tupels = build_plot_values(gdpinfo, newtest[country])
            ans[country] = gdp_list_tupels
    
    #print(ans)
    return ans

#build_plot_dict({'separator': ',', 'min_year': 2000, 'country_name': 
# 'Country Name', 'quote': '"', 'gdpfile': 'gdptable1.csv', 
# 'max_year': 2005, 'country_code': 'Code'}, ['Country3'])
#build_plot_dict({'separator': ',', 'min_year': 2000, 'country_name': 'Country Name', 'quote': '"',
# 'gdpfile': 'isp_gdp_new.csv', 'max_year': 2005, 'country_code': 'Code'}, ['Aruba'])

def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
   
    data = build_plot_dict(gdpinfo, country_list)
    print(data)
    print(country_list)
    nested_list = []

    for country in range(len(country_list)):
        nested_list.append(data[country_list[country]])
    print(nested_list)

    
    xy_chart = pygal.XY()
    xy_chart = pygal.XY(explicit_size=400, title='GDP 1960-2015', x_title ='Years' , y_title='GDP Growth')
    #xy_chart = pygal.XY(title='GDP 1960-2015', x_title ='Years' , y_title='GDP Growth')
    #xy_chart = pygal.XY(width=1000)
    for country in range(len(country_list)):
        xy_chart.add(country_list[country], nested_list[country])
    
    xy_chart.render_in_browser()
    xy_chart.render_to_file(plot_file)
    
    

    return

def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
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
    #render_xy_plot(gdpinfo, ['Aruba','Andorra'], "isp_gdp_xy_Aruba.svg")
    #render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    render_xy_plot(gdpinfo, ["Canada", "Japan", "South Africa",'Australia'],
                   "isp_gdp_xy_uk+usa.svg")

# Make sure the following call to test_render_xy_plot is commented out
# when submitting to OwlTest/CourseraTest.
test_render_xy_plot()