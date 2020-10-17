# clinguistics
## Комментарий к программе 14(создание словаря)
**_Задание_**. На вход программе дается два слова: _русское_ и _английское_. Необходимо создать словарь, в который будут заноситься данные значения.

**Важно учитывать**, что нам не гарантировано, что пользователь введет слово, состоящее только из символов _кириллицы_ или _латиницы_, он также может вводить цифры, перемешивать символы. Поэтому необходимо сделать так называемую _проверку от дурака_.:eyes:

Что надо сделать, чтобы выполнить _проверку от дурака_:
1. Проверить, есть  в введенном значении цифры;
2. Проверить, содержатся в слове кроме букв от A до Z(a - z) буквы от А до Я(а - я) или наоборот: если кроме букв от А до Я(а - я) в значении содеражатся буквы от A до Z(a - z);
3. Если значение не соответствует условиям, вывести _Wrong answer_.

Вот пример ввода и вывода данных моей программы:
| 1 слово  | 2 слово  | Вывод                                             |
| ---------| :-------:| :-------------------------------------------------|
| h8llo    | goodbye  | wrong answer                                      |
| hello    | g88dbye  | wrong answer                                      |
| hello    | привет   | Русское слово - привет; The English word is hello |
| helлоу   | приvet   | wrong answer                                      |
  
Код можно найти по этой [ссылке](https://github.com/asaunina/clinguistics/commit/2a223af4d5eaa9ba54394957deb8d8af4022d8ba) :point_right::point_left:

Хорошего настроения! 

![Хорошего настроения!](https://sun9-26.userapi.com/c855028/v855028059/9a934/ZKeZ9Rua94E.jpg)
