import factory
from faker import Faker
from users.client.client_controller import ClientFactory
from users.expert.expert_controller import ExpertFactory

from app.question.question_models import Question

fake = Faker()


class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    id = factory.Sequence(lambda n: n)
    question_text = factory.LazyFunction(fake.text)
    answer = factory.LazyFunction(fake.text)
    question_date = factory.LazyFunction(fake.date_time_this_month)
    answer_date = factory.LazyFunction(fake.date_time_this_month)
    client = factory.SubFactory(ClientFactory)
    expert_id = factory.SubFactory(ExpertFactory)
