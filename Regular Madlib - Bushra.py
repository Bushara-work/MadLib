import random
# Note: Python 2.x users should use raw_input, the equivalent of 3.x's input

#Three story titles and templates
Titles_and_Templates = {
    "Final Advertisement Script": "Are you looking for a {first adjective} {first noun}? Look no further! Our {first adjective} {first noun} is now available for only {number} {plural noun}. This {second adjective} deal won’t last long, so {first verb} now!\n\nVisit our {third adjective} store, and for a limited time, get a free {second noun} with every purchase. Our {fourth adjective} team is ready to {second verb} you with any questions.\n\nHurry, this offer ends soon!",
    "Exciting Partnership Announcement!": "We are thrilled to announce a {first adjective} partnership between {first company name} and {second company name}. This collaboration will bring {second adjective} {first plural noun} and {third adjective} {second plural noun} to our customers.\n\nTogether, we will {verb} to achieve {first plural noun} and {second plural noun} to begin {present tense verb}!. We feel incredibly {emotion} to be partnering together!\n\nSincerely, The {first company name} and {second company name} Teams",
    "Emergency Advisory Notice": "Attention all residents,\n\nDue to an unexpected {noun}, we have {past tense verb} all {first adjective} activities until further notice. Please ensure that your {second noun} is {present tense verb} at all times.\n\nFor your safety, avoid {second adjective} {third noun} and remember to end any {third adjective} situations immediately./n/nThank you for your cooperation and understanding during this {fourth adjective} time,\n\n{name} "
                      }

#dictonary needed word and response going from empty to response filled
Advertisment_List = {'first adjective': '', 'first noun': '', 'number': '', 'plural noun': '', 'second adjective': '', 'first verb': '', 'third adjective': '', 'second noun': '', 'fourth adjective': '', 'second verb': ''}
Announcment_List = {'first adjective': '', 'first company name': '', 'second company name': '', 'second adjective': '', 'first plural noun': '', 'third adjective': '', 'second plural noun': '', 'verb': '', 'present tense verb': '', 'emotion': ''}
Advisory_List = {'first noun': '', 'past tense verb': '', 'first adjective': '', 'second noun': '', 'present tense verb': '', 'second adjective': '', 'third noun': '', 'third adjective': '', 'fourth adjective': '', 'name': ''}

user_name = input("What is your name?")

Play_Story = True
while Play_Story == True:
    #Ask for a story name or random story until an accepted value is retrieved
    while True:
        Story = input("If you know the story titles please enter one now, if not or if you wish for a random story selection enter 'Random'")
        if Story not in Titles_and_Templates.keys() and Story !='Random':
            print("Please check your, spelling, punctuation, or capitilization")
            continue
        #if Random is chosen pseudorandomly select a story
        else:
            if Story == 'Random':
                Stories_Titles_list = list(Titles_and_Templates.keys())
                Story = random.choice(Stories_Titles_list)
                
            print("Your story is: " + Story)
            break

    #Select the correct dictionary of required words to be requested, determined by the previously selected story
    if Story == "Final Advertisement Script":
        BlankSpace_Type = Advertisment_List
    elif Story == "Exciting Partnership Announcement!":
        BlankSpace_Type = Announcment_List
    else:
        BlankSpace_Type = Advisory_List



    #Set a variable that will eventually hold the completed story, currently holds the incomplete one
    Completed_Story = Titles_and_Templates[Story]

    #iterate through the keys of the selected story aka the word type
    for word in BlankSpace_Type.keys():
        #the word to be changed is the key placed in curly brackets
        sub = "{" + word + "}"

        #ask for needed word, it is the value/response to key/needed word
        BlankSpace_Type[word] = input("Please enter a/an: " + word)

        #if the entry if for the company names or name capatalize the first letter of each word
        if word == 'first company name' or word == 'second company name' or word == 'name':
            BlankSpace_Type[word] = BlankSpace_Type[word].title()
        
        #set the value/response as the replacement
        repl = BlankSpace_Type[word]
        
        #replace the placeholders with the associated response
        Completed_Story = Completed_Story.replace(sub, BlankSpace_Type[word])
        
    #Print the story name
    print("\n" + Story)
    #Print the Madlib
    print(Completed_Story)
    
    while True:
        Continue_Game = input("Do you want to continue playing?")
        if Continue_Game != 'yes' and Continue_Game != 'no':
            print("Please try again")
            continue
        elif Continue_Game == 'no':
            Play_Story = False
            goodbye_message = "Thank you for playing {0}".format(user_name)
            print(goodbye_message)
            break
        else:
            Play_Story = True
            break


