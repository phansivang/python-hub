import requests
import concurrent.futures

# Define the POST data to send
data = {
    "surveyId": "6e4b44ba-6d25-40ef-be82-21bcefedaff3",
    "organizationId": "e9352737-446c-479b-8258-df936b6e1dc9",
    "categoryId": "a9a0f43a-75d5-4e7e-8b54-c7008761d37a",
    "fullName": "Ricky Test",
    "gender": "MALE",
    "email": "ricky.test@company.com",
    "phoneNumber": "012345678",
    "remark": "just testing",
    "languageCode": "EN",
    "platform": "API",
    "questions": [
        {
            "surveyQuestionId": "q1",
            "answer": "Food",
            "answers": [
                {
                    "surveyQuestionId": "q1",
                    "surveyQuestionAnswerId": "123a369e-a912-4115-8c24-bf81e954b29e",
                    "type": "TEXT",
                    "answer": "Food"
                }
            ]
        },
        {
            "surveyQuestionId": "q123",
            "answer": "Very likely",
            "answers": [
                {
                    "surveyQuestionId": "q123",
                    "surveyQuestionAnswerId": "892937b2-3177-416b-99ef-d3f93af9c6d5",
                    "type": "TEXT",
                    "answer": "Very likely"
                }
            ]
        },
        {
            "surveyQuestionId": "q2",
            "answer": "The website is well-organized and easy to navigate.",
            "answers": [
                {
                    "surveyQuestionId": "q2",
                    "surveyQuestionAnswerId": "5e4a52dc-d2e0-4663-883b-6b23fe794082",
                    "type": "TEXT",
                    "answer": "The website is well-organized and easy to navigate."
                }
            ]
        },
        {
            "surveyQuestionId": "q3",
            "answer": "The website is visually unappealing.",
            "answers": [
                {
                    "surveyQuestionId": "q3",
                    "surveyQuestionAnswerId": "67e16d88-7e23-4b27-8144-d9393fffc31a",
                    "type": "TEXT",
                    "answer": "The website is visually unappealing."
                }
            ]
        },
        {
            "surveyQuestionId": "q4",
            "answer": "Never",
            "answers": [
                {
                    "surveyQuestionId": "q4",
                    "surveyQuestionAnswerId": "113ac61e-ab98-47ac-8e46-3e63abae0e77",
                    "type": "TEXT",
                    "answer": "Never"
                }
            ]
        }
    ]
}

# Now 'data' is a Python dictionary that you can work with

# Define the API endpoint URL
url = "https://survey-api-dev-3xhko3k52a-as.a.run.app/v1/surveys/results"

# Define the number of concurrent users (threads) and the total requests
concurrent_users = 10  # You can adjust this based on your requirements
total_requests = 500  # Total requests to make per concurrent user

# Define a function for making POST requests
def make_post_request():
    for _ in range(total_requests):
        response = requests.post(url, json=data)
        # You can add assertions or logging here to check the response if needed
        # For example, assert response.status_code == 200

# Create a ThreadPoolExecutor to manage concurrent users
with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
    # Submit the POST request tasks
    futures = [executor.submit(make_post_request) for _ in range(concurrent_users)]

# Wait for all tasks to complete
concurrent.futures.wait(futures)
