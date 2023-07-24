from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



class Mailling_list(models.Model):
    FREQUENCY_CHOICES = (
        ('daily', 'ежедневно'),
        ('weekly', 'еженедельно'),
        ('monthly', 'ежемесячно'),

    )

    STATUS_CHOICES = (
        ('created', 'создана'),
        ('started', 'запущена'),
        ('completed', 'выполнена'),
    )

    mailing_time = models.TimeField(auto_now=True, verbose_name='время рассылки')
    frequency = models.CharField(max_length=15, choices=FREQUENCY_CHOICES, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='created', verbose_name='статус рассылки')
    client = models.ManyToManyField(Client, verbose_name='клиенты')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'



class Message(models.Model):

        subject = models.CharField(max_length=150, verbose_name='тема письма')
        body = models.TextField(verbose_name='тело письма')
        mailling_list = models.ForeignKey(Mailling_list, on_delete=models.CASCADE, verbose_name='настройки рассылки')


        def __str__(self):
            return f'{self.subject}'

        class Meta:
            verbose_name = 'Письмо'
            verbose_name_plural = 'Письма'



class MailingLogs(models.Model):

    STATUS_CHOICES = (
        ('success', 'успешно'),
        ('error', 'ошибка'),
    )

    attempt_time = models.DateField(auto_now=True, verbose_name='дата последней попытки')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='статус попытки')
    responce = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    mailling_list = models.ForeignKey(Mailling_list, on_delete=models.CASCADE, verbose_name='Письмо для рассылки')
