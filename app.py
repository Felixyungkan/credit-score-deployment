import streamlit as st
import requests

# uvicorn api:app --reload
# streamlit run app.py

def main():

    st.title("Credit Score Prediction")

    col1, col2 = st.columns(2)

    with col1:

        month = st.selectbox(
            "Month",
            [
                "January","February","March","April",
                "May","June","July","August",
                "September","October","November","December"
            ]
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        occupation = st.text_input(
            "Occupation",
            "Engineer"
        )

        annual_income = st.number_input(
            "Annual Income",
            value=50000.0
        )

        num_bank_accounts = st.number_input(
            "Number of Bank Accounts",
            min_value=0,
            value=2
        )

        num_credit_card = st.number_input(
            "Number of Credit Cards",
            min_value=0,
            value=2
        )

        interest_rate = st.number_input(
            "Interest Rate",
            min_value=0,
            value=5
        )

        num_of_loan = st.number_input(
            "Number of Loans",
            min_value=0,
            value=1
        )

        delay_from_due_date = st.number_input(
            "Delay From Due Date",
            min_value=0,
            value=0
        )

        num_of_delayed_payment = st.number_input(
            "Number of Delayed Payments",
            value=0.0
        )

        changed_credit_limit = st.number_input(
            "Changed Credit Limit",
            value=5.0
        )

    with col2:

        num_credit_inquiries = st.number_input(
            "Number of Credit Inquiries",
            value=1.0
        )

        credit_mix = st.selectbox(
            "Credit Mix",
            ["Bad", "Standard", "Good"]
        )

        outstanding_debt = st.number_input(
            "Outstanding Debt",
            value=1000.0
        )

        credit_utilization_ratio = st.slider(
            "Credit Utilization Ratio",
            0.0,
            100.0,
            30.0
        )

        credit_history_age = st.number_input(
            "Credit History Age",
            value=10.0
        )

        payment_of_min_amount = st.selectbox(
            "Payment Of Min Amount",
            ["Yes", "No"]
        )

        total_emi_per_month = st.number_input(
            "Total EMI Per Month",
            value=200.0
        )

        amount_invested_monthly = st.number_input(
            "Amount Invested Monthly",
            value=300.0
        )

        payment_behaviour = st.selectbox(
            "Payment Behaviour",
            [
                "Low_spent_Small_value_payments",
                "Low_spent_Medium_value_payments",
                "Low_spent_Large_value_payments",
                "High_spent_Small_value_payments",
                "High_spent_Medium_value_payments",
                "High_spent_Large_value_payments"
            ]
        )

        monthly_balance = st.number_input(
            "Monthly Balance",
            value=3000.0
        )

        num_loan_types = st.number_input(
            "Number of Loan Types",
            min_value=0,
            value=1
        )

    if st.button("Make Prediction"):

        features = {

            "Month": month,
            "Age": age,
            "Occupation": occupation,
            "Annual_Income": annual_income,
            "Num_Bank_Accounts": num_bank_accounts,
            "Num_Credit_Card": num_credit_card,
            "Interest_Rate": interest_rate,
            "Num_of_Loan": num_of_loan,
            "Delay_from_due_date": delay_from_due_date,
            "Num_of_Delayed_Payment": num_of_delayed_payment,
            "Changed_Credit_Limit": changed_credit_limit,
            "Num_Credit_Inquiries": num_credit_inquiries,
            "Credit_Mix": credit_mix,
            "Outstanding_Debt": outstanding_debt,
            "Credit_Utilization_Ratio": credit_utilization_ratio,
            "Credit_History_Age": credit_history_age,
            "Payment_of_Min_Amount": payment_of_min_amount,
            "Total_EMI_per_month": total_emi_per_month,
            "Amount_invested_monthly": amount_invested_monthly,
            "Payment_Behaviour": payment_behaviour,
            "Monthly_Balance": monthly_balance,
            "Num_Loan_Types": num_loan_types
        }

        result = make_prediction(features)

        st.success(
            f"Predicted Credit Score: {result}"
        )


def make_prediction(features):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=features
    )

    return response.json()["prediction"]


if __name__ == "__main__":
    main()