with open('input.txt', 'r') as f:
    inp = [line.strip() for line in f]

inp.append('')

groups = []
responses = {}
responses.setdefault('answers', [])
unique = ''
all_letters = ''

for line in inp:
    if line != '':
            responses['answers'].append(line)
            for letter in line:
                all_letters = all_letters + letter
                if letter not in unique:
                    unique = unique + letter
            
    else:
        checked_letters = []
        yes = 0
        members = len(responses['answers'])
    
        for letter in all_letters:
            if letter in checked_letters:
                continue
            else:
                checked_letters.append(letter)
                count = all_letters.count(letter)
                if count == members:
                    yes += 1
        
        questions = len(unique)
        responses['questions'] = questions
        responses['unique_letters'] = unique
        responses['all_yes'] = yes
        
        groups.append(responses)
        
        responses = {}
        responses.setdefault('answers', [])
        unique = ''
        all_letters = ''

questions = 0
all_yes = 0
for group in groups:
    q = group['questions']
    questions += q

    y = group['all_yes']
    all_yes += y

print(f"Part 1 Solution: {questions}")
print(f"Part 2 Solution: {all_yes}")