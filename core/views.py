from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))


def soma(request, v1, v2):
    return HttpResponse('<h1>resultado da soma de {} + {} = {}</h1>'.format(v1, v2, v1 + v2))


def subtracao(request, v1, v2):
    return HttpResponse('<h1>resultado da subtração de {} - {} = {}</h1>'.format(v1, v2, v1 - v2))


def multiplicacao(request, v1, v2):
    return HttpResponse('<h1>resultado da multiplicação de {} x {} = {}</h1>'.format(v1, v2, v1 * v2))


def divisao(request, v1, v2):
    return HttpResponse('<h1>resultado da divisão de {} / {} = {}</h1>'.format(v1, v2, v1 / v2))
