import matplotlib.pyplot as plt
import pandas as pd
import sys

def main(input_file, output_file, graph_file):
    print("--START--")

    eva_data = read_json_to_df(input_file)

    write_df_to_csv(eva_data, output_file)

    plot_cumulative_time_in_space(eva_data, graph_file)

    print("--END--")

def read_json_to_df(input_file):

    """
    Read a JSON file and return a Pandas DataFrame
    Clean the data by removing rows with missing values and sorting by date

    Args:
        input_file (str): path to the JSON file

    Returns:
        eva_df (pd.DataFrame): Pandas DataFrame containing the EVA data    

    """

    print(f'Reading JSON file {input_file}')
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df

def write_df_to_csv(eva_df,output_file):

    """
    Write a Pandas DataFrame to a CSV file

    Args:

        eva_df (pd.DataFrame): Pandas DataFrame containing the EVA data
        output_file (str): path to the output CSV file

    Returns:
        None
        
    """

    print(f'Writing DataFrame to CSV file {output_file}')
    eva_df.to_csv(output_file, index=False)
    return None

def plot_cumulative_time_in_space(eva_df, graph_file):

    """
    Plot the cumulative time spent in space over time

    Args:

        eva_df (pd.DataFrame): Pandas DataFrame containing the EVA data
        graph_file (str): path to the output graph file

    Returns:
        None

    """

    eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
    plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()
    return None

if __name__ == '__main__':

    if len (sys.argv) < 3:

        print('Using default input and output filenames')
        input_file = './data/eva-data.json'
        output_file = './results/eva-data.csv'

    else:

        print('Using input and output filenames provided as command-line arguments')
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    graph_file = './results/cumulative_eva_graph.png'

    main(input_file, output_file, graph_file)