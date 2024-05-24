def print_table():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    
    col_widths = [0] * len(table_data)
    
    for i in range(len(table_data)):
        for a in table_data[i]:
            col_widths[i] = max(col_widths[i], len(a))
    
    for i in range(len(table_data[0])):
        for j in range(len(table_data)):
            print(table_data[j][i].rjust(col_widths[j]), end=' ')
        print()

print_table()

