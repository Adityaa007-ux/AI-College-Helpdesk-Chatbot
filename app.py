import streamlit as st

st.set_page_config(
    page_title="AI College Helpdesk Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI College Helpdesk Chatbot")

def get_response(user_input):

    text = user_input.lower()

    # Admission
    if "admission" in text or "apply" in text:
        return "Admissions are open through the official college portal. Fill the application form and upload required documents."

    # Eligibility
    elif "eligibility" in text or "criteria" in text:
        return "Eligibility depends on the selected course and minimum academic percentage."

    # Exam Timetable
    elif "timetable" in text or "schedule" in text:
        return "The exam timetable is released on the college website and notice board before exams."

    # Exam Results
    elif "result" in text or "marks" in text:
        return "Exam results are available on the student portal after evaluation."

    # Fees
    elif "fees" in text or "payment" in text:
        return "Fees can be paid online through the college payment portal."

    # Scholarship
    elif "scholarship" in text:
        return "Scholarship details are available at the student section."

    # Library
    elif "library" in text or "book" in text:
        return "The library is open from 9 AM to 5 PM on working days."

    # Hostel
    elif "hostel" in text or "accommodation" in text:
        return "Hostel facility is available based on seat availability."

    # WiFi
    elif "wifi" in text or "internet" in text:
        return "Wi-Fi facility is available for all registered students."

    # Transport
    elif "transport" in text or "bus" in text:
        return "College transport facility is available for students."

    # Sports
    elif "sports" in text or "games" in text:
        return "Sports facilities are available on campus."

    # Contact
    elif "contact" in text or "helpdesk" in text:
        return "You can contact the helpdesk at helpdesk@college.edu"

    else:
        return "Sorry, I could not understand your question."

question = st.text_input("Ask your question:")

if st.button("Ask"):

    if question:

        answer = get_response(question)

        st.write("### 🧑 You:")
        st.write(question)

        st.write("### 🤖 Bot:")
        st.write(answer)