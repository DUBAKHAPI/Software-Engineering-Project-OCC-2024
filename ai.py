import openai
import mysql.connector

# Establish OpenAI API connections
openai.api_key = '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'
openai.organization = 'org-oGBGu9sxvYSvEpA9gj8iNCXA'

# Establish database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="paulsucks01!",
    database="Chatterbot"
)

# Create a cursor object
myCursor = connection.cursor()

# Define the first query to fetch data from the users table
query1 = "SELECT first_name, last_name, email, password FROM users"

# Execute the first query
myCursor.execute(query1)

# Fetch all the results from the users table
users_data = myCursor.fetchall()

# Define the second query to fetch data from the faqs table
query2 = "SELECT faq_name, faq_url FROM faqs"

# Execute the second query
myCursor.execute(query2)

# Fetch all the results from the faqs table
faq_data = myCursor.fetchall()

# Close the database connection
connection.close()

# Combine the data from both queries
combined_data = users_data + faq_data

# Generate response using OpenAI chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"prompt"}
    ]
)

generated_response = response['choices'][0]['message']['content']

print(generated_response)