# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
	students = (
		{'id': 1,
		'first_name': u'Вейдер',
		'second_name': u'Дарт',
		'ticket': 34,
		'image': 'img/SOS.JPG'},
		{'id': 2,
		'first_name': u'Мелфой',
		'second_name': u'Люціус',
		'ticket': 66,
		'image': 'img/Mich.JPG'},
		{'id': 3,
		'first_name': u'Бендер',
		'second_name': u'Остап',
		'ticket': 21,
		'image': 'img/Kir.JPG'})
	groups = (
		{'name_group': '1Б-04',
		'leader': 'Бацура Олександр',
		'ticket': 41},
		{'name_group': '2Б-04',
		'leader': 'Козаченко Богдан',
		'ticket': 85},
		{'name_group': 'БМ-04',
		'leader': 'Мелфой Люціус',
		'ticket': 66})
	return render(request, 'students/students_list.html', {'students': students, 'groups': groups})
	
def students_add(request):
	return HttpResponse('<h1>Add Student</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
	
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
