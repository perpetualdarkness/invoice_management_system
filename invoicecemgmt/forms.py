from django import forms
from .models import Invoice
from inventory.models import Inventory
from customer.models import Customer
from django.forms import TextInput, DateInput
from crispy_forms.helper import FormHelper

class InvoiceForm(forms.ModelForm):

	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
				'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
				'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
				'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
				'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
								'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
				'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
				'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
				'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
				'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
				'total', 'paid', 'invoice_type'
				]

		widgets = {
            'line_one_quantity': TextInput(),
			'line_two_quantity': TextInput(),
			'line_three_quantity': TextInput(),
			'line_four_quantity': TextInput(),
			'line_five_quantity': TextInput(),
			'line_six_quantity': TextInput(),
			'line_seven_quantity': TextInput(),
			'line_eight_quantity': TextInput(),
			'line_nine_quantity': TextInput(),
			'line_ten_quantity': TextInput(),
			'line_one_unit_price': TextInput(),
			'line_two_unit_price': TextInput(),
			'line_three_unit_price': TextInput(),
			'line_four_unit_price': TextInput(),
			'line_five_unit_price': TextInput(),
			'line_six_unit_price': TextInput(),
			'line_seven_unit_price': TextInput(),
			'line_eight_unit_price': TextInput(),
			'line_nine_unit_price': TextInput(),
			'line_ten_unit_price': TextInput(),
			'invoice_date': DateInput(attrs={'type': 'date'}),
        }

	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
		return invoice_number


	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

	def clean_line_one(self):
		line_one = self.cleaned_data.get('line_one')
		if not line_one:
			raise forms.ValidationError('This field is required')
		return line_one

	def clean_line_one_quantity(self):
		line_one_quantity = self.cleaned_data.get('line_one_quantity')
		if not line_one_quantity:
			raise forms.ValidationError('This field is required')
		return line_one_quantity


class InvoiceSearchForm(forms.Form):
	generate_invoice = forms.BooleanField(required=False)
	invoice_number = forms.CharField(max_length=100, required=False)
	name = forms.CharField(max_length=100, required=False)

class InvoiceUpdateForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
				'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
				'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
				'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
				'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',
				'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
				'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
				'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
				'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
				'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
				'total', 'paid', 'invoice_type'
				]

		widgets = {
			'invoice_date': DateInput(attrs={'type': 'date'}),
		}

	def clean_invoice_number(self):
		invoice_number = self.cleaned_data.get('invoice_number')
		if not invoice_number:
			raise forms.ValidationError('This field is required')
		return invoice_number


	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

	def clean_line_one(self):
		line_one = self.cleaned_data.get('line_one')
		if not line_one:
			raise forms.ValidationError('This field is required')
		return line_one

	def clean_line_one_quantity(self):
		line_one_quantity = self.cleaned_data.get('line_one_quantity')
		if not line_one_quantity:
			raise forms.ValidationError('This field is required')
		return line_one_quantity

class EmailForm(forms.Form):
	customer = forms.CharField(widget=forms.Select)
	email = forms.CharField(max_length=100)
	subject = forms.CharField(max_length=100)
	attach = forms.FileField()
	message = forms.CharField(widget = forms.Textarea)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['customer'].widget.choices = [(i.name, i.name) for i in Customer.objects.all()]
