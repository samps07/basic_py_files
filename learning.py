def find_all_occurrences(s, p):
    indices = []
    for i in range(len(s)):
        match = True
        for j in range(len(p)):
            if s[i + j] != p[j]:
                match = False
                break
        if match:
            indices.append(i)
    print(indices[i] for i in range(len(indices)))

# Example usage
s = 'harry goes to a public school not a private school'
p = 'school'
find_all_occurrences(s,p)


                
        