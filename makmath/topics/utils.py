from .models import *


class StatisticsManager:
    @staticmethod
    def get_statistics_for_topic(topic, user):
        if not (isinstance(topic, Topic) and isinstance(user, User)):
            return 0
        completed_tasks = TaskComplition.objects.filter(user=user)

        topic_completed_tasks = []

        for item in completed_tasks:

            if item.task.topic == topic:
                topic_completed_tasks.append(item)

        amount_of_topic_tasks = len(Task.objects.filter(topic=topic))
        return (len(topic_completed_tasks) * 100 // amount_of_topic_tasks
                if amount_of_topic_tasks
                else 0)

    @staticmethod
    def get_statistics_for_section(section, user):
        if not (isinstance(section, Section) and isinstance(user, User)):
            return 0
        topics = Topic.objects.filter(section=section)

        sum = 0

        for item in topics:
            sum += StatisticsManager.get_statistics_for_topic(item, user)

        return sum // len(topics) if topics else 0

    @staticmethod
    def get_statistics_in_html(user):
        stat_info = "<ul>"
        for item in Section.objects.filter(is_published=True):
            stat_info += (f"<li>{item.name} - "
                          f"{StatisticsManager.get_statistics_for_section(item, user)}%<ul>")

            for topic in Topic.objects.filter(section=item):
                stat_info += (f"<li>{topic.topic_name} - "
                              f"{StatisticsManager.get_statistics_for_topic(topic, user)}%</li>")

            stat_info += "</ul></li>"

        stat_info += "</ul>"

        return stat_info


ALPHABET = "abcdefghijklmnopwrstuwxyz_0123456789"


class Analizator():

    @staticmethod
    def is_in_alphabet(character, alphabet):
        return character.lower() in alphabet

    @staticmethod
    def is_correct_string(text, min_length, max_length):
        correction = True

        if min_length <= len(text) <= max_length:
            for character in text:
                if not Analizator.is_in_alphabet(character, ALPHABET):
                    correction = False
                    break
        else:
            correction = False

        return correction

    @staticmethod
    def find_index_of_value_in_array(value, array):
        result = None
        for i in range(len(array)):
            if array[i] == value:
                result = i

        return result

    @staticmethod
    def insertion_sort(data):
        for i in range(len(data)):
            j = i - 1
            key = data[i]
            while data[j] > key and j >= 0:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data
