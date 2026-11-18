# Скрипт анализа нагрузки на сервер за N дней
# В этом коде есть 2 логические ошибки для практического задания на код-ревью

days = int(input("Введите количество дней мониторинга: "))
high_load_days = 0

for day in range(1, days):
    total_requests = 0
    requests = int(input(f"Запросов за день {day}: "))
    total_requests += requests

    if requests > 100:
        high_load_days += 1

print("Итоги мониторинга:")
print("Всего запросов за период:", total_requests)
print("Дней с пиковой нагрузкой (>100):", high_load_days)


# Эталонное исправленное решение (для проверки учителем)
# Ошибка 1: total_requests = 0 выносим до цикла, чтобы сумма накапливалась.
# Ошибка 2: в range ставим days + 1, чтобы не терять последний день.
#
# days = int(input("Введите количество дней мониторинга: "))
# high_load_days = 0
# total_requests = 0
#
# for day in range(1, days + 1):
#     requests = int(input(f"Запросов за день {day}: "))
#     total_requests += requests
#     if requests > 100:
#         high_load_days += 1
#
# print("Итоги мониторинга:")
# print("Всего запросов за период:", total_requests)
# print("Дней с пиковой нагрузкой (>100):", high_load_days)
