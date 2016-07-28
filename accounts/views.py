# -*- encodig: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from accounts.models import Perfil
from django.contrib import messages



class Dashboard(View):
	def get(self,request):
		template_name = 'accounts/perfil.html'
		messages.error(request,'Entramos a tu perfil exitosamente')
		return render(request,template_name)

