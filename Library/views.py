# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render
from Scripts.django_summernote.widgets import SummernoteInplaceWidget
from Scripts.exploreropen.fileopen_box import fileopenbox
from Scripts.exploreropen.filesave_box import filesavebox


def load(request):
    input_file = fileopenbox(filetypes=[["*.htm", "*.html", "HTML for Django"]], msg="Выберите файл")
    if input_file is not None:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = None

    return index(request, text)


def index(request, data=None):
    class SampleForm(forms.Form):
        desc2 = forms.CharField(
            label='',
            initial=data,  # инициализация текста здесь
            widget=SummernoteInplaceWidget(),
            required=True
        )

        def clean(self):
            data = super().clean()
            return data

    form = SampleForm()

    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            passed = True
            input_file = filesavebox(default="Документ из Django.html",
                                     filetypes=[["*.htm", "*.html", "HTML for Django"]],
                                     msg="Сохранение файла")
            if input_file is not None:
                with open(input_file, 'w', encoding="utf-8") as text:
                    data_form = dict(form.clean())["desc2"]
                    text.write(data_form)

    return render(request, 'index.html', {
        'form': form,
    })
