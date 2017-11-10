s = '''It was the best of times, it was the worst of times; it was the age of wisdom, it was the age of foolishness; it was the epoch of belief, it was the epoch of incredulity; it was ...'''

newS = s.replace('.', ' ')          #a
newS = newS.replace(',', ' ')       #a
newS = newS.replace(';', ' ')       #a
newS = newS.replace('/n', ' ')      #a

newS = newS.replace('  ', ' ')

newS = newS.lower()

newS.count('it was')

