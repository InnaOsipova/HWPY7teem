import calc as c
import log as l

def ask_user ():
    choise = input("Какой калькулятор выбираем c - комплексными числами, r - рациональные")
    if choise == "c":
        l.add_log("Пользователь выбрал работу с комплексными числами")
        c.calc_complex()
    if choise == "r":
        l.add_log("Пользователь выбрал работу с комплексными числами")
        c.calc_ration()
