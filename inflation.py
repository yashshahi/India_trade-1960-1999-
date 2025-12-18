#creating csv for the inflation data 
import pandas as pd

# Original data (unsorted)
data = {
    "Year": [
        1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981,
        1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971,
        1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962, 1961, 1960
    ],
    "Rate": [
        8.97, 7.07, 9.38, 8.8, 8.73, 5.56, 8.32, 11.87, 7.89, 13.11,
        11.35, 6.28, 2.52, 8.31, -7.63, 5.75, 28.6, 16.94, 6.44, 3.08,
        5.09, -0.58, 3.24, 13.06, 10.8, 9.47, 13.36, 2.95, 3.63, 1.7, 1.78
    ]
}
#source:(https://www.macrotrends.net/datasets/global-metrics/countries/ind/india/inflation-rate-cpi)

# Create DataFrame
df = pd.DataFrame(data)

# Sort by Year (chronological order)
df = df.sort_values(by='Year')

# Save to CSV
df.to_excel('inflation_1960_1990.xlsx', index=False)

print("CSV file created successfully!")

