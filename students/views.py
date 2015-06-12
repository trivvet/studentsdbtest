# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Home page
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

# Group List
def groups_list(request):
	groups = (
		{'id': 1,
		'name_group': '1Б-04',
		'leader': 'Бацура Олександр'},
		{'id': 2,
		'name_group': '2Б-04',
		'leader': 'Козаченко Богдан'},
		{'id': 3,
		'name_group': 'БМ-04',
		'leader': 'Мелфой Люціус'})
	return render(request, 'students/groups_list.html', {'groups': groups})
	
def groups_add(request):	
	return HttpResponse('<h1>Add Group From</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)	
	

# Journal
def journal_list(request):
	return HttpResponse('<h1>Journal List</h1>')


# Create your views here.
