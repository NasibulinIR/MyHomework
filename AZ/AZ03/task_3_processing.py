import csv

def clean_price(price):
    return int(price.replace('руб.', '').replace(' ', ''))

input_file = 'divans.csv'
output_file = 'cleanned_prices.csv'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow([header[1]])

    for row in reader:
        clean_row = [clean_price(row[1])]
        writer.writerow(clean_row)
    print(f"Обработанные данные сохранены в файл {output_file}")


