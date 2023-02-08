from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[('PYTHON','python'),('SQL','sql'),('DJANGO','django'),('WEB','web')]
class studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)