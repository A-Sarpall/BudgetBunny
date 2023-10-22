import streamlit as st

def financial_literacy_quiz():
    """
    Function to create a financial literacy game using Streamlit.

    This function will create a web application where users can play a financial literacy game.
    The game will present users with multiple-choice questions related to personal finance,
    and provide feedback on their answers.

    Returns:
    - None
    """

    # Define the questions and their corresponding answers
    questions = [
        {
            "question": "What is the recommended percentage of your income to save each month?",
            "choices": ["Select Choice", "10%", "25%", "50%"],
            "correct_answer": "25%"
        },
        {
            "question": "What is the difference between a debit card and a credit card?",
            "choices": ["Select Choice",
                        "Debit card is linked to your bank account, while credit card allows you to borrow money", 
                        "Debit card is used for online purchases, while credit card is used for in-person purchases",
                        "Debit card has a lower interest rate than credit card"],
            "correct_answer": "Debit card is linked to your bank account, while credit card allows you to borrow money"
        },
        {
            "question": "What is a credit score?",
            "choices": ["Select Choice",
                        "A score that measures your ability to save money", 
                        "A score that measures your ability to repay debt on time",
                        "A score that measures your income"],
            "correct_answer": "A score that measures your ability to repay debt on time"
        },
        {
        "question": "What is the 50/30/20 rule in personal finance?",
        "choices": [
            "Select Choice",
            "A budgeting rule that suggests allocating 50% of income to essentials, 30% to wants, and 20% to savings and debt repayment",
            "A rule that recommends investing 50% of your income in stocks, 30% in bonds, and 20% in cash",
            "A guideline for investing 50% of your income in long-term assets, 30% in short-term assets, and 20% in high-risk assets"
        ],
        "correct_answer": "A budgeting rule that suggests allocating 50% of income to essentials, 30% to wants, and 20% to savings and debt repayment"
    },
    {
        "question": "What does ROI stand for in finance?",
        "choices": ["Select Choice", "Return on Investment", "Rate of Interest", "Risk of Investment"],
        "correct_answer": "Return on Investment"
    },
    {
        "question": "What is the best way to build an emergency fund?",
        "choices": [
            "Select Choice",
            "Investing in stocks",
            "Putting all your extra money in a savings account",
            "Setting aside a portion of your income regularly in a high-yield savings account"
        ],
        "correct_answer": "Setting aside a portion of your income regularly in a high-yield savings account"
    },
    {
        "question": "What is a common form of long-term investment?",
        "choices": ["Select Choice", "Savings account", "Certificate of deposit (CD)", "Piggy bank"],
        "correct_answer": "Certificate of deposit (CD)"
    },
    {
        "question": "What is the difference between a traditional IRA and a Roth IRA?",
        "choices": [
            "Select Choice",
            "Traditional IRA contributions are tax-deductible, and Roth IRA contributions are not tax-deductible.",
            "Traditional IRA contributions are never taxed, and Roth IRA contributions are always taxed.",
            "There is no difference between traditional and Roth IRAs."
        ],
        "correct_answer": "Traditional IRA contributions are tax-deductible, and Roth IRA contributions are not tax-deductible."
    },
    {
        "question": "What is compound interest?",
        "choices": [
            "Select Choice",
            "Interest calculated only on the initial principal",
            "Interest calculated on the initial principal and the accumulated interest from previous periods",
            "Interest calculated at a fixed rate annually"
        ],
        "correct_answer": "Interest calculated on the initial principal and the accumulated interest from previous periods"
    },
    {
        "question": "What is a common type of insurance that covers medical expenses?",
        "choices": ["Select Choice", "Auto insurance", "Home insurance", "Health insurance"],
        "correct_answer": "Health insurance"
    },
    {
        "question": "What does FICO stand for in the context of credit scores?",
        "choices": [
            "Select Choice",
            "Fair Investment Credit Option",
            "Fast Internet Checkout Option",
            "Fair Isaac Corporation"
        ],
        "correct_answer": "Fair Isaac Corporation"
    },
    {
        "question": "What is a common type of consumer debt?",
        "choices": ["Select Choice", "Mortgage", "Stocks", "Savings account"],
        "correct_answer": "Mortgage"
    },
    {
        "question": "What is diversification in investing?",
        "choices": [
            "Select Choice",
            "Putting all your money into a single investment",
            "Spreading investments across different assets to reduce risk",
            "Investing in high-risk assets only"
        ],
        "correct_answer": "Spreading investments across different assets to reduce risk"
    },
    {
        "question": "What is an example of a tax-advantaged retirement account?",
        "choices": ["Select Choice", "Savings account", "401(k)", "Checking account"],
        "correct_answer": "401(k)"
    },
    {
        "question": "What is the purpose of a budget?",
        "choices": [
            "Select Choice",
            "To restrict your spending",
            "To allocate your income to different categories and track your financial goals",
            "To invest in high-risk assets"
        ],
        "correct_answer": "To allocate your income to different categories and track your financial goals"
    }
    ]

    # Initialize a variable to keep track of the user's score
    score = 0

    # Display the game title
    st.title("Financial Literacy Quiz")

    # Loop through each question
    for i, question in enumerate(questions):
        # Display the question
        st.subheader(f"Question {i+1}:")
        st.write(question["question"])

        # Get the user's answer
        user_answer = st.radio("Your answer:", question["choices"])

        # Check if the user's answer is correct
        if user_answer == question["correct_answer"]:
            st.write("Correct!")
            score += 1
        else:
            st.write("Incorrect!")

    # Display the final score
    st.subheader("Final Score:")
    st.write(f"You scored {score} out of {len(questions)}.")

# Run the financial literacy game
if __name__ == "__main__":
    financial_literacy_quiz()