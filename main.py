import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv('covid_deaths.csv')

# Convert date column
df['start_date'] = pd.to_datetime(df['start_date'])

# Clean country column and get input
df['country'] = df['country'].str.strip().str.lower()
country = input("Enter a country name: ").strip().lower()

#  Filter
country_data = df[df['country'] == country]

#  Check if country data is found
if country_data.empty:
    print(f"No data found for '{country}'. Please check the country name.")
    print("Available countries:\n", df['country'].unique())
else:
    # Show latest rows
    print("\nLatest COVID-19 Data:")
    print(country_data[['start_date', 'covid_deaths', 'expected_deaths', 'excess_deaths']].tail())

    # Line plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='start_date', y='covid_deaths', data=country_data)
    plt.title(f'COVID Deaths Over Time in {country.title()}')
    plt.xlabel('Date')
    plt.ylabel('COVID Deaths')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    #  Bar chart
    latest = country_data.iloc[-1]
    labels = ['COVID Deaths', 'Expected Deaths', 'Excess Deaths']
    values = [latest['covid_deaths'], latest['expected_deaths'], latest['excess_deaths']]

    plt.figure(figsize=(6, 4))
    sns.barplot(x=labels, y=values)
    plt.title(f'Total Deaths Comparison in {country.title()} (Latest)')
    plt.tight_layout()
    plt.show()
#python main.py for running the code