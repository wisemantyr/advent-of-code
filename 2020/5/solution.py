import math
import pandas as pd

with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f]

first_row = 0
last_row = 127

first_col = 0
last_col = 7


def front(seat_range):
    first = seat_range[0]
    last = math.floor(((seat_range[1]-first)/2) + first)
    return (first, last)

def back(seat_range):
    last = seat_range[1]
    first = round(((last - seat_range[0])/2) + seat_range[0])
    return (first, last)

def get_row(first, last, seats):
    seat_range = (first, last)
    for letters in seats[0:7]:
        for index in letters:
            if index == 'F':
                seat_range = front(seat_range)
            else:
                seat_range = back(seat_range)
    row = seat_range[1]
    return row

def get_col(first, last, seats):
    seat_range = (first, last)
    for letters in seats[7:]:
        for index in letters:
            if index == 'L':
                seat_range = front(seat_range)
            else:
                seat_range = back(seat_range)
    col = seat_range[1]
    return col


def get_id(row,col):
    return (row * 8) + col

seats = []

for seat in inp:
    row = get_row(first_row, last_row, seat)
    col = get_col(first_col, last_col, seat)
    seat_id = get_id(row,col)
    
    seat_info = {}
    seat_info['id'] = seat_id
    seat_info.setdefault('seat', (row, col))
    seats.append(seat_info)

highest_id = max(seat['id'] for seat in seats)
print(f"Part 1 Solution: {highest_id}")

seat_ids = [seat['id'] for seat in seats]
assigned = [seat['seat'] for seat in seats]
rows = [x for x,y in assigned]
cols = [y for x,y in assigned]

data = {'id': seat_ids, 'row': rows, 'col': cols}
seats_df = pd.DataFrame.from_dict(data)
seats_df = seats_df.set_index('id')

high_row = seats_df['row'].max()
low_row = seats_df['row'].min()

seats_df = seats_df.loc[(seats_df['row'] != high_row) & (seats_df['row'] != low_row)]
row_groups = seats_df.groupby('row').size()
rows_open = row_groups[row_groups < 8]
row_nums_open = rows_open.index.to_list()

rows_open_df = seats_df.loc[seats_df['row'].isin(row_nums_open)]
open_seats_rows = rows_open_df['row'].to_list()
open_seats_cols = rows_open_df['col'].to_list()

seated_nearby = list(zip(open_seats_rows, open_seats_cols))

col_nums = [num for num in range(first_col, last_col + 1)]

all_nearby = []
for row in row_nums_open:
    for col in col_nums:
        seat = (row,col)
        all_nearby.append(seat)

missing_seats = [seat for seat in seated_nearby + all_nearby
                if seat not in seated_nearby or seat not in all_nearby]


def check_surrounding(missing_seats, assigned):
    for a in missing_seats:
        count_true = 0
        
        seat_up = (a[0] + 1, a[1])
        seat_down = (a[0] - 1, a[1])
        seat_left = (a[0], a[1] + 1)
        seat_right = (a[0], a[1] - 1)
        
        check_seats = [seat_up, seat_down, seat_left, seat_right]
        
        for b in check_seats:
            for c in assigned:
                if b == c:
                    count_true += 1
        if count_true == 4:
            return a

my_seat = check_surrounding(missing_seats, assigned)
my_seat_id = get_id(my_seat[0], my_seat[1])

print(f"Part 2 Solution: {my_seat_id}")

