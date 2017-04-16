# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import socket
import netifaces as net
import nmap
import paramiko
from .models import Host

def home(request):
	return render(request,'home.html')

def scan(request):
	inet_addrr = net.ifaddresses('wlp6s0')[2][0]['addr']
	print inet_addrr
	nm = nmap.PortScanner()
	hosts = inet_addrr+'/24'
	nm.scan(hosts=hosts, arguments='-p 22 --open')
	hosts = nm.all_hosts()
	#hosts  = ['1000','2020000']
	for host in hosts:
		new_host = Host.objects.create(ip=host)
		new_host.save()
	return render(request,'scan.html',{'hosts':hosts})

def ifconfig(request):
	hosts = Host.objects.all()
	for host in hosts:
		if host.accessed == 0:
			host.command = 'ifconfig'
			try:
				client = paramiko.SSHClient()	
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				client.connect(host.ip, username='student', password='pass@123',allow_agent=False,look_for_keys=False)
				stdin, stdout, stderr = client.exec_command('ifconfig')
				stdout = stdout.read()
				stderr = stderr.read()
				print stdout
				print stderr
				print type(stderr)
				print type(stdout)
				if stderr:
					print('ERROR')
					host.status = stderr
					host.save()
				else:
					host.status = stdout
					host.save()
				client.close()
			except paramiko.AuthenticationException:
				host.status = 'Wrong Credentials'
				host.save()
			host.accessed = 1;
			host.save()

	return HttpResponseRedirect('/result')

def update(request):
	hosts = Host.objects.all()
	for host in hosts:
		if host.accessed == 0:
			host.command = 'echo \'pass@123\' | sudo -S apt-get update'
			try:
				client = paramiko.SSHClient()	
				client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				client.connect(host.ip, username='student', password='pass@123',allow_agent=False,look_for_keys=False)
				stdin, stdout, stderr = client.exec_command('echo \'pass@123\' | sudo -S apt-get update')
				stdout = stdout.read()
				stderr = stderr.read()
				print stdout
				if len(stdout)==0:
					print('ERROR')
					print stderr
					host.status = 'ERROR ERROR ERROR ERROR' + '\n' + stderr
					host.save()
				else:
					print stdout
					host.status = stdout
					host.save()
				client.close()
				
			except paramiko.AuthenticationException:
				host.status = 'Wrong Credentials'
				host.save()
			host.accessed=1
			host.save()
	return HttpResponseRedirect('/result')

def result(request):
	hosts = Host.objects.all()
	return render(request,'result.html',{'hosts':hosts})






# Create your views here.