import os
import base64
import pandas as pd
import psycopg2
from pprint import pprint

path = r'C:\Users\ptishchenko\Desktop\Новая папка'

names_list = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
files_list = os.listdir(path)


image64_list = []
for files in files_list:
    if files.endswith('.png') or files.endswith('.jpeg') or files.endswith('.jpg') :
        with open(path + '/' + files, 'rb') as image:
            image_64 = base64.b64encode(image.read())
            image_base64 = 'data:image/png;base64,' + str(image_64).strip("b'")
            image64_list.append(image_base64)
    else: pass


value = []
for i in image64_list:
    value.append(f'[{{"key": "image","type": "string","value": \"{i}\"}}]')


dict = {'name': names_list, 'value': value}
dict_table = {'Наименование': names_list, 'Изображение': image64_list}


df = pd.DataFrame(dict)
df_table = pd.DataFrame(dict_table)
print(df_table)


df_table.to_csv(f'{path}/РНИС.xlsx', index=False, encoding='CP1251')

# conn = psycopg2.connect(host='', port='5432', user='', password='', database='')
# cursor = conn.cursor()

# for index, row in df.iterrows():
#     cursor.execute(f"INSERT INTO bi.reference_information_values(reference_id,name,value,attributes) "
#                    f"VALUES(75, '{row['name']}', 1, '{row['value']}')")
#     conn.commit()
#
# cursor.close()
# conn.close()


header=True

