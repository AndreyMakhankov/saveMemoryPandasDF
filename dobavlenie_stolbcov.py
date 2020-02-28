import os
import time

import pandas
import pandas as pd
import numpy as np

def vivesti_stolbec_faila(path, extension):
    """Функция для вывода одного или нескольких столбцов из файла Excel в "path" нужно прописать путь до файла без
    расширения. Пример - ('C:/Users/USER/Desktop/1') в "extension" нужно прописать расширение файла. Пример - ('.xls)
    в "stolbec" нужно прописать необходимые столбцы. Пример "A, C, E:J" либо можно написать наименования столбцов (
    "company", "rank", "revenues") """
    file = path + extension
    data = pandas.read_excel(file)
    return data

def get_name_df():
     df = vivesti_stolbec_faila(r'C:/Users/USER/Desktop/1', '.xlsx')
     return df


# help(vivesti_stolbec_faila) # Функция справки python используется для отображения документации модулей, функций,
# классов, ключевых слов и т. Д.



# print("\n--- список всех столбцов в вытащеном файле ---\n",
# df.columns.tolist())  # - показать листы в данном примере список будет иметь 2 элемента - [0,1] - эти
# элементы содержат заголовки столбцов


gl_obj = get_name_df().select_dtypes(include=['object']).copy()
converted_obj = get_name_df().select_dtypes(include=['object']).copy()
print(gl_obj.describe())


def mem_usage(pandas_obj):
    if isinstance(pandas_obj, pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    usage_mb = usage_b / 1024 ** 2  # преобразуем байты в мегабайты
    return "{:03.2f} MB".format(usage_mb)

print(get_name_df().info(memory_usage='deep'))

for col in gl_obj.columns:
    num_unique_values = len(gl_obj[col].unique())
    num_total_values = len(gl_obj[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:, col] = gl_obj[col].astype('category')
    else:
        converted_obj.loc[:, col] = gl_obj[col]

# df.to_excel(r'C:/Users/USER/Desktop/3.xls')   # записать в файл
print('До оптимизации столбцов: '+mem_usage(gl_obj))
print('После оптимизации столбцов: '+mem_usage(converted_obj))