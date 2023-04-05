name = 'Sun'

# "SuI"
print(name.replace('n', 'I'))

# True
print(name.startswith('S'))

# True
print(name.endswith('n'))

# False
print(name.isupper())

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# list 맨 앞에 'Inseon'을 추가
days_of_week.insert(0, 'Inseon')
print(days_of_week)

# list 맨 뒤에 'Inseon'을 추가
days_of_week.append('Inseon')
print(days_of_week)

# list 에서 'Inseon'을 삭제
days_of_week.remove('Inseon')
print(days_of_week)

# list 에서 맨 앞에 있는 요소를 삭제
days_of_week.pop(0)
print(days_of_week)

# list 에서 맨 뒤에 있는 요소를 삭제
days_of_week.pop()
print(days_of_week)

# Tuple
# Tuple 에서 요소를 삭제하려고 하면 에러 발생
days = ("Mon", "Tue", "Wed")

print(days.count('Mon'))
print(days.index('Wed'))

# Dictionary
player = {
    'name': 'sun',
    'age': 20,
    'alive': True
}
print(player)
print(player.get('name'))
player['xp'] = 1500
print(player)
