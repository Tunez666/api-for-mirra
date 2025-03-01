from django.db import models

class Tablo(models.Model):
    id_u = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name="Уникальный идентификатор")
    name = models.TextField(null=True, blank=True, default=None, verbose_name="Наименование")
    oid_parameter = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="OID справочника с параметрами шкалы")
    id_parameter = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name="Группировочный код шкалы в параметрах")
    oid_interpretation = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="OID справочника с интерпретацией шкалы")
    id_interpretation = models.CharField(max_length=50, null=True, blank=True, default=None, verbose_name="Группировочный код шкалы в интерпретациях")
    point_scale = models.BooleanField(null=True, blank=True, default=None, verbose_name="Признак балльной шкалы")
    valid = models.IntegerField(null=True, blank=True, default=None, verbose_name="Валидация")
    valid_author = models.TextField(null=True, blank=True, default=None, verbose_name="Названия и авторы")
    valid_doi = models.CharField(max_length=100, null=True, blank=True, default=None, verbose_name="Идентификатор публикации")
    org = models.TextField(null=True, blank=True, default=None, verbose_name="Организацияz")

    def __str__(self):
        return self.name if self.name else "Без названия"
