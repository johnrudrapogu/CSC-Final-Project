## Lambda Function for parsing notes


def lambda_handler(event, context):
    value = int(event['value'])
    bank_notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    notes_count = {}
    
    for note in bank_notes:
        count = value // note
        value -= count * note
        if count > 0:
            notes_count[str(note)] = count
    
    response = {'notes_count': notes_count}
    return response
