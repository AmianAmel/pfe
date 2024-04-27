from django.shortcuts import render, redirect
from .models import Domain, Training

def add_training(request):
    if request.method == 'POST':
        domain_id = request.POST['domain']
        training_name = request.POST['training_name']
        training_description = request.POST['training_description']

        domain = Domain.objects.get(pk=domain_id)
        new_training = Training(
            domain=domain,
            training_name=training_name,
            training_descrption=training_description,
        )
        new_training.save()

        # Redirect to a success page or another relevant view
        return redirect('success_page')  # Replace with your redirect URL

    else:
        domains = Domain.objects.all()
        context = {'domains': domains}
        return render(request, 'odros/add_training.html', context)
