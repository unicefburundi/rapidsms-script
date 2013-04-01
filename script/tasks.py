'''
Created on Mar 31, 2013

@author: asseym
'''
from celery.task import task
from django.conf import settings
from django.core.management import call_command

@task(track_started=True)
def check_script_progress_task():
    """
    Move people along in the script
    """
    call_command('check_script_progress', e=8, l=24)