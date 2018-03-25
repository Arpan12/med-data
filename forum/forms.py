from django import forms


class PostArea(forms.Form):
	tag=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeHolder':"enter catergories"}))
	new_post=forms.CharField(widget=forms.TextInput(attrs={'placeHolder':"post a Question"}),max_length=200)





