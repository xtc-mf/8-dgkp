from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Sum, Count
from django.db.models.functions import Coalesce
from django.shortcuts import render, get_object_or_404, redirect
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from .forms import *
from .models import Breaking
from django.http import HttpResponse
from urllib.parse import unquote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.db.models import DecimalField
from io import BytesIO
from reportlab.pdfgen import canvas


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


def send_email(email_subject, email_message, email_recipient):
    with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
    ) as connection:
        email_from = settings.EMAIL_HOST_USER
        EmailMessage(email_subject, email_message, email_from, email_recipient, connection=connection).send()


def index(request):
    notification = None
    form_errors = []

    if request.method == "POST":
        form = Breaking_Form(request.POST)
        if form.is_valid():
            try:
                saved_form = form.save()
                email_subject = f'Уважаемый(ая) {saved_form.breaking_full_name}, Ваша заявка поступила в обработку.'
                email_message = 'Указанные данные:\n\n'
                email_message += (f'Отправитель: {saved_form.breaking_full_name};\n'
                                  f'Дата заявки: {saved_form.breaking_date};\n'
                                  f'Кабинет: {saved_form.breaking_room};\n'
                                  f'Категория: {saved_form.breaking_category};\n'
                                  f'Описание: {saved_form.breaking_description};\n'
                                  f'\n\nС уважением 8DGKP Manager!')
                email_recipient = [saved_form.breaking_email]
                send_email(email_subject, email_message, email_recipient)
                messages.success(request, 'Заявка успешно оставлена!')
                form = Breaking_Form()
            except Exception as e:
                messages.error(request, f'Ошибка сохранения формы или отправки электронной почты: {e}')
        else:
            form_errors = [f'{form.fields[field].label}: {error}' for field, error in form.errors.items()]
    else:
        form = Breaking_Form()

    context = {
        'notification': notification,
        'form': form,
        'form_errors': form_errors,
    }
    return render(request, 'index.html', context)


@login_required
def journal(request):
    user = request.user
    user_group_name = None

    selected_category = request.GET.get('category', '')
    selected_status = request.GET.get('status', '')
    search_query = request.GET.get('search', '')

    breaking_materials = BreakingMaterial.objects.select_related('breaking', 'material').all()
    breaking_list = Breaking.objects.all().order_by('breaking_date')

    if user.is_authenticated:
        user_groups = user.groups.all()
        if user_groups.exists():
            user_group = user_groups.first()
            user_group_name = user_group.name

    if user_group_name:
        breaking_list = breaking_list.filter(breaking_category__name=user_group_name)

    if selected_category:
        selected_category = unquote(selected_category.replace('+', ' '))
        breaking_list = breaking_list.filter(breaking_category__name__iexact=selected_category)

    if selected_status:
        breaking_list = breaking_list.filter(breaking_status=selected_status)

    if search_query:
        breaking_list = breaking_list.filter(
            Q(breaking_full_name__icontains=search_query) |
            Q(breaking_date__icontains=search_query) |
            Q(breaking_room__icontains=search_query) |
            Q(breaking_description__icontains=search_query) |
            Q(breaking_status__icontains=search_query)
        )

    categories = set(b.breaking_category.name for b in breaking_list if b.breaking_category)
    statuses = set(b.breaking_status for b in breaking_list)

    page = request.GET.get('page', 1)
    paginator = Paginator(breaking_list, 8)

    try:
        breaking_list = paginator.page(page)
    except PageNotAnInteger:
        breaking_list = paginator.page(1)
    except EmptyPage:
        breaking_list = paginator.page(paginator.num_pages)

    context = {
        'breaking_list': breaking_list,
        'breaking_materials': breaking_materials,
        'categories': categories,
        'statuses': statuses,
        'selected_category': selected_category,
        'selected_status': selected_status,
    }
    return render(request, 'journal.html', context)


@login_required
def edit_breaking(request, breaking_id):
    breaking = get_object_or_404(Breaking, id=breaking_id)
    if request.method == "POST":
        form = Breaking_Form_Admin(request.POST, instance=breaking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно обновлена!')
            email_breaking_full_name = form.cleaned_data['breaking_full_name']
            email_breaking_date = form.cleaned_data['breaking_date']
            email_breaking_room = form.cleaned_data['breaking_room']
            email_breaking_category = form.cleaned_data['breaking_category']
            email_breaking_description = form.cleaned_data['breaking_description']
            email_breaking_recipient = form.cleaned_data['breaking_email']
            if 'send_email_button' in request.POST:
                email_subject = f'Уважаемый(ая) {email_breaking_full_name}, Заявка {breaking.breaking_number} выполнена!'
                email_message = 'Указанные данные:\n\n'
                email_message += (f'Отправитель: {email_breaking_full_name};\n'
                                  f'Дата заявки: {email_breaking_date};\n'
                                  f'Кабинет: {email_breaking_room};\n'
                                  f'Категория: {email_breaking_category};\n'
                                  f'Описание: {email_breaking_description};\n'
                                  f'\n\nСпасибо за вашу помощь! =)\n'
                                  f'С уважением 8DGKP Manager!')
                email_recipient = [email_breaking_recipient]
                try:
                    send_email(email_subject, email_message, email_recipient)
                    messages.success(request, 'Email sent successfully!')
                except Exception as e:
                    messages.error(request, f'Error sending email: {e}')
            return redirect('journal')
        else:
            messages.error(request, 'Ошибка при обновлении заявки!')
    else:
        form = Breaking_Form_Admin(instance=breaking)

    context = {
        'form': form,
        'breaking': breaking
    }
    return render(request, 'edit.html', context)


@login_required
def add_material_breaking(request, breaking_id):
    breaking = get_object_or_404(Breaking, id=breaking_id)
    materials = BreakingMaterial.objects.filter(breaking_id=breaking_id)

    if request.method == "POST":
        form = BreakingMaterial_Form(breaking_id, request.POST)
        if form.is_valid():
            material_breaking = form.save(commit=False)
            material_breaking.breaking_id = breaking_id
            material_breaking.save()
            messages.success(request, 'Материал успешно добавлен!')
            return redirect('add_material_breaking', breaking_id=breaking_id)
        else:
            messages.error(request, 'Ошибка при добавлении материала!')
    else:
        form = BreakingMaterial_Form(breaking_id=breaking_id)

    if request.method == "POST":
        mat_form = Material_Form(request.POST)
        if mat_form.is_valid():
            material = mat_form.save(commit=False)
            material.save()
            messages.success(request, 'Добавлен новый материал!')
            mat_form = Material_Form()
        else:
            messages.error(request, 'Ошибка добавления материала!')
    else:
        mat_form = Material_Form()

    context = {
        'form': form,
        'materials': materials,
        'breaking': breaking,
        'mat_form': mat_form
    }
    return render(request, 'material-breaking.html', context)


@login_required
def delete_material(request, breaking_id, material_id):
    material = get_object_or_404(BreakingMaterial, id=material_id)

    if request.method == 'POST':
        material.delete()
        messages.success(request, 'Материал успешно удален!')

    return redirect('add_material_breaking', breaking_id=breaking_id)


@login_required
def staff(request):
    categories = Group.objects.all()
    if request.method == "POST":
        form = Staff_Form(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)
            staff.save()
            messages.success(request, 'Добавлен новый персонал!')
            form = Staff_Form()
        else:
            messages.error(request, 'Ошибка добавления материала!')
    else:
        form = Staff_Form()
    staff_list = Staff.objects.all()
    search_query = request.GET.get('search', '')
    selected_category = request.GET.get('category', '')

    if search_query:
        staff_list = staff_list.filter(
            Q(staff_fullname__icontains=search_query) |
            Q(staff_phone_number__icontains=search_query)
        )

    if selected_category:
        selected_category = unquote(selected_category.replace('+', ' '))
        staff_list = staff_list.filter(staff_category__name__iexact=selected_category)

    page = request.GET.get('page', 1)
    paginator = Paginator(staff_list, 7)

    try:
        staff_list = paginator.page(page)
    except PageNotAnInteger:
        staff_list = paginator.page(1)
    except EmptyPage:
        staff_list = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'staff_list': staff_list,
        'form': form
    }
    return render(request, 'staff.html', context)


@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)

    if request.method == 'POST':
        staff.delete()
        messages.success(request, 'Работник успешно удален!')

    return redirect('staff')


@login_required
def edit_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == "POST":
        form = Staff_Form(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно обновлена!')
            return redirect('staff')
        else:
            messages.error(request, 'Ошибка при обновлении заявки!')
    else:
        form = Staff_Form(instance=staff)

    context = {
        'form': form,
        'staff': staff
    }
    return render(request, 'edit.html', context)


@login_required
def report(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    breaking_list = Breaking.objects.filter(breaking_date__range=[start_date, end_date])
    staff_list = Staff.objects.all()
    material_list = BreakingMaterial.objects.all()
    breaking_materials = BreakingMaterial.objects.select_related('breaking', 'material').all()
    breaking_statistics = breaking_list.values('breaking_status').annotate(count=Count('id'))

    material_aggregated = BreakingMaterial.objects.filter(breaking__breaking_date__range=[start_date, end_date]).values(
        'material__material_name').annotate(
        total_quantity=Coalesce(Sum('quantity', output_field=DecimalField()), 0, output_field=DecimalField()),
        breaking_numbers=Count('breaking', distinct=True)
    )

    context = {
        'breaking_list': breaking_list,
        'staff_list': staff_list,
        'material_list': material_list,
        'start_date': start_date,
        'end_date': end_date,
        'breaking_statistics': breaking_statistics,
        'material_aggregated': material_aggregated,
        'breaking_materials': breaking_materials,

    }

    if request.method == 'POST' and 'export_pdf' in request.POST:
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)

        # Register Unicode font with UTF-8 encoding
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        pdf.setFont("Verdana", 14)

        # Title
        pdf.setTitle("ОТЧЕТ")
        pdf.drawCentredString(300, 750, "ОТЧЕТ")
        pdf.drawCentredString(300, 730, f"За период: {start_date} - {end_date}")

        # Set the font for the tables
        pdf.setFont("Verdana", 10)

        # Breaking List
        pdf.drawString(50, 710, "Заявки:")
        y_position = 690
        for breaking in breaking_list:
            pdf.drawString(50, y_position,
                           f"Заявка №: {breaking.breaking_number}, Дата: {breaking.breaking_date.strftime('%d.%m.%Y')}, Статус: {breaking.breaking_status}")
            y_position -= 20

        # Material List
        pdf.drawString(50, y_position, "Использованные материалы:")
        y_position -= 20
        for breaking_material in material_aggregated:
            material_name = breaking_material['material__material_name']
            total_quantity = breaking_material['total_quantity']
            pdf.drawString(50, y_position,
                           f"Материал: {material_name}, "
                           f"Общее количество: {total_quantity}")
            y_position -= 20

        # Breaking Statistics
        pdf.drawString(50, y_position, "Всего статусов:")
        y_position -= 20
        for stat in breaking_statistics:
            pdf.drawString(50, y_position, f"{stat['breaking_status']}: {stat['count']}")
            y_position -= 20

        pdf.showPage()
        pdf.save()

        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response
    else:
        return render(request, 'report.html', context)