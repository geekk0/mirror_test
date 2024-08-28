from tortoise import fields, models


class Order(models.Model):
    id = fields.IntField(pk=True)
    apartment_number = fields.CharField(max_length=50)
    pet_name = fields.CharField(max_length=50)
    pet_breed = fields.CharField(max_length=50)
    walk_date = fields.DateField()
    walk_time = fields.TimeField()
    duration = fields.IntField()

    class Meta:
        table = 'orders'

