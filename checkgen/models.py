from django.db import models
from django.contrib.postgres.fields import JSONField


class Printer(models.Model):
    name = models.CharField(verbose_name="название принтера", max_length=64)
    api_key = models.CharField(verbose_name="ключ доступа к API", max_length=64)
    CHECK_TYPES = (
        (1, 'kitchen'),
        (2, 'client')
    )
    check_type = models.IntegerField(verbose_name="тип чека которые печатает принтер", choices=CHECK_TYPES)
    point_id = models.IntegerField(verbose_name="точка к которой привязан принтер")

    def __str__(self):
        return self.name


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, verbose_name="принтер", on_delete=models.CASCADE)
    type = models.CharField(max_length=64, verbose_name="тип чека", choices=Printer.CHECK_TYPES)
    order = JSONField(verbose_name="информация о заказе")
    STATUS_TYPE = (
        (1, 'new'),
        (2, 'rendered'),
        (3, 'printed')
                   )
    status = models.IntegerField(verbose_name="статус чека", choices=STATUS_TYPE)
    pdf_file = models.FileField(verbose_name="ссылка на созданный PDF-файл", upload_to='pdf/')

    def __str__(self):
        return self.printer_id

