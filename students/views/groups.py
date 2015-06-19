# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
	groups = (
		{'id': 1,
		'name_group': '1Б-04',
		'leader': {'id': 1, 'name': u'Бацура Олександр'}},
		{'id': 2,
		'name_group': '2Б-04',
		'leader': {'id': 2, 'name': u'Козаченко Богдан'}},
		{'id': 3,
		'name_group': 'БМ-04',
		'leader': {'id': 3, 'name': u'Мелфой Люціус'}})
	return render(request, 'students/groups_list.html', {'groups': groups})
	
def groups_add(request):	
	return HttpResponse('<h1>Add Group From</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)	
