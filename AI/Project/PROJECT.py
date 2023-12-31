import re
import RESPONSES as res
#guessing the message response
def message_probability (user_message, recognised_words, single_response=False, required_words=[]):
    #function will take user message , the words that are recognized , if it is a single response , and list of required words 

    #merit counter
    message_certainty = 0
    #supposing it has required words
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            #incrementing the message_certainity by 1 meaning it is a more accurate sentense
            message_certainty += 1

    
    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            #seeing if the message has the required word for response
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        #if something matched
        return int(percentage * 100)
    else:
        #if nothing matched
        return 0
    
def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'coding'], required_words=['coding'])
    response('cricket',['play','like'],required_words=['play','like'])
    response('walaikum asalam',['salam'],required_words=['salam'])

    # Longer responses
    response(res.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(res.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    #matching the message
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    #return unknown if low score 
    return res.unknown() if highest_prob_list[best_match] < 1 else best_match

#for getting response
def get_response(userinput) :
    #spliting the message to check each word
    split_message = re.split(r'\s+|[,:?!.-]\s*',userinput.lower())
    #getting apropriate response by checking each word
    response = check_all_messages(split_message)
    return response

#infinte loop for questions
while True :
    #bot getting response
    print('bot:'+get_response(input('you:')))
