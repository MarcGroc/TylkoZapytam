import random

from faker import Faker

fake = Faker()


def populate_model(model_class):
    """
    Function that takes a model class as a parameter and populates all fields in the model with random data.
    """
    model_instance = model_class()
    for field in model_class._meta.get_fields():
        if field.name == "id":
            continue
        if field.get_internal_type() in ('CharField', 'TextField'):
            setattr(model_instance, field.name, fake.text())
        elif field.get_internal_type() in ('IntegerField', 'BigIntegerField', 'PositiveIntegerField'):
            setattr(model_instance, field.name, random.randint(0, 100))
        elif field.get_internal_type() == 'BooleanField':
            setattr(model_instance, field.name, random.choice([True, False]))
        elif field.get_internal_type() == 'DateField':
            setattr(model_instance, field.name, fake.date_between(start_date='-30y', end_date='today'))
        elif field.get_internal_type() == 'DateTimeField':
            setattr(model_instance, field.name, fake.date_time_this_decade())
        elif field.get_internal_type() in ('DecimalField', 'FloatField'):
            setattr(model_instance, field.name, fake.random_number())
        elif field.get_internal_type() == 'EmailField':
            setattr(model_instance, field.name, fake.email())
        elif field.get_internal_type() == 'URLField':
            setattr(model_instance, field.name, fake.url())
        elif field.get_internal_type() == 'IPAddressField':
            setattr(model_instance, field.name, fake.ipv4_public())
        elif field.get_internal_type() == 'GenericIPAddressField':
            setattr(model_instance, field.name, fake.ipv4())
        elif field.get_internal_type() == 'FileField':
            setattr(model_instance, field.name, fake.file_path())
        elif field.get_internal_type() == 'ImageField':
            setattr(model_instance, field.name, fake.image_url())
        elif field.get_internal_type() == 'SlugField':
            setattr(model_instance, field.name, fake.slug())
        elif field.get_internal_type() == 'ForeignKey':
            setattr(model_instance, field.name, random.choice(field.related_model.objects.all()))
        elif field.get_internal_type() == 'ManyToManyField':
            setattr(model_instance, field.name,
                    random.sample(list(field.related_model.objects.all()), random.randint(0, 5)))
        else:
            print(field.get_internal_type())
    return model_instance
