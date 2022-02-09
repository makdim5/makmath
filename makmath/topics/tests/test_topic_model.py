import pytest

from topics.models import Topic


@pytest.fixture()
def get_topic():
    return Topic.objects.get(id=2)


@pytest.mark.django_db
def test_topic_name_label(get_topic):
    assert get_topic.topic_name == 'Тема 1. Введение в математический анализ.'


@pytest.mark.django_db
def test_topic_name_max_length(get_topic):
    max_length = get_topic._meta.get_field('topic_name').max_length
    assert max_length == 255


@pytest.mark.django_db
def test_topic_name_verbose_name(get_topic):
    verbose_name = get_topic._meta.get_field('topic_name').verbose_name
    assert verbose_name == "Название темы"


@pytest.mark.django_db
def test_topic_name_verbose_name(get_topic):
    verbose_name = get_topic._meta.get_field('content').verbose_name
    assert verbose_name == "Текст лекции"


@pytest.mark.django_db
def test_topic_is_published_default(get_topic):
    default = get_topic._meta.get_field('is_published').default
    assert default == True


@pytest.mark.django_db
def test_topic_section_verbose_name(get_topic):
    verbose_name = get_topic._meta.get_field('section').verbose_name
    assert verbose_name == "Выбор раздела"


@pytest.mark.django_db
def test_get_absolute_url(get_topic):
    assert get_topic.get_absolute_url() == '/topics/topc1/'
