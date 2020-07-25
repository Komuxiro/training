# Данная программа измеряет композицию (состав) тела, замеры производятся с помощью калипера и рассчете на основе
# этих данных процентного содержания жира.
print('Эта программа поможет вам посчитать состав вашего тела')
fatPercentage = ()  # процент жира

print('Введите свой возвраст (значение должно быть целым числом)')
age = int(input())  # возраст
print("Введите свой пол: 'Male' если вы мужчина, 'Female' если вы женщина")
sex = input()  # пол

# считаем состав тела - мужчины
while sex == 'Male':
    # Входные данные
    print("Введите показание измерения толщины складки на боку в 'мм'.")
    foldSide = int(input())  # складка на боку

    print("Введите показание измерения толщины складки на животе в 'мм'.")
    creaseStomach = int(input())  # складка на животе

    print("Введите показание измерения толщины складки на груди в 'мм'.")
    creaseChest = int(input())  # складка на груди

    print("Введите показние измерения толщины складки в подмышечной впадине в 'мм'.")
    axillaryFold = int(input())  # складка в подмышечной впадине

    # подсчет результата
    a = (foldSide + creaseStomach + creaseChest + axillaryFold) * 0.27784
    b = (a ** 2) * 0.000053
    c = age * 0.12437
    fatPercentage = (a - b + c) - 3.28791
    print('Процент жира: %.1f' % (fatPercentage))
    break

# считаем состав тела - женщины
while sex == 'Female':
    # Входные данные
    print("Введите показание измерения толщины складки на задней поверхности плеча в 'мм'.")
    creaseBackShoulder = int(input())  # складка на задней поверхности плеча

    print("Введите показание измерения толщины складки на боку в 'мм'.")
    foldSideFemale = int(input())  # складка на боку

    print("Введите показание измерения толщины складки на животе в 'мм'.")
    creaseStomachFemale = int(input())  # складка на животе

    # подсчет результата
    a = (creaseBackShoulder + foldSideFemale + creaseStomachFemale) * 0.41563
    b = (a ** 2) * 0.00112
    c = age * 0.03661
    fatPercentage = (a - b + c) - 4.03653
    print('Процент жира: %.1f' % (fatPercentage))
    break
