import pytest
from topics.models import Section


@pytest.fixture()
def get_section():
    return Section.objects.filter(id=1)[0]


@pytest.mark.django_db
def test_section_name_max_length(get_section):
    max_length = get_section._meta.get_field('name').max_length
    assert max_length == 100


@pytest.mark.django_db
def test_section_name_verbose_name(get_section):
    verbose_name = get_section._meta.get_field('name').verbose_name
    assert verbose_name == "Название раздела"


@pytest.mark.django_db
def test_image_link_verbose_name(get_section):
    verbose_name = get_section._meta.get_field('image_link').verbose_name
    assert verbose_name == "URL картинки"


@pytest.mark.django_db
def test_description_max_length(get_section):
    max_length = get_section._meta.get_field('description').max_length
    assert max_length == 100


@pytest.mark.django_db
def test_topic_is_published_default(get_section):
    default = get_section._meta.get_field('is_published').default
    assert default is True


@pytest.mark.django_db
def test_get_absolute_url(get_section):
    assert get_section.get_absolute_url() == '/section/diff_ovf/'
