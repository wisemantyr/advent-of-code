with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f]

inp.append('')

valid_fields = ['byr', 'iyr','eyr','hgt', 'hcl','ecl','pid']
cid = 'cid'

passport_count = 0
valid_count = 0

kv_strings = []
fields = []

for line in inp:
    if line != '':
        kv_strings=line.split()
        for string in kv_strings:
            pair = string.split(':')
            fields.append(pair[0])
    else:
        passport_count += 1
        
        diff_fields = []
        diff_fields = [x for x in fields + valid_fields if x not in fields or x not in valid_fields]
        
        if len(diff_fields) == 1:
            if cid in diff_fields:
                valid_count += 1
        elif len(diff_fields) == 0:
            valid_count += 1
        
        kv_strings = []
        fields =[]

print(valid_count)