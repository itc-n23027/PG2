import pyinputplus as pyip


prices = {
    '小麦パン': 1.0, '白パン': 1.0, 'サワー種': 1.5,
    'チキン': 2.0, 'ターキー': 2.0, 'ハム': 2.0, '豆腐': 2.0,
    'チェダー': 0.5, 'スイス': 0.5, 'モツァレラ': 0.5,
    'マヨネーズ': 0.25, 'からし': 0.25, 'レタス': 0.25, 'トマト': 0.25
}

 
exchange_rate = 110


bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='パンの種類を選んでください:\n')

protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n')

cheese_needed = pyip.inputYesNo('チーズが必要ですか？ (yes/no)\n')


if cheese_needed == 'yes':
    cheese = pyip.inputMenu(['チェダー', 'スイス', 'モツァレラ'], prompt='チーズの種類を選んでください:\n')
else:
    cheese = None


mayo = pyip.inputYesNo('マヨネーズが必要ですか？ (yes/no)\n')

mustard = pyip.inputYesNo('からしが必要ですか？ (yes/no)\n')

lettuce = pyip.inputYesNo('レタスが必要ですか？ (yes/no)\n')

tomato = pyip.inputYesNo('トマトが必要ですか？ (yes/no)\n')


number_of_sandwiches = pyip.inputInt('サンドイッチはいくつほしいですか？ (1以上の整数)\n', min=1)


total_price_dollars = prices[bread] + prices[protein]
if cheese:
    total_price_dollars += prices[cheese]
if mayo == 'yes':
    total_price_dollars += prices['マヨネーズ']
if mustard == 'yes':
    total_price_dollars += prices['からし']
if lettuce == 'yes':
    total_price_dollars += prices['レタス']
if tomato == 'yes':
    total_price_dollars += prices['トマト']

total_price_dollars *= number_of_sandwiches


total_price_yen = total_price_dollars * exchange_rate


print(f'合計金額は {total_price_yen:.0f} 円です。')


