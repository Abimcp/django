from django.db import models

# Create your models here.
dog_info = [
    { 'id': 1, 'name': 'Clifford', 'breed': 'Clumber Spaniel', 'Owner':'Abigail'},
    { 'id': 2, 'name': 'Baillie', 'breed': 'Border Collie', 'Owner':'Abigail'},
    { 'id': 3, 'name': 'Bracken', 'breed': 'Border Collie / GS', 'Owner':'Steven'},
    { 'id': 4, 'name': 'Clara', 'breed': 'Clumber Spaniel', 'Owner':'Abigail'}
]

class Breed(models.Model):
    name = models.CharField(max_length=100)
    temperament = models.TextField()

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    owner = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name} ({self.breed.name})'