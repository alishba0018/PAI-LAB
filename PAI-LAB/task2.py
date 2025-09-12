def vorc(string):
     if string.endswith('a')==True or string.endswith('e')==True or string.endswith('i')==True or string.endswith('o')==True or string.endswith('u')==True:
          return 'is vowel'
     else:
          return 'not vowel'     

print(vorc('hi my name is alishba'))
