from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceSearchForm, InvoiceUpdateForm, EmailForm
from .models import *
from inventory.models import Inventory
from customer.models import Customer
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import EmailMessage
from django.conf import settings
import os

def home(request):
    title = 'Digital Invoice Management System'
    context = {
    "title": title,
    }
    return render(request, "home.html",context)

@login_required
def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:6]
    model_data=Inventory.objects.values_list('product_number','amount')
    data=[model for model in model_data.values()]
    cust_model_data = Customer.objects.values_list('customer_id','ph_no')
    customer_data=[model for model in cust_model_data.values()]

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/invoice/list_invoice')
    context = {
        "form": form,
        "title": "New Invoice",
        "total_invoices": total_invoices,
    "queryset": queryset,
        "data": data,
        "customer_data": customer_data,
    }
    return render(request, "entry.html", context)

@login_required
def list_invoice(request):
    title = 'List of Invoices'
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    context = {
    "title": title,
    "queryset": queryset,
    "form":form,
    }

    if request.method == 'POST':
           queryset = Invoice.objects.filter(invoice_number__icontains=form['invoice_number'].value(),name__name__icontains=form['name'].value())
    context = {
    "form": form,
    "title": title,
    "queryset": queryset,
    }
    if form['generate_invoice'].value() == True:
        instance = queryset
        data_file = instance
        num_of_invoices = len(queryset)
        message = str(num_of_invoices) + " invoices successfully generated."
        messages.success(request, message)

        def import_data(data_file):
            invoice_data = data_file
            for row in invoice_data:
                invoice_type = row.invoice_type
                invoice_number = row.invoice_number
                invoice_date = row.invoice_date
                name = row.name
                phone_number = row.phone_number

                line_one = row.line_one
                line_one_quantity = row.line_one_quantity
                line_one_unit_price = row.line_one_unit_price
                line_one_total_price = row.line_one_total_price

                line_two = row.line_two
                line_two_quantity = row.line_two_quantity
                line_two_unit_price = row.line_two_unit_price
                line_two_total_price = row.line_two_total_price

                line_three = row.line_three
                line_three_quantity = row.line_three_quantity
                line_three_unit_price = row.line_three_unit_price
                line_three_total_price = row.line_three_total_price

                line_four = row.line_four
                line_four_quantity = row.line_four_quantity
                line_four_unit_price = row.line_four_unit_price
                line_four_total_price = row.line_four_total_price

                line_five = row.line_five
                line_five_quantity = row.line_five_quantity
                line_five_unit_price = row.line_five_unit_price
                line_five_total_price = row.line_five_total_price

                line_six = row.line_six
                line_six_quantity = row.line_six_quantity
                line_six_unit_price = row.line_six_unit_price
                line_six_total_price = row.line_six_total_price

                line_seven = row.line_seven
                line_seven_quantity = row.line_seven_quantity
                line_seven_unit_price = row.line_seven_unit_price
                line_seven_total_price = row.line_seven_total_price

                line_eight = row.line_eight
                line_eight_quantity = row.line_eight_quantity
                line_eight_unit_price = row.line_eight_unit_price
                line_eight_total_price = row.line_eight_total_price

                line_nine = row.line_nine
                line_nine_quantity = row.line_nine_quantity
                line_nine_unit_price = row.line_nine_unit_price
                line_nine_total_price = row.line_nine_total_price

                line_ten = row.line_ten
                line_ten_quantity = row.line_ten_quantity
                line_ten_unit_price = row.line_ten_unit_price
                line_ten_total_price = row.line_ten_total_price

                total = row.total
                pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
                save_name = os.path.join(os.path.expanduser("~"), "Desktop/src/Invoices/", pdf_file_name)
                generate_invoice(str(name), str(invoice_number),
                    str(line_one), str(line_one_quantity), str(line_one_unit_price),
                    str(line_one_total_price), str(line_two), str(line_two_quantity),
                    str(line_two_unit_price), str(line_two_total_price), str(line_three),
                    str(line_three_quantity), str(line_three_unit_price),
                    str(line_three_total_price), str(line_four), str(line_four_quantity),
                    str(line_four_unit_price), str(line_four_total_price),  str(line_five),
                    str(line_five_quantity), str(line_five_unit_price),
                    str(line_five_total_price), str(line_six), str(line_six_quantity),
                    str(line_six_unit_price), str(line_six_total_price), str(line_seven),
                    str(line_seven_quantity), str(line_seven_unit_price),
                    str(line_seven_total_price), str(line_eight), str(line_eight_quantity),
                    str(line_eight_unit_price), str(line_eight_total_price), str(line_nine),
                    str(line_nine_quantity), str(line_nine_unit_price), str(line_nine_total_price),
                    str(line_ten), str(line_ten_quantity), str(line_ten_unit_price),
                    str(line_ten_total_price), str(total), str(phone_number), str(invoice_date),
                    str(invoice_type), save_name)

        def generate_invoice(name, invoice_number,
                line_one, line_one_quantity, line_one_unit_price, line_one_total_price,
                line_two, line_two_quantity, line_two_unit_price, line_two_total_price,
                line_three, line_three_quantity, line_three_unit_price, line_three_total_price,
                line_four, line_four_quantity, line_four_unit_price, line_four_total_price,
                line_five, line_five_quantity, line_five_unit_price, line_five_total_price,
                line_six, line_six_quantity, line_six_unit_price, line_six_total_price,
                line_seven, line_seven_quantity, line_seven_unit_price, line_seven_total_price,
                line_eight, line_eight_quantity, line_eight_unit_price, line_eight_total_price,
                line_nine, line_nine_quantity, line_nine_unit_price, line_nine_total_price,
                line_ten, line_ten_quantity, line_ten_unit_price, line_ten_total_price,
                total, phone_number, invoice_date, invoice_type, save_name):
            c = canvas.Canvas(save_name)

            # image of seal
            logo = 'logo.png'
            c.drawImage(logo, 50, 700, width=500, height=120)

            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(400, 660, str(invoice_type) + ':')
            c.setFont('Helvetica', 12, leading=None)
            invoice_number_string = str('0000' + invoice_number)
            c.drawCentredString(490, 660, invoice_number_string)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(409, 640, "Date:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(492, 641, invoice_date)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(397, 620, "Amount:")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(484, 622, 'Rs'+total)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(88, 660, "To:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 660, name)

            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(98, 640, "Phone:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(165, 640, phone_number)

            c.setFont('Helvetica-Bold', 14, leading=None)
            c.drawCentredString(310, 580, str(invoice_type))
            c.drawCentredString(110, 560, "Particulars:")
            c.drawCentredString(295, 510, "__________________________________________________________")
            c.drawCentredString(295, 480, "__________________________________________________________")
            c.drawCentredString(295, 450, "__________________________________________________________")
            c.drawCentredString(295, 420, "__________________________________________________________")
            c.drawCentredString(295, 390, "__________________________________________________________")
            c.drawCentredString(295, 360, "__________________________________________________________")
            c.drawCentredString(295, 330, "__________________________________________________________")
            c.drawCentredString(295, 300, "__________________________________________________________")
            c.drawCentredString(295, 270, "__________________________________________________________")
            c.drawCentredString(295, 240, "__________________________________________________________")
            c.drawCentredString(295, 210, "__________________________________________________________")

            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(110, 520, 'ITEMS')
            c.drawCentredString(220, 520, 'QUANTITY')
            c.drawCentredString(330, 520, 'UNIT PRICE')
            c.drawCentredString(450, 520, 'LINE TOTAL')


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(110, 490, line_one)
            c.drawCentredString(220, 490, line_one_quantity)
            c.drawCentredString(330, 490, line_one_unit_price)
            c.drawCentredString(450, 490, line_one_total_price)

            if line_two != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 460, line_two)
                c.drawCentredString(220, 460, line_two_quantity)
                c.drawCentredString(330, 460, line_two_unit_price)
                c.drawCentredString(450, 460, line_two_total_price)

            if line_three != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 430, line_three)
                c.drawCentredString(220, 430, line_three_quantity)
                c.drawCentredString(330, 430, line_three_unit_price)
                c.drawCentredString(450, 430, line_three_total_price)

            if line_four != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 400, line_four)
                c.drawCentredString(220, 400, line_four_quantity)
                c.drawCentredString(330, 400, line_four_unit_price)
                c.drawCentredString(450, 400, line_four_total_price)

            if line_five != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 370, line_five)
                c.drawCentredString(220, 370, line_five_quantity)
                c.drawCentredString(330, 370, line_five_unit_price)
                c.drawCentredString(450, 370, line_five_total_price)

            if line_six != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 340, line_six)
                c.drawCentredString(220, 340, line_six_quantity)
                c.drawCentredString(330, 340, line_six_unit_price)
                c.drawCentredString(450, 340, line_six_total_price)

            if line_seven != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 310, line_seven)
                c.drawCentredString(220, 310, line_seven_quantity)
                c.drawCentredString(330, 310, line_seven_unit_price)
                c.drawCentredString(450, 310, line_seven_total_price)

            if line_eight != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 280, line_eight)
                c.drawCentredString(220, 280, line_eight_quantity)
                c.drawCentredString(330, 280, line_eight_unit_price)
                c.drawCentredString(450, 280, line_eight_total_price)

            if line_nine != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 250, line_nine)
                c.drawCentredString(220, 250, line_nine_quantity)
                c.drawCentredString(330, 250, line_nine_unit_price)
                c.drawCentredString(450, 250, line_nine_total_price)

            if line_ten != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 220, line_ten)
                c.drawCentredString(220, 220, line_ten_quantity)
                c.drawCentredString(330, 220, line_ten_unit_price)
                c.drawCentredString(450, 220, line_ten_total_price)



            # TOTAL
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(400, 140, "TOTAL:")
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(484, 140, 'Rs'+total)


            # SIGN
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(150, 140, "Signed:__________________")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(170, 120, 'Manager')


            c.showPage()
            c.save()

        import_data(data_file)
    return render(request, "list_invoice.html", context)

@login_required
def update_invoice(request, pk):
    queryset = Invoice.objects.get(pk=pk)
    form = InvoiceUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/invoice/list_invoice')

    context = {
        'form':form
    }
    return render(request, 'entry.html', context)

@login_required
def delete_invoice(request, pk):
    queryset = Invoice.objects.get(pk=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/invoice/list_invoice')
    return render(request, 'delete_invoice.html')

# @login_required
class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'email.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        cust_model_data = Customer.objects.values_list('customer_id','ph_no', 'email')
        customer_data=[model for model in cust_model_data.values()]
        context = {
          "customer_data": customer_data,
          'email_form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            attach1 = request.FILES['attach']

            try:
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
                mail.attach(attach1.name, attach1.read(), attach1.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})
