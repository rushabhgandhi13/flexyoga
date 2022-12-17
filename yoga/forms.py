from django import forms
from django.forms import DateInput
from yoga.models import Suscription

class SuscriptionForm(forms.ModelForm):
    
    class Meta:
        model = Suscription
        fields = ['age', 'batch', 'start_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
 
        # data from the form is fetched using super function
        super(SuscriptionForm, self).clean()
         
        # extract the username and text field from the data
        sage = self.cleaned_data.get('age')
        
 
        # conditions to be met for the username length
        if sage < 18 or sage>65:
            self._errors['age'] = self.error_class([
                'Age should be between 18 to 65 years'])
       
 
        # return any errors if found
        return self.cleaned_data

    

    # class Meta:
    #     model = User
    #     fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']