import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):
   return \
       ((text.lower()).translate(str.maketrans('','',string.punctuation))).replace(' ','') == \
       (((reverse(text)).lower()).translate(str.maketrans('','',string.punctuation))).replace(' ','')

something = input('Текст - ')

if is_palindrome(something):
    print('Это палиндром')
else:
    print('Это не палиндром')


# print(reverse('кот'))


