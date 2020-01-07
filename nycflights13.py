import pandas as pd

def main():
    flights_dataframe = pd.read_csv('flights.csv')
    airline_dataframe = pd.read_csv('airlines.csv')

    joined_dataframe = pd.merge(flights_dataframe, airline_dataframe, on='carrier')
    data_top = joined_dataframe.columns
    print(joined_dataframe)
    drop_rows = []
    for index, row in joined_dataframe.iterrows():
        for i in data_top:
            if(pd.isnull(row[i])):
                drop_rows.append(index)
                break

    dropped_data_frame = joined_dataframe.drop(drop_rows)
    print(dropped_data_frame)

main()