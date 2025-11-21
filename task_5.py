class TestCase():

    def __init__(self, steps=None, result=None):
        # Если steps не передается, то создаем пустой словарь
        if steps is None:
            steps = {}
        self.steps = steps
        self.result = result

    # Метод set_step — добавляет в словарь steps шаг тест-кейса.
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    # Метод delete_step — удаляет шаг из steps по ключу step_number, который передали в метод.
    def delete_step(self, step_number):

        self.steps.pop(step_number)

    # Метод set_result — устанавливает ожидаемый результат. Он помещает его в атрибут result по параметру result, который передали методу.
    def set_result(self, result):
        self.result = result

    # Метод get_test_case — печатает информацию о составе тест-кейса в формате:

    def get_test_case(self):
        result_dict = {'Шаги': self.steps, 'Ожидаемый результат': self.result}
        return result_dict


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()