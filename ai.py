import openai
import mysql.connector

#Establish OpenAI API connections
openai.api_key = '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'
openai.organization = 'org-gpv1WLBaSK222UolWai5g5WW'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(response['choices'][0]['message']['content'])

# Establish database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="paulsucks01!",
    database="Chatterbot"
)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute("SELECT first_name, last_name FROM users")

# Fetch all rows
rows = cursor.fetchall()

# Process the data as needed
prompt = "Give me the name of each person in users"
for row in rows:
    # Construct the prompt using data from the database
    first_name = row[0]
    last_name = row[1]
    prompt += f"User: What is the first and last name of the person? First name: {first_name}, Last name: {last_name}\n"

# Close cursor and connection
cursor.close()
connection.close()


# Generate response using OpenAI
response = openai.Completion.create(
    engine="curie",  # Choose the appropriate engine
    prompt='Give me the name of each person in users',
    max_tokens=150
)

generated_response = response['choices'][0]['text'].strip()

print(generated_response)