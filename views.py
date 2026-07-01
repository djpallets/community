from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.apps import apps
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import capfirst

from .forms import UserForm


def staff_required(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


@login_required(login_url='/accounts/login/')
def dashboard(request):
    if not staff_required(request.user):
        return redirect('/accounts/login/')

    model_summaries = []
    for model in apps.get_models():
        if model._meta.app_label == 'auth' and model._meta.model_name == 'user':
            count = model.objects.count()
            model_summaries.append({
                'app_label': model._meta.app_label,
                'model_name': model._meta.model_name,
                'verbose_name': capfirst(model._meta.verbose_name_plural),
                'count': count,
            })
        elif model._meta.app_label != 'contenttypes' and model._meta.app_label != 'sessions':
            count = model.objects.count()
            model_summaries.append({
                'app_label': model._meta.app_label,
                'model_name': model._meta.model_name,
                'verbose_name': capfirst(model._meta.verbose_name_plural),
                'count': count,
            })

    return render(request, 'pallets/dashboard.html', {'models': model_summaries})


@login_required(login_url='/accounts/login/')
@user_passes_test(staff_required, login_url='/accounts/login/')
def model_list(request, app_label, model_name):
    model_class = None
    for candidate in apps.get_models():
        if candidate._meta.app_label == app_label and candidate._meta.model_name == model_name:
            model_class = candidate
            break

    if model_class is None:
        messages.error(request, 'The requested model was not found.')
        return redirect('pallets:dashboard')

    if model_class._meta.model_name == 'user':
        queryset = model_class.objects.all()
    else:
        queryset = model_class.objects.all()

    objects = []
    for obj in queryset:
        display_values = []
        for field in model_class._meta.fields[:4]:
            value = getattr(obj, field.name, '')
            display_values.append(value if value not in ('', None) else '-')
        obj.display_values = display_values
        objects.append(obj)

    return render(request, 'pallets/model_list.html', {
        'objects': objects,
        'app_label': app_label,
        'model_name': model_name,
        'verbose_name': capfirst(model_class._meta.verbose_name_plural),
        'display_fields': [field.verbose_name for field in model_class._meta.fields[:4]],
    })


@login_required(login_url='/accounts/login/')
@user_passes_test(staff_required, login_url='/accounts/login/')
def model_create(request, app_label, model_name):
    model_class = get_model_class(app_label, model_name)
    if model_class is None:
        messages.error(request, 'The requested model was not found.')
        return redirect('pallets:dashboard')

    form_class = modelform_factory(model_class, exclude=[])
    if model_class._meta.model_name == 'user':
        form_class = UserForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully.')
            return redirect('pallets:model_list', app_label=app_label, model_name=model_name)
    else:
        form = form_class()

    return render(request, 'pallets/model_form.html', {
        'form': form,
        'app_label': app_label,
        'model_name': model_name,
        'title': f'Create {capfirst(model_class._meta.verbose_name)}',
    })


@login_required(login_url='/accounts/login/')
@user_passes_test(staff_required, login_url='/accounts/login/')
def model_edit(request, app_label, model_name, pk):
    model_class = get_model_class(app_label, model_name)
    if model_class is None:
        messages.error(request, 'The requested model was not found.')
        return redirect('pallets:dashboard')

    obj = get_object_or_404(model_class, pk=pk)
    form_class = modelform_factory(model_class, exclude=[])
    if model_class._meta.model_name == 'user':
        form_class = UserForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully.')
            return redirect('pallets:model_list', app_label=app_label, model_name=model_name)
    else:
        form = form_class(instance=obj)

    return render(request, 'pallets/model_form.html', {
        'form': form,
        'app_label': app_label,
        'model_name': model_name,
        'title': f'Edit {capfirst(model_class._meta.verbose_name)}',
    })


@login_required(login_url='/accounts/login/')
@user_passes_test(staff_required, login_url='/accounts/login/')
def model_delete(request, app_label, model_name, pk):
    model_class = get_model_class(app_label, model_name)
    if model_class is None:
        messages.error(request, 'The requested model was not found.')
        return redirect('pallets:dashboard')

    obj = get_object_or_404(model_class, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Record deleted successfully.')
        return redirect('pallets:model_list', app_label=app_label, model_name=model_name)

    return render(request, 'pallets/model_delete.html', {
        'object': obj,
        'app_label': app_label,
        'model_name': model_name,
        'verbose_name': capfirst(model_class._meta.verbose_name),
    })


def get_model_class(app_label, model_name):
    for model in apps.get_models():
        if model._meta.app_label == app_label and model._meta.model_name == model_name:
            return model
    return None


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('pallets:dashboard')
    else:
        form = AuthenticationForm(request)

    return render(request, 'pallets/login.html', {'form': form})
