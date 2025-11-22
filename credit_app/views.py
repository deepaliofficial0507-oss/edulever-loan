from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def personal_loan(request):
    result = None
    income = loan_amount = tenure = ''

    if request.method == "POST":
        income = request.POST.get("income", "")
        loan_amount = request.POST.get("loan_amount", "")
        tenure = request.POST.get("tenure", "")

        # Dummy loan calculation logic
        if income and loan_amount and tenure:
            interest_rate = 10  # Example interest rate
            emi = (float(loan_amount) * (1 + (interest_rate / 100) * float(tenure))) / (float(tenure) * 12)
            result = round(emi, 2)

    return render(request, 'personal_loan.html', {
        "income": income,
        "loan_amount": loan_amount,
        "tenure": tenure,
        "result": result
    })

from django.shortcuts import render

from django.shortcuts import render

def loan_compare(request):
    offers = []
    income = amount = tenure = ''

    if request.method == "POST":
        print("✅ POST request received")  # Debug check

        income = request.POST.get("income", "")
        amount = request.POST.get("amount", "")
        tenure = request.POST.get("tenure", "")

        print("Income:", income, "Amount:", amount, "Tenure:", tenure)  # Debug line

        if income and amount and tenure:
            try:
                amount = float(amount)
                tenure = float(tenure)

                banks = [
                    {"name": "HDFC Bank", "rate": 10.75},
                    {"name": "ICICI Bank", "rate": 11.25},
                    {"name": "Axis Bank", "rate": 10.99},
                    {"name": "SBI Bank", "rate": 9.85},
                ]

                for bank in banks:
                    rate = bank["rate"] / 100 / 12
                    months = tenure * 12
                    emi = (amount * rate * (1 + rate) ** months) / ((1 + rate) ** months - 1)
                    offers.append({
                        "bank": bank["name"],
                        "rate": bank["rate"],
                        "emi": round(emi, 2)
                    })

                print("✅ Offers generated:", offers)

            except Exception as e:
                print("❌ Error:", e)

    return render(request, 'loan_compare.html', {
        "income": income,
        "amount": amount,
        "tenure": tenure,
        "offers": offers,
    })
