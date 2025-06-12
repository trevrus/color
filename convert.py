import csv

with open('BM/Williamsburg/WILLIAMSBURG_Collection.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print("INSERT INTO fs_colors (color_code, color_name, hex_code, manufacturer, deck) VALUES")
    rows = []
    for row in reader:
        # Escape single quotes for SQL
        values = [row['color_code'],
                  row['color_name'].replace("'", "''"),
                  row['hex_code'],
                  row['manufacturer'],
                  row['deck']]
        rows.append("('{}', '{}', '{}', '{}', '{}')".format(*values))
    print(",\n".join(rows) + ";")

  