import ipywidgets as widgets
from IPython.display import display
from openai import OpenAI

# Initialize the API client
client = OpenAI()

input_box = widgets.Textarea(
    value='',
    placeholder='Enter your message here...',
    disabled=False,
    layout=widgets.Layout(width='100%', height='100px'),
    style={'description_width': 'initial'}
)

send_button = widgets.Button(
    description='Send Message',
    button_style='info',
    tooltip='Click to send your message',
    icon='paper-plane',
    layout=widgets.Layout(width='100%', height='50px', margin='10px 0')
)

output_area = widgets.Output(
    layout=widgets.Layout(border='1px solid #007BFF', width='100%', height='300px', overflow='auto')
)

display(input_box, send_button, output_area)

def handle_send_button_click(b):
    send_button.disabled = True  # Disable the button to prevent multiple clicks
    with output_area:
        output_area.clear_output(wait=True)
        print("Loading...")  # Show a loading message while processing
        user_message = input_box.value
        if user_message.strip() != '':
            bot_message = get_openai_response(user_message)
            output_area.clear_output()  # Clear the loading message
            print(f"Chatbot: {bot_message}")
        send_button.disabled = False  # Re-enable the button after displaying the message

send_button.on_click(handle_send_button_click)

def get_openai_response(user_message):
    system_prompt = '''
        You are a helpful HR Assistant Bot who answers employees' questions about internal policies. Here is a list of the most important policies. If you don't know an answer, ask the employee to email hr@example.com.

        Policies:
        1. Annual Leave: Employees are entitled to 20 days of paid leave per year, which can be accrued but must be used within the fiscal year.
        2. Health Benefits: Eligibility for health benefits, including medical and dental, begins 60 days after employment.
        3. Payroll: Payroll is processed on the last working day of the month. Any discrepancies should be reported immediately for correction in the next cycle.
        4. Flexible Working Hours: Employees may start their day anytime between 7:00 AM and 10:00 AM, provided they coordinate with their manager and complete the standard 8-hour workday.
        5. Professional Development: Employees have a budget of $2000 per year for attending conferences and training sessions. This budget covers all related expenses including transportation, accommodation, and registration fees. Applications for sponsorship must be approved based on departmental budgets and the relevance of the event to their professional growth.
    '''
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        model="gpt-3.5-turbo",
        temperature=0.2,
        max_tokens=50,
    )
    return response.choices[0].message.content
