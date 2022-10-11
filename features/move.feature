Feature: Object move

  # positive
  Scenario: Тело меняет положение в пространстве
    Given  Тело находится в точке (12, 5) пространства
    And имеет скорость (-5, 2)
    When  выполняется операция MoveCommand
    Then  новое положение тела в пространстве определяется точкой (7, 7)

    # негативный
    Scenario: Невозможно изменить положение в пространстве тела, у которого нельзя прочитать свойство Position
    Given Тело находится в точке (12, 5) пространства
    When невозможно определить мгновенную скорость
    Then операция MoveCommand прерывается выбросом исключения ValueError

    # негативный
    Scenario: Невозможно изменить положение в пространстве тела, у которого нельзя прочитать значения свойство Velocity
    Given Тело, у которого невозможно определить положение в пространстве
    And имеет скорость (-5, 2)
    Then операция MoveCommand прерывается выбросом исключения ValueError

    # негативный
    Scenario: Невозможно изменить положение в пространстве тела, у которого нельзя изменить значения свойство Position
    Given Тело находится в точке (12, 5) пространства
    And имеет скорость (-5, 2)
    And невозможно установить новое положение тела в пространстве
    Then операция MoveCommand прерывается выбросом исключения ValueError