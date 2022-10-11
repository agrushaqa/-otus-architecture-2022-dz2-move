from behave import given, then, when
from src.move import Move


@given('Тело находится в точке ({x}, {y}) пространства')
def given_the_body_located_at_the_point(context, x, y):
    context.mock.set_position([int(x), int(y)])


@given('Тело, у которого невозможно определить положение в пространстве')
def given_the_body_which_is_unable_to_located(context):
    context.exception = None
    try:
        raise ValueError('невозможно определить положение в пространстве')
    except Exception as e:
        context.exception = e


@given('имеет скорость ({x}, {y})')
def when_the_body_has_velocity(context, x, y):
    context.mock.get_velocity.configure_mock(return_value=[int(x), int(y)])


@when('выполняется операция MoveCommand')
def when_the_body_moves(context):
    Move(context.mock).execute()


@given('невозможно установить новое положение тела в пространстве')
def it_is_impossible_to_change_position_of_the_body(context):
    context.exception = None
    try:
        raise ValueError(
            'невозможно установить новое положение тела в пространстве'
        )
    except Exception as e:
        context.exception = e


@then('новое положение тела в пространстве определяется точкой ({x}, {y})')
def then_the_body_should_be_moved_to_point(context, x, y):
    assert context.mock.get_position() == [int(x), int(y)]


@when('невозможно определить мгновенную скорость')
def when_it_it_unable_to_get_velocity_value(context):
    context.exception = None
    try:
        raise ValueError('невозможно определить мгновенную скорость')
    except Exception as e:
        context.exception = e


@then('операция MoveCommand прерывается выбросом исключения {exception_type}')
def then_thee_movement_of_the_body_is_not_possible(context, exception_type):
    assert isinstance(context.exception, eval(exception_type)),\
        "Invalid exception - expected " + exception_type
