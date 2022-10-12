# Домашнее задание

Движение игровых объектов по полю.
Цель:

Выработка навыка применения SOLID принципов на примере игры "Космическая битва".
В результате выполнения ДЗ будет получен код, отвечающий за движение объектов по игровому полю, устойчивый к появлению новых игровых объектов и дополнительных ограничений, накладываемых на это движение.

Описание/Пошаговая инструкция выполнения домашнего задания:

В далекой звездной системе встретились две флотилии космических кораблей. Корабли могут передвигаться по всему пространству звездной системы по прямой, поворачиваться против и по часовой стрелке, стрелять фотонными торпедами. Попадание фотонной торпеды в корабль выводит его из строя.
От каждой флотилии в сражении принимают участие по три космических корабля.
Победу в битве одерживает та флотилия, которая первой выведет из строя все корабли соперника.
Управление флотилиями осуществляется игрокам компьютерными программами (то есть не с клавиатуры).
Концептуально игра состоит из трех подсистем:

    Игровой сервер, где реализуется вся игровая логика.
    Player - консольное приложение, на котором отображается конкретная битва.
    Агент - приложение, которое запускает программу управления танками от имени игрока и отправляет управляющие команды на игровой сервер.
    Реализовать движение объектов на игровом поле в рамках подсистемы Игровой сервер.


Критерии оценки:

За выполнение каждого пункта, перечисленного ниже начисляются баллы:

    ДЗ сдано на проверку - 1 балл
    Оформлен pull/merge request на github/gitlab - 1 балл
    Настроен CI - 2 балла
    Прямолинейное равномерное движение без деформации.
        Само движение реализовано в виде отдельного класса - 1 балл.
        Для движущихся объектов определен интерфейс, устойчивый к появлению новых видов движущихся объектов - 1 балл
        Реализован тесты:

    Для объекта, находящегося в точке (12, 5) и движущегося со скоростью (-7, 3) движение меняет положение объекта на (5, 8)
    Попытка сдвинуть объект, у которого невозможно прочитать положение в пространстве, приводит к ошибке
    Попытка сдвинуть объект, у которого невозможно прочитать значение мгновенной скорости, приводит к ошибке
    Попытка сдвинуть объект, у которого невозможно изменить положение в пространстве, приводит к ошибке
    1 балл

    Поворот объекта вокруг оси.
        Сам поворот реализован в виде отдельного класса - 1 балл
        Для поворачивающегося объекта определен интерфейс, устойчивый к появлению новых видов движущихся объектов - 1 балл
        Реализован тесты - 1 балл.
        Итого: 10 баллов
        Задание считается принятым, если набрано не менее 7 баллов.

# Запуск
## без создания отчёта
### UI
В pycharm я запускал move.feature 
Слева был треугольник run test
### CLI
    python -m behave ./features
## c созданием allure отчёта
в папке move запускаем:

    python -m behave -f allure_behave.formatter:AllureFormatter -o report ./features

# Конфигурирование:
Установить python 3.11

Установить pip
https://bootstrap.pypa.io/get-pip.py.

py get-pip.py

https://pip.pypa.io/en/stable/installation/

pip install behave
https://pypi.org/project/behave/
https://behave.readthedocs.io/en/stable/tutorial.html?highlight=features#features

pip install allure-behave
https://pypi.org/project/allure-behave/

pip install mock

pip install numpy

install allure
https://docs.qameta.io/allure

it needs java:

https://docs.oracle.com/en/java/javase/11/install/installation-jdk-microsoft-windows-platforms.html#GUID-371F38CC-248F-49EC-BB9C-C37FC89E52A0
-   To set JAVA_HOME, do the following:
-   a. Right click My Computer and select Properties.
-   b. On the Advanced tab, select Environment Variables, and then edit JAVA_HOME to point to where the JDK software is located, for example, C:\Program Files\Java\jdk1.6.0_02.

# Вывести справку о behave

python -m behave -h

# Allure
allure generate -c report -o allure-report

allure open allure-report

https://stackoverflow.com/questions/49267027/how-to-allure-behave-generate-report-from-test-cases-allure-generated-only-one

# code style
## isort
python -m pip install isort
### run 
isort .
## mypy
python -m pip install mypy
### run 
mypy .
## flake8
python -m pip install flake8
### run
flake8
## code coverage
pip install coverage
### run
coverage run C:\Users\agrusha\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\behave\__main__.py
в файле .coveragerc нужно указать исходники