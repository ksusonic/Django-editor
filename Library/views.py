# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from Scripts.django_summernote.widgets import SummernoteInplaceWidget
from Scripts.exploreropen.fileopen_box import fileopenbox
from Scripts.exploreropen.filesave_box import filesavebox


def load(form):
    input_file = fileopenbox(default="Документ из Django.html", filetypes=[["*.htm", "*.html", "HTML for Django"]], msg="Выберите файл")
    if input_file is not None:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        return form

    class SampleForm(forms.Form):
        desc2 = forms.CharField(
            label='',
            initial=text,  # инициализация текста здесь
            widget=SummernoteInplaceWidget(),
            required=True
        )

    form = SampleForm()
    return form


def save(form):
    if form.is_valid():
        passed = True
        input_file = filesavebox(default="Документ из Django.html",
                                 filetypes=[["*.htm", "*.html", "HTML for Django"]],
                                 msg="Сохранение файла")
        if input_file is not None:
            with open(input_file, 'w', encoding="utf-8") as text:
                data_form = dict(form.clean())["desc2"]
                text.write(data_form)


def index(request, data=None):
    class SampleForm(forms.Form):
        desc2 = forms.CharField(
            label='',
            initial=data,  # инициализация текста здесь
            widget=SummernoteInplaceWidget(),
            required=True
        )

    form = SampleForm()

    if request.method == "POST":
        form = SampleForm(request.POST)

        if request.POST.get('save') == 'Сохранить':
            save(form)
        if request.POST.get('open') == 'Открыть':
            form = load(form)

    return render(request, 'index.html', {'form': form})
