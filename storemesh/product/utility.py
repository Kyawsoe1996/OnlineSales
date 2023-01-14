from django.forms import BaseForm
class BaseFormInherit(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})