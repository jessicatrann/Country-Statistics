# final.py
# ARMIN SANDHU, JESSICA TRAN, BLOCK 4, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
import numpy as np
import matplotlib.pyplot as plt
 
class World:
    '''A class used to create a World object.
        
        Attributes:
            region(str): String that represents a region in the world.
            country(str): String that represents a country in the world.
    '''
    def __init__(self, region, country):
        self.region = region
        self.country = country
    
    def country_stats(self):
        '''A function that prints out the user's input of the country and the region it belongs to.
        Parameters: None
        Return: None
        '''
        print(f'You have selected {self.country} in {self.region}')
    
    def region_stats(self):
        '''A function that prints out the user's input of the region they have chosen.
        Parameters: None
        Return: None
        '''
        print(f'You have selected {self.region}')
def mean(data, user_input2, column):
    '''A function that evaluates the mean value of a list of data that is also created in the function.
    Parameters:
    threatened_data: the imported data from the Threatened_Species csv file.
        column: the average of each column(which is the type of species) in the Threatened_Species csv file is made into a list.
    
    Return:
        The average of each threatened species.
    '''
    mean_list = []
    for x in range(1, 190):
        mean_list.append(data[x, column])
    mean_arr = np.array(mean_list).astype(int)
    mean_val = np.mean(mean_arr, dtype = int)
    return mean_val

def mean_region(data, list, column):
    '''A function that evaluates the mean value of a list of specific region data also created in the function.
    Parameters:
        data: the imported data from a given csv file.
        column: the specific column that is being evaluated.
    
    Return:
        The average of value of the specified data
    '''
    mean_region_list = []
    for x in range(1,194):
        if data[x,0] in list:
            mean_region_list.append(data[x, column])
    mean_region_arr = np.array(mean_region_list).astype(int)
    mean_region_val = np.mean(mean_region_arr, dtype = int)
    return mean_region_val
 
 
def main():
    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, dtype = str)                                     # Import the Country_Data csv file.
    pop_data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True, dtype = str)                                      # Import the Population_Data csv file.
    threatened_data = np.genfromtxt('Threatened_Species.csv', delimiter = ',', skip_header = True, dtype = str)                            # Import the Threatened_species csv file.
    
    print("ENDG 233 World Statistics\n")                                                                                                   # Display ENDG 233 World Statistics.
    un_region_list = sorted(['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'])                                                           # Sorted list of UN regions.
    print(f'List of UN regions:')                                                                                                          # Print list of UN regions.
    for x in un_region_list:                                                                                                               # Formatting of the list.
        if un_region_list.index(x) < len(un_region_list)-1:
            print(f'| {x}', end= ' ')    
        else:
            print(f'| {x} |')                                                                                                              # Display the sorted list of UN regions.
    while True:                                                                                                                            # Execute till break.
        user_input1 = input('\n\nSelect the region you would like to retrieve data for: ')                                                 # Prompt user to select a UN region they want to retrieve data for.
        if user_input1 in un_region_list:
            list_countries = []                                                                                                            # Create a list of countries that are in the region the user inputted.
            for x in range(1, 194):
                if user_input1 in country_data[x,1]:
                    list_countries.append(country_data[x,0])
                else:
                    continue
            break
        else:
            print('\nYou must enter a valid region.')                                                                                       # Prompt the user to enter a region from the list of UN regions.
    while True:
        user_input2 = input('Select the country you would like to retrieve data for, else re-enter the selected region for region data: ')  # Prompt the user to choose a country from the list of countries in the region or re-enter the region they inputted.
        if user_input2 == user_input1:                                                                                                      # Execute if the second input is the same as first input.
            print("\n***Requested Region Statistics***\n")
            World.region_stats(World(user_input1, user_input2))                                                                             # Call World class, and region_stats instance method, passing in the first and second user input.
            mean_pop_2020 = mean_region(pop_data, list_countries, 21)
            mean_size = mean_region(country_data, list_countries, 3)
            mean_species = 0
            for x in range(1,194):
                if threatened_data[x,0] in list_countries:
                    for p in range(1,5):
                        mean_species += int(threatened_data[x,p])
                else:
                    continue
            mean_species = mean_species // len(list_countries)
            print('\n{region:19}{pop:33}{size:19}{species:33}'.format(region='UN Region', pop='Mean population of 2020', size='Mean size', species='Mean Threatened Species'))
            print('-'*94)
            print('{region:<19}{pop:<33}{size:<19}{species:<33}'.format(region=user_input2, pop=mean_pop_2020, size=mean_size, species=mean_species))
            
            mean_region_pop = []                                                                                                           
            for x in range(1,22):                                                                                                           # Calling 'mean_region" function to find the mean population of the desired region for each year(2000 - 2020) and inputting this value into empty list above.
                mean_region_pop.append(mean_region(pop_data, list_countries, x))
            plot1 = plt.figure(1)                                                                                                           # Generating figure 1
            plt.subplot(1, 1, 1)                                                                                                            # Generate a plot in column 1, row 1, position 1
            plt.plot(range(2000, 2021), mean_region_pop, 'go', label = 'Mean Population')
            plt.ylabel('Mean Population')                                                                                                   # Label the y-axis as "Mean Population".
            plt.xlabel('Year')                                                                                                              # Label the x-axis as "Year".
            plt.xticks([2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020])
            plt.title(f'{user_input2} Mean Population from 2000-2020')                                                                      # Title the graph as "[the inputted region's] Mean Population form 2000-2020".
            plt.legend(shadow = True)                                                                                                       # Display the legend with a shadow.
          
            plot2 = plt.figure(2)
            region_mean_threatened = [mean_region(threatened_data, list_countries, 1), mean_region(threatened_data, list_countries, 2), mean_region(threatened_data, list_countries, 3), mean_region(threatened_data, list_countries, 4)]                                                                                     # Create a list of the average of each threatened species in the region.
            plt.subplot(1, 1, 1)                                                                                                            # Generate a plot in column 1, row 1, position 1
            plt.plot(['Plants', 'Fish', 'Birds', 'Mammals'], region_mean_threatened, 'bo', label = f'{user_input2} Mean Species')           # Plot the graph with the types of species, the mean threatened species in the region, blue dots, and label it as "[the inputted region] Mean species"
            plt.ylabel('Mean of Threatened Species')                                                                                        # Label the y-axis as "Mean of Threatened Species".
            plt.xlabel('Type of Species')                                                                                                   # Label the x-axis as "Type of Species"
            plt.title(f'Mean Threatened Species of {user_input2}')                                                                          # Title the graph as "Mean Threatened Species of [the inputed region]".
            plt.legend(shadow = True)                                                                                                       # Display the legend with a shadow.
            
            plt.show()                                                                                                                      # Display the plot
            break
 
        elif user_input2 in list_countries:
            print("\n***Requested Country Statistics***\n")                                                                                 # Display "***Requested Region Statistics***".
            World.country_stats(World(user_input1, user_input2))
            all_countries_list = list(country_data[:,0])
            pop_list = []                                                                                                                   # Create a list of the population for the country the user inputted.
            for x in range(1, 22):
                if user_input2 in all_countries_list:
                    pop_list.append(int(pop_data[all_countries_list.index(user_input2), x]))
            pop_arr = np.array(pop_list).astype(int)                                                                                        # Create an array of the population data for the country the user inputted.
            mean_pop = np.mean(pop_arr, dtype = int)                                                                                        # Compute the average of the population array for the country the user inputted.
            species_list = []                                                                                                               # Create a list of the amount of each type of threatened species of the country the user inputted.
            for x in range(1,5):
                if user_input2 in all_countries_list:
                    species_list.append(int(threatened_data[all_countries_list.index(user_input2), x]))
            species_arr = np.array(species_list).astype(int)                                                                                # Create an array of the threatened species data for the country the user inputted.
            mean_species = np.mean(species_arr, dtype = int)                                                                                # Compute the average of the threatened species array for the country the user inputted.                                                                                             
            print('\n{region:19}{country:17}{pop:40}{species:33}'.format(region='UN Region', country='Country', pop='Mean population from 2000-2020', species='Mean Threatened Species'))
            print('-'*99)
            print('{region:<19}{country:17}{pop:<40}{species:<33}'.format(region=user_input1, country=user_input2, pop=mean_pop, species=mean_species))
    
 
            year = list(range(2000, 2021))                                                                                                  # Create a list of years ranging from 2000 to 2020.
            plt.subplot(1, 1, 1)                                                                                                            # Create a plot with one row, one column, in position 1.
            plt.plot(year, pop_list, 'r--', label = user_input2)                                                                            # Plot the graph with the year, the population data, red dashed line, with a label of the user's input.
            plt.ylabel('Population of {0}'.format(user_input2))                                                                             # Label the y-axis with "Population of" the user's inputted country.
            plt.xlabel('Time(year)')                                                                                                        # Label the x-axis with "Time (year)".
            plt.title('Population of {0} v.s. Time'.format(user_input2))                                                                    # Title the graph with "Population of [the inputted country] v.s. Time"
            plt.legend(shadow = True, loc='upper right')                                                                                    # Display the label of the inputted country in the upper right of the graph with a shadow.
            plt.xticks(np.arange(min(year), max(year)+1, 5))                                                                                # Label the x-axis starting from the year 2000 increasing by 5 up to the year 2020.
            list_mean_threatened = [mean(threatened_data, user_input2, 1), mean(threatened_data, user_input2, 2), mean(threatened_data, user_input2, 3), mean(threatened_data, user_input2, 4)]                                                                                     # Create a list of the average of each threatened species of each country.
            list_country_threatened = [int(threatened_data[all_countries_list.index(user_input2), 1]), int(threatened_data[all_countries_list.index(user_input2), 2]), int(threatened_data[all_countries_list.index(user_input2), 3]), int(threatened_data[all_countries_list.index(user_input2), 4])]  # Create a list of the number of threatened species for the inputted country.
            plot2 = plt.figure(2)
            plt.subplot(3, 1, 1)                                                                                                            # Create a plot with one row, one column, in position 1.
            plt.plot(['Plants', 'Fish', 'Birds', 'Mammals'], list_mean_threatened, 'bo', label = 'World Mean')                              # Plot the graph with the types of species, the mean threatened species of all countries, blue dots, and label it as "World Mean"
            plt.ylabel('Mean of Threatened Species')                                                                                        # Label the y-axis as "Threatened Species".
            plt.xlabel('Type of Species')                                                                                                   # Label the x-axis as "Type of Species"
            plt.title('Type of Species v.s. Mean Threatened Species of the World')                                                          # Title the graph as "Type of Species v.s. Threatened Species".
            plt.legend(shadow = True, loc='upper right')                                                                                    # Display a legend from the label in the upper right of the graph with a shadow.
         
            plt.subplot(3,1,3)
            plt.plot(['Plants', 'Fish', 'Birds', 'Mammals'], list_country_threatened, 'go', label = f'{user_input2}\'s Mean')               # Plot the graph with the types of species, the amount of threatened species of the inputted country, green dots, and label it as "[Inputted Country] Mean".
            plt.ylabel('Amount of Threatened Species in {0}'.format(user_input2))                                                           # Label the y-axis as "Amount of Threatened Species in [inputted country]".
            plt.xlabel('Type of Species')                                                                                                   # Label the x-axis as "Type of Species"
            plt.legend(shadow = True, loc='upper right')                                                                                    # Display a legend from the label in the upper right of the graph with a shadow.
            plt.title('Type of Species v.s. Amount of Threatened Species in {0}'.format(user_input2))                                       # Title the graph as "Type of Species v.s. Amount of Threatened Species in [inputted country]".
            plt.show()                                                                                                                      # Display the graphs.
            break
        else:
            print('You must enter a valid option.')
  
  
 
if __name__ == '__main__':
   main()
