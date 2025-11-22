from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import LoanApplication

# STEP 1 — Save data to session and go to confirm page
@login_required
def apply_loan(request):
    if request.method == "POST":

        # Create loan immediately (including file upload)
        loan = LoanApplication.objects.create(
            user=request.user,
            full_name=request.POST["full_name"],
            father_name=request.POST["father_name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            college_name=request.POST["college_name"],
            course_name=request.POST["course_name"],
            year_of_study=request.POST["year_of_study"],
            father_income=request.POST["father_income"],
            family_income=request.POST["family_income"],
            required_amount=request.POST["required_amount"],
            purpose=request.POST["purpose"],

            # FILE uploads saved here
            id_proof=request.FILES["id_proof"],
            student_photo=request.FILES["student_photo"],
            address_proof=request.FILES["address_proof"],
            marksheet_10=request.FILES["marksheet_10"],
            marksheet_12=request.FILES["marksheet_12"],
            college_id=request.FILES["college_id"],
            bank_statement=request.FILES["bank_statement"],
        )

        # Store loan ID temporarily in session
        request.session["pending_loan_id"] = loan.id

        return redirect("apply_confirm")

    return render(request, "apply_loan.html")



# STEP 2 — Show confirmation page
@login_required
def apply_confirm(request):
    loan_id = request.session.get("pending_loan_id")

    if not loan_id:
        return redirect("apply_loan")

    loan = LoanApplication.objects.get(id=loan_id)

    return render(request, "apply_confirm.html", {"loan": loan})



# STEP 3 — Final submit: Save to DB + save files + send email + success page
@login_required
def apply_submit(request):
    loan_id = request.session.get("pending_loan_id")

    if not loan_id:
        return redirect("apply_loan")

    loan = LoanApplication.objects.get(id=loan_id)

    # Optional email sending
    try:
        from django.core.mail import send_mail
        from django.conf import settings

        send_mail(
            subject="Your Loan Application Has Been Submitted",
            message=f"Thank you {loan.full_name}, your application ID is {loan.id}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[loan.email],
            fail_silently=True,
        )
    except:
        pass

    # Clear the temporary session
    del request.session["pending_loan_id"]

    return redirect("apply_success", loan_id=loan.id)



# SUCCESS PAGE
def apply_success(request, loan_id):
    loan = LoanApplication.objects.get(id=loan_id)
    return render(request, "success.html", {"loan": loan})





# LOAN STATUS PAGE
@login_required
def loan_status(request):
    loans = LoanApplication.objects.filter(user=request.user)
    return render(request, "loan_status.html", {"loans": loans})
