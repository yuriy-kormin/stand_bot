from django.core.exceptions import ValidationError
from django.db import models

from ..user.models import User


class Venue(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Timeslot(models.Model):
    WEEKDAY_NAMES = {
        0: ("Понедельник", "Пн"),
        1: ("Вторник", "Вт"),
        2: ("Среда", "Ср"),
        3: ("Четверг", "Чт"),
        4: ("Пятница", "Пт"),
        5: ("Суббота", "Сб"),
        6: ("Воскресенье", "Вс"),
    }

    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    dow = models.PositiveSmallIntegerField()  # 0 = Monday, 1
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.venue} - {self.get_dow(short=True)} ' \
               f'({self.start_time.strftime("%H:%M")}-' \
               f'{self.end_time.strftime("%H:%M")})'

    def get_dow(self, short=False):
        return self.WEEKDAY_NAMES[self.dow][1] \
            if short else self.WEEKDAY_NAMES[self.dow][0]

    def set_dow(self, dow=''):
        for i, names in self.WEEKDAY_NAMES.items():
            if any([x == dow for v in names for x in
                    (v, v.upper(), v.lower())]):
                self.dow = i
                self.save()
                return
        raise ValidationError(f'Invalid day of the week value: {dow}')


class Event(models.Model):
    start_date = models.DateField(auto_now_add=True)
    recurrent = models.BooleanField(default=False)
    timeslot = models.ForeignKey(to=Timeslot, on_delete=models.CASCADE)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE,)
    creator = models.ForeignKey(to=User, on_delete=models.SET_NULL,
                                related_name='created_by_events', null=True)
    active = models.BooleanField(default=True)
