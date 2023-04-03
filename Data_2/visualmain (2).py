import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file):
    """
    Load CSV file and return two dataframes, one with years and one with countries as column.
    """
    df = pd.read_csv(file)
    years = [str(year) for year in range(2011, 2022)] # assumes years are from 2011 to 2021
    df.set_index('Country Name', inplace=True)
    df = df.loc[countries, years]
    return df, pd.DataFrame(years, columns=['Year'])


# Define list of countries to plot
countries = ['Canada', 'Brazil', 'Bangladesh', 'China', 'Ecuador', 'France', 'India', 'Nigeria',
             'Russian Federation', 'South Africa', 'Sweden', 'United Kingdom', 'United States']

# Load methane emissions CSV file
methane_file = 'API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_4903685.csv'
methane_df, methane_years_df = load_data(methane_file)

# Plot bar graph of methane emissions for the specified years
methane_df.plot(kind='bar')
plt.title('Methane Emissions by Country')
plt.xlabel('Country')
plt.ylabel('Methane Emissions')
plt.show()

# Load poverty head count CSV file
poverty_file = 'API_SI.POV.DDAY_DS2_en_csv_v2_5349804.csv'
poverty_df, poverty_years_df = load_data(poverty_file)

# Plot bar graph of poverty head count for the specified years
poverty_df.plot(kind='bar')
plt.title('Poverty Head Count by Country')
plt.xlabel('Country')
plt.ylabel('Poverty Head Count')
plt.show()

# Plot pie chart of poverty head count for the specified years
poverty_total = poverty_df.sum(axis=1)
plt.pie(poverty_total, labels=countries, autopct='%1.1f%%')
plt.title('Poverty Head Count by Country')
plt.show()

# Load access to electricity CSV file
electricity_file = 'API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_5356635.csv'
electricity_df, electricity_years_df = load_data(electricity_file)

# Set x and y values
x = electricity_df.index.values
y = electricity_df['2018'].values

# Create point plot
plt.plot(x, y, 'o')
plt.title('Access to Electricity by Country')
plt.xlabel('Country')
plt.ylabel('Access to Electricity')
plt.show()


# Load electricity power consumption CSV file
power_file = 'API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_5354744.csv'
power_df, power_years_df = load_data(power_file)

# Plot bar graph of electricity power consumption for the specified years
power_df.plot(kind='bar')
plt.title('Electricity Power Consumption by Country')
plt.xlabel('Country')
plt.ylabel('Electricity Power Consumption')
plt.show()

# Load urban population percentage CSV file
urban_file = 'API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5351947.csv'
urban_df, urban_years_df = load_data(urban_file)

# Plot line graph of urban population percentage for the specified years
urban_df.plot(kind='line', marker='o')
plt.title('Urban Population Percentage by Country')
plt.xlabel('Year')
plt.ylabel('Urban Population Percentage')
plt.legend(loc='upper left')
plt.show()

# Plot a heat map of methane emissions for all countries across years
methane_countries_df = methane_df.loc[countries, :].astype(float)
plt.figure(figsize=(10, 8))
sns.heatmap(methane_countries_df, cmap='YlGnBu')
plt.title('Methane Emissions by Country Across Years')
plt.xlabel('Year')
plt.ylabel('Country')
plt.show()