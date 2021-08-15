import graphene
from graphene_django.types import DjangoObjectType
from tasks.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        exclude = []


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    pass
