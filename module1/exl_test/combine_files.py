import csv
from collections import defaultdict
import pandas as pd


def normalize_csv(filename, new_file) -> str:
    val_file = new_file
    with open(filename, encoding='utf-8') as file:
        data_file = csv.reader(file, delimiter=',')
        normalized_data = list(data_file)[4:]

    with open(new_file, encoding='utf-8', mode='w') as new_file:
        data_in_file = csv.writer(new_file, delimiter=',', lineterminator='\r')
        for row in normalized_data:
            data_in_file.writerow(row)
    return val_file


def find_info(filename, year, default_dict):
    with open(filename, encoding='utf-8') as first_file_csv:
        data_first_file = csv.DictReader(first_file_csv, delimiter=',')
        for row in data_first_file:
            if row[year]:
                for key, val in row.items():
                    if key.find('Country Name') != -1:
                        default_dict[val].append(row[year])


def execute_search(first_file, second_file, year, default_dict):
    find_info(first_file, year, default_dict)
    find_info(second_file, year, default_dict)


def combine_csv_files(first_file, second_file, data_year):
    countries = []
    first_indicator = []
    second_indicator = []

    normalized_first_file = normalize_csv(first_file, 'first_file_normalized.csv')
    normalized_second_file = normalize_csv(second_file, 'second_file_normalized.csv')
    data_dict = defaultdict(list)

    execute_search(normalized_first_file, normalized_second_file, data_year, data_dict)

    for country, indicators in data_dict.items():
        if len(indicators) > 1:
            countries.append(country)
            first_indicator.append(indicators[0])
            second_indicator.append(indicators[1])
    return countries, first_indicator, second_indicator


def write_to_excel(data_set: tuple, filename, first_argument, second_argument):
    file_xlsx = pd.DataFrame(
        {
            'Countries': data_set[0],
            first_argument: [round(float(item), 3) for item in data_set[1]],
            second_argument: [round(float(item), 3) for item in data_set[2]]
        }
    )
    file_xlsx.to_excel(filename, index=False)


if __name__ == '__main__':
    first_filename = 'Export_import/API_NE.EXP.GNFS.ZS_DS2_en_csv_v2_3012018.csv'
    second_filename = 'API_AG.PRD.CROP.XD_DS2_en_csv_v2_3012354/API_AG.PRD.CROP.XD_DS2_en_csv_v2_3012354.csv'
    our_data = combine_csv_files(first_filename, second_filename, '2018')
    write_to_excel(our_data, 'Special_for_Vanya.xlsx', 'Експорт', 'Індекс виробництва зернових культур')
