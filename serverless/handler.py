import json

def five_attributes(event, context):
    body = {
        "name": "Esteban Pineda",
        "age": 30,
        "city": "Armenia",
        "email": "esteban@example.com",
        "phone": "1234567890",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def ten_attributes(event, context):
    body = {
        "name": "Felipe Lopez",
        "age": 28,
        "city": "Pereira",
        "email": "feli@example.com",
        "phone": "9876543210",
        "country": "Colombia",
        "occupation": "Software Engineer",
        "company": "Tech Corp",
        "hobby": "Photography",
        "website": "www.felipedev.com",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
