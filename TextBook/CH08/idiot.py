import pyinputplus as pyip

while True:
    prompt = 'バカを何時間も忙しくしておく方法を知りたいですか？\n'
    response = pyip.inputYesNo(prompt,yesVal='はい', noVal='いいえ')
    if response == 'いいえ':
        break
    print('ありがとう、ごきげんよう。')