#!/usr/bin/env python

s = str(123)
s_capitalize1 = s.capitalize()
s_capitalize2 = s.capitalize('a')
s_center1 = s.center()
s_center2 = s.center(123)
s_center3 = s.center(123,'a')
s_center4 = s.center('abc')
s_center5 = s.center(123,123)
s_count1 = s.count()
s_count2 = s.count(123)
s_count3 = s.count('abc')
s_decode = s.decode('foo')
s_encode = s.encode('foo')
s_endswith = s.endswith('abc')
s_expandtabs1 = s.expandtabs()
s_expandtabs2 = s.expandtabs(123)
s_find = s.find('abc')
s_index = s.index('abc')
s_isalnum = s.isalnum()
s_join1 = s.join(('a','b','c'))
s_join2 = s.join(['a','b','c'])
s_join3 = s.join('abc')
s_join4 = s.join(123)
s_join5 = s.join(['a',123])
s_partition = s.partition('abc')
s_split = s.split(' ')
