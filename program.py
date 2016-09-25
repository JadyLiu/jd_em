import os
import csv
import io

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)
    print(data)

def print_header():
    print('---------------------------') 
    print('REAL ESTATE DATA MINING APP') 
    print('---------------------------')
    print('')

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder,'data','file.csv')

def load_file(filename):
    with io.open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline().strip()
        print('header found'+ header)


        lines = []
        for line in fin:
            line_data = line.strip().split('.')
            bed_count = line_data[4]
            lines.append(line_data)
        print(lines[:5])

def query_data(data):
    pass


if __name__ == '__main__':
    main()