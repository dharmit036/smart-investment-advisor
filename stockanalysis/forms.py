from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _

################################################################
####### This approach is default approach ######################
####### Here I used some another way to store html data to data-
# base ########################################################
################################################################

class user(forms.ModelForm):
    class Meta(object):
        model=userdata
        fields=['your_name','username','email_id','birth_date','job_type','phone_no','income','plans','schemes','ex_returns','problems_faced','saving_ratio','span']
        widgets={
                'your_name':forms.TextInput(
                     attrs={
                      'class':'form-control',
                      'cols': 5,
                      'rows': 8,
                    }),        

                 'username':forms.TextInput(
                    attrs={
                     'class':'form-control'}),
                 'email_id':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'birth_date':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'job_type':forms.TextInput( 
                    attrs={ 
                       'class':'form-control' 
                    }),
                 'phone_no':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                    'income':forms.TextInput(
                     attrs={
                      'class':'form-control'
                    }),
                 'plans':forms.TextInput(
                    attrs={
                     'class':'form-control'}),
                 'schemes':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'ex_returns':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                 'problems_faced':forms.TextInput( 
                    attrs={ 
                       'class':'form-control' 
                    }),
                 'saving_ratio':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),
                  'span':forms.TextInput(
                      attrs={ 
                       'class':'form-control' 
                    }),                                 
               }
