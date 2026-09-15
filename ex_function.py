# // create list of languages 
# // print all languages
# // if you can speak that language, print 'i can speak' if not 'i can not speak'


# listoflanguage = ['english','nepali','hindi','german']
# print(listoflanguage)

# language = (input('what language can you speak?'))
# print(language)

# if language == "english" :
#     print('i can speak')
# else :
#     print('i can not speak')


# def languagesiknow():
#     listoflanguage = ['english','nepali','hindi','german']
#     print(listoflanguage)

#     language = (input('what language can you speak?'))
#     print(language)

#     if language == "english" :
#         print('i can speak')
#     else :
#         print('i can not speak')

# languagesiknow()




mylanguage = ['english','chinese','burmese']
for language in mylanguage:
    result = input('can you speak '+ language +"?. say only 'yes'and 'no' ")

    if result == ('yes'): 
        print('yes i can speak')

    else :
        print('no i can not speak')