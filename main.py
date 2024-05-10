import Operations
import database_operations


def clr():
    print("\n" * 60)
    return ""


class Menu:
    operations = None

    def __init__(self, operations):
        self.operations = operations

    @staticmethod
    def about_record() -> (str, str, str):  # get info about record
        record_category = input(f"{clr()} Выберите категорию (Расход/прибыль) -> ").capitalize()
        if record_category not in ("Расход", "Прибыль"):
            input(f"{clr()}Вы можете выбрать лишь одну категорию (расход или доход)!")
            return

        record_sum = input(f"{clr()} Введите сумму -> ").capitalize()
        if not record_sum.isdigit():
            input(f"{clr} Вы ввели неверную сумму платежа! Пишите только числа, пожалуйста!")

        record_annotation = input(f"{clr()} Введите комментарий -> ").replace(" ", "_")

        return record_category, record_sum, record_annotation

    def show_menu(self):
        print("(Введите цифру в консоли для управления)\n\n"
              "Меню:\n"
              "  1. Показать баланс и все записи\n"
              "  2. Добавление записи\n"
              "  3. Редактирование записи\n"
              "  4. Поиск по записям")

        try:
            select = int(input("-> "))
        except (Exception, ValueError):
            clr()
            input("Вы ввели неверное значение (принимаются только числа от 1 до ..)")
            clr()
            return

        clr()
        if select == 1:
            self.operations.get_balance_and_records()
            input("Чтобы продолжить, нажмите на любую кнопку")
            clr()
        elif select == 2:
            record_category, record_sum, record_annotation = self.about_record()
            self.operations.push_record(record_category, record_sum, record_annotation)
            input("Запись успешно добавлена! Чтобы продолжить, нажмите на любую кнопку")
            clr()
        elif select == 3:
            record_id = input(f"{clr()} Какое ID у записи, которую необходимо изменить? -> ")
            if not record_id.isdigit():
                input(f"{clr()} Вы ввели неверную сумму платежа! Пишите только числа, пожалуйста!")

            record_category, record_sum, record_annotation = self.about_record()
            self.operations.edit_record(record_id, record_category, record_sum, record_annotation)

            input("Запись успешно изменена! Чтобы продолжить, нажмите на любую кнопку")
            clr()
        elif select == 4:
            record_category = input(f"{clr()} Какая категория должна быть у записей? (Расход/доход/любая) -> ").capitalize()

            if record_category == "Любая" or "" or " ":
                record_category = None
            if record_category not in ("Расход", "Доход", None):
                input(f"{clr()}Вы можете выбрать категорию только из списка! (расход, доход или любая)!")
                return

            record_date = input(f"{clr()} Какая дата у записей должна быть?"
                                f" Если любая, то ENTER! (формат: 2024-05-02) -> ").capitalize()
            record_sum = input(f"{clr()} Какая сумма должна быть у записей? Если любая, то ENTER! -> ")
            clr()
            self.operations.search_records(record_category, record_sum, record_date)

            input("Поиск выполнен успешно! Чтобы продолжить, нажмите на любую кнопку")
            clr()


if __name__ == "__main__":
    clr()
    menu = Menu(Operations.Operations(database_operations.TextDB()))
    while True:
        menu.show_menu()
