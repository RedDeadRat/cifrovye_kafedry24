money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0  # Счетчик месяцев

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
total_spend1 = 0
total_spend2 = 0

while True:
    money_capital+=(salary-spend)  #Баланс на конец месяца
    if money_capital < 0:  #Если баланс отрицателен, то придется брать в долг
        break
    count += 1
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", count)
