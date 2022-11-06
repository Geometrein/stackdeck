import os
import json
import requests

import pandas as pd

URL = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/yskp/statfin_yskp_pxt_13qb.px'

QUERY = {
  "query": [
    {
      "code": "Sukupuoli",
      "selection": {
        "filter": "item",
        "values": [
          "S"
        ]
      }
    },
    {
      "code": "Ammattiluokitus 2010",
      "selection": {
        "filter": "item",
        "values": [
          "25",
          "251",
          "2511",
          "2512",
          "2513",
          "2514",
          "2519",
          "252",
          "2521"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}


def get_json_response() -> json:
    api_response = requests.post(URL, json=QUERY)
    json_data = json.loads(api_response.text)
    return json_data


def parse_fields(json_data: json) -> pd.DataFrame:
    row_index = json_data['dimension']['Ammattiluokitus 2010']['category']['index']
    row_labels = json_data['dimension']['Ammattiluokitus 2010']['category']['label'].values()

    column_index = json_data['dimension']['Tiedot']['category']['index']
    column_label = json_data['dimension']['Tiedot']['category']['label']

    flat_values = json_data['value']

    n_columns = len(column_index)
    nested_values = [flat_values[i:i + n_columns] for i in range(0, len(flat_values), n_columns)]

    new_df = pd.DataFrame(data=nested_values, columns=column_label)
    new_df.drop(columns=['sans_91'], inplace=True)
    new_df['label'] = row_labels
    return new_df


def clean_up(input_df: pd.DataFrame) -> pd.DataFrame:
    column_names = {
        'lkm': 'number',
        'sans_ka': 'average',
        'sans_p10': 'decile_1',
        'sans_median': 'median',
        'sans_p90': 'decile_9',
    }
    input_df.rename(columns=column_names, inplace=True)
    column_order = ['label', 'number', 'average', 'decile_1', 'median', 'decile_9']
    return input_df[column_order]


def get_salaries() -> pd.DataFrame:
    response = get_json_response()
    df = parse_fields(json_data=response)
    df = clean_up(input_df=df)
    return df


def get_salaries_dict():

    items = []

    salaries_df = get_salaries()
    data_dict = salaries_df.to_dict('records')
    for row in data_dict:
        items.append(row)
    return items


if __name__ == '__main__':
    get_salaries_dict()
