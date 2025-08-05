def response_handler(res):
    if res.status_code != 200:
        print("Request failed")

    