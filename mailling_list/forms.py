from django import forms

from mailling_list.models import Mailling_list, Message, Client


class MaillingForm(forms.ModelForm):
    class Meta:
        model = Mailling_list
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class ClientForm(forms.ModelForm):

   class Meta:
         model = Client
         fields = '__all__'


   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'