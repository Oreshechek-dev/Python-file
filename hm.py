investment_list = ["технології", "зелена енергетика", "освіта", "здоров'я", "фінтех"]

def check_investment():
    print("Ласкаво просимо до інвестиційного додатку!")
    print("Введіть назву вашого продукту:")

    product = input().strip().lower()
    if product in [item.lower() for item in investment_list]:
        print("Вітаємо! Ваш продукт цікавий для мене. Ви отримаєте необхідні інвестиції.")
    else:
        print("На жаль, ваш продукт не входить до моїх сфер інтересів. Мені це нецікаво.")

if __name__ == "__main__":
    while True:
        check_investment()
        print("\nЧи хочете ви продовжити? (так/ні)")
        answer = input().strip().lower()
        if answer != "так":
            print("Дякуємо за використання додатку. До побачення!")
            break
