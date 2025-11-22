from django.db import models
from django.contrib.auth.models import User

class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Personal
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)     # NEW FIELD
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Academic
    college_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    year_of_study = models.CharField(max_length=20)

    # Income
    father_income = models.IntegerField()
    family_income = models.IntegerField()
    required_amount = models.IntegerField()
    purpose = models.TextField()

    # Documents
    student_photo = models.ImageField(upload_to="loan_docs/student_photo/", null=True, blank=True)
    id_proof = models.FileField(upload_to='loan_docs/id_proof/')
    address_proof = models.FileField(upload_to='loan_docs/address_proof/')
    marksheet_10 = models.FileField(upload_to='loan_docs/marksheet_10/')
    marksheet_12 = models.FileField(upload_to='loan_docs/marksheet_12/')
    college_id = models.FileField(upload_to='loan_docs/college_id/')
    bank_statement = models.FileField(upload_to='loan_docs/bank_statement/')

    # Auto timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.required_amount}"
