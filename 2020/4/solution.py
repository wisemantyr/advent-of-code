import re

with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f]

inp.append('')

valid_fields = ['byr', 'iyr','eyr','hgt', 'hcl','ecl','pid']
cid = 'cid'

passport_count = 0
valid_count = 0

kv_strings = []
fields = []
values = []
results = {"valids": []}

for line in inp:
    if line != '':
        kv_strings = line.split()
        for string in kv_strings:
            pair = string.split(':')
            fields.append(pair[0])
            values.append(pair[1])
    else:
        passport_count += 1
        
        diff_fields = []
        diff_fields = [x for x in fields + valid_fields if x not in fields or x not in valid_fields]
        
        if len(diff_fields) == 1:
            if cid in diff_fields:
                valid_count += 1
                passport = dict(zip(fields, values))
                results['valids'].append(passport)
        elif len(diff_fields) == 0:
            valid_count += 1
            passport = dict(zip(fields, values))
            results['valids'].append(passport)
        
        kv_strings = []
        fields =[]
        values =[]

print(f"Solution (pt. 1): {valid_count}")

byr_min = 1920
byr_max = 2002

iyr_min = 2010
iyr_max = 2020

eyr_min = 2020
eyr_max = 2030

cm_min = 150
cm_max = 193

in_min = 59
in_max = 76

pid_max = 9

ecl_opts = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

num_keys = ['byr','iyr', 'eyr']

v = results['valids']

for p in v:
    for key in num_keys:
        p[key]=int(p[key])
        
    if p['byr'] < byr_min or p['byr'] > byr_max:
        p.clear()
        continue
    if p['iyr'] < iyr_min or p['iyr'] > iyr_max:
        p.clear()
        continue
    if p['eyr'] < eyr_min or p['eyr'] > eyr_max:
        p.clear()
        continue
        
    if len(p['pid']) != pid_max:
        p.clear()
        continue
        
    hgt = p['hgt']

    if 'cm' not in hgt:
        if 'in' not in hgt:
            p.clear()
            continue
    if 'in' not in hgt:
        if 'cm' not in hgt:
            p.clear()
            continue
        
    if 'cm' in hgt:
        newhgt = re.split('(cm)', hgt)
        newhgt[0] = int(newhgt[0])
        p['hgt'] = newhgt[:2]
        if p['hgt'][0] < cm_min or p['hgt'][0] > cm_max:
            p.clear()
            continue
    if 'in' in hgt:
        newhgt = re.split('(in)', hgt)
        newhgt[0] = int(newhgt[0])
        p['hgt'] = newhgt[:2]
        if p['hgt'][0] < in_min or p['hgt'][0] > in_max:
            p.clear()
            continue
    
    if p['ecl'] not in ecl_opts:
        p.clear()
        continue
    
    if p['hcl'][0] != '#':
        p.clear()
        continue
    if len(p['hcl']) > 7:
        p.clear()
        continue
    

v = [i for i in v if i]
print(f"Solution (pt. 2): {len(v)}")