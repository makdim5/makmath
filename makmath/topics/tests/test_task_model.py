import pytest
from topics.models import Task


@pytest.fixture()
def get_task():
    return Task.objects.filter(id=2)[0]


@pytest.mark.django_db
def test_task_info_max_length(get_task):
    max_length = get_task._meta.get_field('task_info').max_length
    assert max_length == 255


@pytest.mark.django_db
def test_task_info_verbose_name(get_task):
    verbose_name = get_task._meta.get_field('task_info').verbose_name
    assert verbose_name == "Задание"


@pytest.mark.django_db
def test_correct_answer_verbose_name(get_task):
    verbose_name = get_task._meta.get_field('correct_answer').verbose_name
    assert verbose_name == "Правильный ответ"


@pytest.mark.django_db
def test_correct_answer_max_length(get_task):
    max_length = get_task._meta.get_field('correct_answer').max_length
    assert max_length == 5


@pytest.mark.django_db
def test_task_topic_verbose_name(get_task):
    verbose_name = get_task._meta.get_field('topic').verbose_name
    assert verbose_name == "Выбор темы"


# check_task testing
@pytest.fixture()
def get_simple_task():
    task = Task()
    task.correct_answer = "3"
    return task


@pytest.mark.parametrize("answer, expected",
                         [('3', True),
                          ([0], False),
                          ("dvvdvd", False)])
def test_check_task(answer, expected, get_simple_task):
    assert get_simple_task.check_task(answer) == expected
