from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('./txt_file.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./txt_file.txt', mode = 'w') as translation_file
            translation_file.write(translation)
except FileNotFoundError as e:

    print('Check File Path')
