trades = int(input('How many pairs do you want to analyze: '))
good = 0
average = 0
bad = 0

for x in range(trades):
    print('Fill in your trade details.')
    pair = input('Pair: ')
    entry = float(input('Entry Price: '))
    stop = float(input('Stop Loss: '))
    profit = float(input('Take Profit: '))

    print(f'Pair: {pair}')
    print(f'Entry: {entry}')
    print(f'Stop: {stop}')
    print(f'Profit: {profit}')

    risk = entry - stop

    if risk <= 0:
        print('Error! Invalid risk!')
        continue

    reward = profit - entry
    rrr = reward/risk

    if rrr >= 2:
        print(f'Good trade setup.')
        good = good + 1
    elif rrr >= 1:
        print(f'Average setup. ')
        average = average + 1
    else:
        print(f'Avoid this trade!')
        bad = bad + 1

print('Trade Summary:')
print(f'Total Trades Analyzed: {trades}')
print(f'Good Trades: {good} ')
print(f'Average Trades: {average}')
print(f'Bad Trades: {bad}')

print('Bonus Metrics:')
good_trades_percentage = good / trades * 100
print(f'Percentage of Good trades: {good_trades_percentage} %')











