words = 'Tomorrow is the defense'

# for idx in range(len(words)):
#     print words[idx]

# for char in words:
#     print char

for idx in range(len(words)):
    char = words[idx]
    #print 'Index: {} Character {}'.format(idx, char)
    print 'Character %s' % char

a_list = [1, 12, -3, 44, 51]
a_list.sort()
a_list.reverse()
for idx, element in enumerate(a_list):
    print 'Index! {} Element! {}'.format(idx, element)
