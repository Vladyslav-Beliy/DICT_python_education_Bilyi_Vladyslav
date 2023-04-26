import math
import sys

example1 = '$ python credit_calculator/credit_calculator.py --diff (principal) (periods) (interest)'
example2 = '$ python credit_calculator/credit_calculator.py --annuity --m (principal) (payment) (interest)'
example3 = '$ python credit_calculator/credit_calculator.py --annuity --p (payment) (periods) (interest)'

arg = sys.argv

print('Welcome to credit calculator\n')
print('for help enter:\n$ python credit_calculator/credit_calculator.py --help\n\n')


def period_calc():
    loan1 = float(arg[3])
    mon_pay1 = float(arg[4])
    loan_int1 = float(arg[5])
    i = loan_int1 / (12 * 100)

    months1 = math.ceil(math.log((mon_pay1 / (mon_pay1 - i * loan1)), (1 + i)))
    years = math.floor(months1 / 12)
    months_part = months1 - years * 12
    if months1 == 0:
        print(f"It will take {years} years to repay this loan!")
    elif years == 0:
        print(f"It will take {months1} months to repay this loan!")
    elif months1 == 0 and years == 0:
        print(f"It will take nothing to repay this loan!")
    else:
        print(f"It will take {years} years and {months_part} months to repay this loan!")


def month_calc():
    loan1 = float(arg[3])
    months1 = float(arg[4])
    loan_int1 = float(arg[5])
    i = loan_int1 / (12 * 100)
    mon_pay1 = math.ceil(loan1 * (i * ((1 + i) ** months1)) / (((1 + i) ** months1) - 1))
    print(f"Your monthly payment = {mon_pay1}")


def diff_calc():
    dm1 = []
    n = 0
    x = 1
    nomer = 0

    loan_p = float(arg[2])
    inter = float(arg[4])
    loan_i = inter / 12 / 100
    months = float(arg[3])
    m = months
    while m != 0:
        dm = (float(loan_p) / int(months)) + float(loan_i) * (float(loan_p) - ((float(loan_p) * (m - 1)) / int(months)))
        m = m - 1
        dm1.append(math.ceil(dm))
    dm1.reverse()
    while x <= len(dm1):
        print(f'Month {x}: payment is {dm1[nomer]}' )
        x = x + 1
        nomer = nomer + 1
    while len(dm1) > 1:
        try:
            result_1 = dm1[n] + dm1[n + 1]
            n = n + 1
            dm1.append(result_1)
            if len(dm1) > 1:
                dm1.__delitem__(0)

        except IndexError:
            print(f'You have to pay {dm1[-1]}$')
            print(f'Overpayment = {dm1[-1] - loan_p}$')
            break


if arg[1] == '--diff' and len(arg) == 5:
    diff_calc()

elif arg[1] == '--annuity' and arg[2] == '--p' and len(arg) == 6:
    period_calc()

elif arg[1] == '--annuity' and arg[2] == '--m' and len(arg) == 6:
    month_calc()

elif arg[1] == '--help':
    print(f'Variant looks like this\n'
          f'this is example for diff:\n{example1})\n'
          f'-m is for month calculation:\n{example2}\n'
          f'-p is for period calculation:\n{example3}')

else:
    print(f'Incorrect format\nCorrect variant looks like this\n'
          f'{example1})\n'
          f'or like this\n'
          f'{example2}\n'
          f'and this\n'
          f'{example3}')
