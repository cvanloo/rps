R = 1
P = 2
S = 3

print((R - R), (R - R) % 3, 'TIE')
print((R - P), (R - P) % 3, 'LOSE')
print((R - S), (R - S) % 3, 'WIN')

print((P - R), (P - R) % 3, 'WIN')
print((P - P), (P - P) % 3, 'TIE')
print((P - S), (P - S) % 3, 'LOSE')

print((S - R), (S - R) % 3, 'LOSE')
print((S - P), (S - P) % 3, 'WIN')
print((S - S), (S - S) % 3, 'TIE')
