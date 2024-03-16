from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


STATUS = [
    ('Не выполнено', 'Не выполнено'),
    ('Выполнено', 'Выполнено'),
    ('В процессе', 'В процессе')
]


class Staff(models.Model):
    staff_fullname = models.CharField('ФИО', max_length=200)
    staff_phone_number = models.CharField('Тел. номер', max_length=13)
    staff_category = models.ForeignKey(Group, verbose_name='Категория', blank=True, null=True,
                                          on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.staff_fullname}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Material(models.Model):
    material_name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.material_name

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Breaking(models.Model):
    breaking_full_name = models.CharField('ФИО',
                                          max_length=70,
                                          validators=[(RegexValidator(
                                              r'[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][а-яёa-z]{2,25}\s[А-ЯЁёA-Z][А-Яа-яЁёA-Za-z]{2,25}\s?'))],
                                          )
    breaking_email = models.EmailField('Электронная почта',max_length=254,
                                       blank=True, null=True)
    breaking_date = models.DateField('Дата', default=timezone.now())
    breaking_room = models.IntegerField('Кабинет', validators=[MinValueValidator(101), MaxValueValidator(500)])
    breaking_category = models.ForeignKey(Group, verbose_name='Категория', null=True,
                                          on_delete=models.SET_NULL)
    breaking_description = models.TextField('Описание', max_length=1000, null=True, blank=True)
    breaking_status = models.CharField('Статус', max_length=100, choices=STATUS, default='Не выполнено')
    breaking_worker_fullname = models.ForeignKey(Staff, verbose_name='Ответсвенный', blank=True, null=True,
                                                 on_delete=models.SET_NULL)
    breaking_number = models.CharField('Номер', max_length=100)

    def save(self, *args, **kwargs):
        self.breaking_number = f"№{self.breaking_date.strftime('%d%m%Y')}.{self.breaking_room}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.breaking_number};"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class BreakingMaterial(models.Model):
    breaking = models.ForeignKey(Breaking, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField('Количество', decimal_places=1,  max_digits=4, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.material} ({self.quantity})"
    class Meta:
        verbose_name = 'Привязанный материал'
        verbose_name_plural = 'Привязанные материалы'
