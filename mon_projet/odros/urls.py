from .models import Domain, Training

# Get the domain you want to add the training to
domain = Domain.objects.get(pk=1)  # Replace domain_id with the actual ID

# Create a new training object
new_training = Training(
    domain=domain,  # Set the domain field
    training_name="web development",
    training_descrption="you will study the front-end  back-end  ",
)

# Save the new training
new_training.save()
# Create a new domain object
new_domain= Domain(
    domain=domain,  # Set the domain field
    training_name="Artificiel intelligence",
    training_descrption="it's a field which ntersting with maching learning     ",
)

# Save the new domain
new_domain.save()
