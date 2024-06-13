print("Welcome to health check")
name=input("What is your name: ")
print("Hey there, how are you feeling today?")

loop1=0
while loop1==0:

    loop = 0

    while loop == 0:
        user_symptom=input("\nEnter your symptoms separated by space  \n Head ache - 1 \n high body temperature - 2 \n Fast heart rate - 3 \n Running nose - 4 \n loss of apetite - 5 \n Abdomen pain - 6 \n Fever - 7 \n Fatigue - 8 \n excessive sweating - 9 \n Heart burn - 10 \n Indigestion - 11 \n Chest pain - 12 \n Chills - 13 \n Bloating - 14 \n Sore throat - 15 \n Dehydration - 16 \n Hot/dry skin - 17 \n Loss of consciousness - 18 \n Nausea - 19 \n Seizure - 20 \n Weight loss - 21 \n Diarrhoea - 22 \n Hair loss - 23 \n Depression - 24 \n Flaky skin - 25 \n Cough - 26 \n Eye irritation - 27 \n sneezing -28 \n Itchy nose and throat - 29 \n Rashes- 30 \nShortness of breath - 31\n ->")
        Malaria =[1,2,3,6,10]
        cold=[4,7,13,26,28]
        Menstrual_pain=[2, 5, 6, 11, 14, 19, 22, 24]
        Ulcer = [11, 3, 10, 6, 12]
        Typhoid = [8,7,2,14,1,21,22]
        Fever = [5,4,15,1,26]
        Heat_stroke=[16,20,18,2,23,26]
        cancer=[23,24,25,]
        allergies=[27,28,29,30,26,25,15,14]
        High_blood_pressure=[31,3,12,1,18]
        

        input_symptoms = []

        if len(user_symptom.split()) == 1:

            input_symptoms.append(user_symptom)

            loop2 = 0

            while loop2 == 0:   

                only = input("Are you experiencing any other symptoms? (YES?NO) \n")
                
                if only.lower() == "yes":
                
                    user_symptom2 = input("Enter your symptoms separated by space  \n Head ache - 1 \n high body temperature - 2 \n Fast heart rate - 3 \n Running nose - 4 \n loss of apetite - 5 \n Abdomen pain - 6 \n Fever - 7 \n Fatigue - 8 \n excessive sweating - 9 \n Heart burn - 10 \n Indigestion - 11 \n Chest pain - 12 \n Chills - 13 \n Bloating - 14 \n Sore throat - 15 \n Dehydration - 16 \n Hot/dry skin - 17 \n Loss of consciousness - 18 \n Nausea - 19 \n Seizure - 20 \n Weight loss - 21 \n Diarrhoea - 22 \n Hair loss - 23 \n Depression - 24 \n Flaky skin - 25 \n Cough - 26 \n Eye irritation - 27 \n sneezing -28 \n  itching nose and throat - 29 \n Rashes- 30 \nShortness of breath - 31 \n->")
                    input_symptoms.append(user_symptom2)

                elif only.lower() == "no":
                    loop2 += 1

                
                    if len(input_symptoms) == 1:

                        input_symptom = input_symptoms[0]

                        match input_symptom:
                            case "1" :
                                extraInfo_1 = input("What area are you feeling the headache?\n(1. Right, 2. Left, 3. Back): \n")

                                if extraInfo_1.lower() == "2" or "left":
                                    print("A headache on the side of your head can be due to a primary headache disorder,\nlike 'migraine' or 'cluster headache'. It can also occur due to an injury like a concussion\n, lifestyle factors like diet or insufficient sleep,\n or a condition such as allergies, high blood pressure, or stroke\n")
                            
                            # elif extraInfo_1.lower()=="1" or "right":
                                # print("A headache on the right side of the head is often caused by a migraine, tension, or cluster headache.")
                            
                                #elif extraInfo_1.lower()== "3" or "back":
                                    #print("It is most like a tension or tension-type headaches (TTH) usually cause tightness or pressure around the forehead, and may also cause discomfort in the neck, shoulders, or scalp.\n These headaches can last for up to 7 days, but they can also be brief, lasting for as little as 30 minutes.\n")
                                else:
                                    print(f"\n{name}, I'm sorry to hear that you're experiencing a headache! Here are some natural remedies you can try to alleviate it:: \n ")
                                    print("Stay Hydrated.\n ")
                                    print("Consider taking pain relief tablet\n")
                                    print("Cold Compress: Apply an ice pack to your forehead to relieve pain. \n")
                                    print("Warm Compress: For tension headaches, use a heating pad on your neck or the back of your head.\n")
                                    print("Reduce bright light exposure to ease headache symptoms.\n")
                                    print("Rest and Sleep \n")
                    
                            case "2":
                                extraInfo_2 = input("Are you feeling \n Tired - A \n nauseous - B \n None - C \n")
                                match extraInfo_2.lower():
                                    case "a":
                                        print(F"{name}, you most likely have a fever, contact your Doctor.\n")
                                    case "b" :
                                        input_gender=input("Are you a (male?Female)\n")
                                        if input_gender.lower()=="male":
                                            print(f"{name}, you most likely have a fever, Contct your Doctor")
                                        elif  input_gender.lower()=="female":
                                            print(f"{name} are you pregnant? if yes, it could be early stages of Pregancy, if not maybe a Fever, contant your Doctor")      

                                    case "c" :
                                        print(f"{name} If your body temperature is high, follow these steps:\n ")
                                        print("Call your doctor immediately if your temperature is 103°F (39.4°C) or higher.\n")
                                        print("For temperatures between 100 and 102°F, drink plenty of fluids and rest. You can take a fever reducer if you like.\n")
                                        print("Call your doctor if your temperature is over 102°F and it doesn't go down within an hour after taking a fever-reducing medication")                            
                                    case _:
                                        # default code block
                                        print(f"{name} If your body temperature is high, follow these steps:\n ")
                                        print("Call your doctor immediately if your temperature is 103°F (39.4°C) or higher.\n")
                                        print("For temperatures between 100 and 102°F, drink plenty of fluids and rest. You can take a fever reducer if you like.\n")
                                        print("Call your doctor if your temperature is over 102°F and it doesn't go down within an hour after taking a fever-reducing medication")    
                            case "3":
                                extraInfo_3 = input("Is your fast heart rate sudden (yes?no)")
                                match extraInfo_3.lower():
                                    case "no":
                                        heartrate_condition= input("what do you think trigger it (select one below)?\n 1. heavy exercise\n 2. stress, fear or anxiety\n 3.Too much alcohol or caffine\n 4.Use of hard drugs\n5.None of the above\n-> ")
                                        match heartrate_condition.lower():
                                            case "1":
                                                print(f"\n{name}, do not panic, your heart rate is faster because you just finished exercising. \nTake enough water and relax, if it gets worse contact your Doctor.")
                                            case "2":
                                                print(f"\n{name}, your heart rate may be faster, because of anxiety which comes from our nervous system \n\n Calm yourself by engaging in calming activities like yoga, meditation or mindfulness exercise that help you focus on your breathing.")
                                            case "3":
                                                print(f"Too much alcohol or caffine may be the reason your heart rate is faster than usual.\nMake sure to reduce your intake of Alchol!")
                                            case "4": 
                                                print("stay away for hard drugs. It is a killer!")  
                                            case _:
                                                print("Invalid Input")
                            case "4":
                                print("On its own, a runny nose isn't usually a cause for concern. If you don't have any other symptoms, there are several ways to manage a runny nose at home with natural self-care options that don't involve medication.\n")
                                print("Here are some tip that could help:\n")
                                print("Drink plenty of Fluid, Drink hot teas and do facial steaming\n")
                            
                            case "6":
                                print(f"Sorry {name}, Abdominal pain is not always related to an underlying condition. It may be caused by:\n- Constipation \n- Menstrual cramps\n- Indigestion\n- Overeating\n- Pulled or strained muscles\n If none of this applies to you, contact your Doctor.")
                            
                            case "7":
                                print(f"\n{name}, fever itself is not necessarily unhealthy. It's not an illness; it's a physiological response to something else. Your body will often react to sickness or infection with a fever")

                            case "8": 
                                print(f"\nThis tips should help {name}\n")
                                print("Get moving and exercise regularly.\n")
                                print("Stay hydrated by drinking plenty of water.\n")
                                print("Prioritize getting enough sleep.\n")
                                print("Eat a balanced diet of fruits, veggies, and lean protein\n")

                            case "9":
                                print(f"{name}, here are some tips that could help:\n")
                                print ("Use antiperspirants before going to bed and wear breathable fabrics ")

                            case "10":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("If you have heartburn, certain types of food and drinks can trigger your symptoms, so you might want to avoid them.\n") 
                                print("carbonated drinks, chocolate, citrus fruits, tomatoes and tomato-based products, peppermint, fried foods, spicy foods, high fat foods, alcohol\n")
                                print("If it gets worse contact your Doctor.\n")
    
                            case "11":  
                                print(f"{name},if you are expericence some of these other symptoms like: Bloating, Heartburn, Belching, Nausea, Abdominal pain, Feeling uncomfortably full and probably Loss of appetite\n")
                                print("It is most likely you have Dyspepsia.\n")
                                print("Here are some tips that could help:\n")
                                print("Reduce your intake of fatty meals\n")
                                print(" Reduce alcohol and tobacco use\n")
                                print("Reduce carbonated drinks intake\n")
                                print("Managing stress\n")   
                                print("Regular exercise\n\n")  
                                print("If it gets worse contact your Doctor.\n")

                            case "12":  
                                print(f"{name}, If your chest pain is mild, use a pain relief medication but if not Contact your Doctor\n")

                            case "13":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("Get plenty of rest and fluids\n") 
                                print("Use fever reducers, such as Tylenol\n")
                                print("Sponge your skin with lukewarm water\n")
                                print ("Wear layers of clothes or use a light sheet\n")
                                print("Turn up the temperature in your home\n")

                            case "14": 
                                print(f"{name}, here are some tips that could help:\n") 
                                print(" Drinking water before, during, and after meals to flush out excess sodium\n")
                                print(" Walking and other simple exercises to get the digestive system moving\n")
                                print("Abdominal self-massage to help release gasses\n")
                                print("Over-the-counter medications and supplements that can ease bloating\n")
                                print("Eating slowly and sitting down during meals to avoid taking in too much air\n")

                            
                            case "15":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("saltwater gargle")
                                print("use an over-the-counter (OTC) pain relief")
                                print ("Take a steam shower")
                                print ("Use an antibiotics")  


                            case "16":  
                                print(f"{name}, here are some tips that could help:\n\n")
                                print("Drink water or oral rehydration solutions that provide essential electrolytes.\n")
                                print("Avoid full-strength fruit juice and soft drinks that may worsen diarrhea.")
                                print("Cool your body and remove any excess clothing.\n")
                                print("Eat foods high in water and add flavor to your drinks if needed.\n")
                                print("Seek medical attention if you have severe dehydration or signs of dehydration in a baby or young child.\n")


                            case "17":  
                                print(f"{name}, here are some tips that could help:\n\\n")
                                print("The following measures can help keep your skin moist and healthy:\n")
                                print("Gently wash your face at least twice a day. Use a gentle, alcohol-free, nonfoaming cleanser on your face twice a day and after sweating.\n")
                                print(" Moisturize.\n")
                                print("Use warm water and limit bath time.\n")
                                print("Use allergen-free moisturizing soap.\n")
                                print("Use a humidifier.\n")    

                            case "18":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("When someone loses consciousness, the best action is to follow the ABCs or CABs:\n")
                                print("Check to see if their airway is open. Is there something in their mouth blocking their airflow.\n")       
                                print("It could be that the tongue is blocking their airway. Check to see if they are breathing.\n ")
                                print("If they are not breathing, you may need to breathe for them. And, most importantly, check for circulation.\n")
                                print("If there is no pulse, start CPR and call 911,” Keany said.\n") 


                            case "19":
                                print(f"{name}, here are some tips that could help:\n")
                                print("Eat a small amount of something dry, like plain crackers or plain bread.\n")
                                print("Slowly sip water or something clear and cold.\n")  
                                print("Avoid alcoholic beverages, dairy products, smoothies, and vegetable juice.\n")
                                print("Try ginger or peppermint.\n")
                                print(" Avoid carbonated beverages.\n")  

                            case "20":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("Move to a safe place.\n")
                                print("Take medication if prescribed.\n")
                                print("Tell someone and try to make sure someone remains with you.\n")
                                print("Sit or lie down")    
                                print("Loosen tight clothing")
                                print ("If it's your first seizure, see a doctor as soon as possible.\n")             
                                                            
                            case "21":  
                                print(f"{name}, if you're losing weight without trying and you're concerned about it, consult your health care provider\n")
                        
                            case "22":  
                                print(f"{name}, sorry to know you have diarroea, this could helpWhen you have diarrhea,this tips should help,\nget lots of rest, drink plenty of water, and start introducing BRAT foods after a few hours.\nAfter a day or 2 of bland, soft foods, you can add in foods like lean ground chicken and scrambled eggs.\n")            

                            case "23":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("1. Scalp massage\n2. Essential oils\n3. Anti-thinning shampoo\n4. Multivitamins\n")             

                            case "24":  
                                print(f"{name}, here are some tips that could help:\n\n")
                                print("What To Do When You Feel Depressed.\n")   
                                print("1. Learn your depression warning signs.\n")
                                print("2. Reach out to your support network.\n")
                                print("3. Practice good sleep habits.\n")
                                print("4. Focus on good food.\n")
                                print("5.Limit alcohol intake.\n")
                                
                            
                            case "25":  
                                print(f"{name}, here are some tips that could help:\n\n")
                                print("To combat flaky skin on the face, you can:\n")
                                print("Apply a high-quality moisturizer to your face every day.\n")  
                                print("  Use a mild cleanser.\n")
                                print("Gently exfoliate.\n")
                                print("Crank up the humidifier.\n")
                                print(" Consult the experts.\n")
                                print("If dryness doesn't go away or is severely itchy, contact your dermatologist.\n")      

                            case "26":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("Use cough drops to soothe your throat. Gargle with warm salt water regularly to remove mucus and soothe your throat. Avoid irritants, including smoke and dust. Add honey or ginger to hot tea to relieve your cough and clear your airway. Use decongestant sprays to unblock your nose and ease breathing.\n")    
                                print("")             
                            case "27":  
                                print(f"{name}, here are some tips that could help:\n")
                                print("Eye irritation can be uncomfortable, but there are several ways to find relief. Here are some steps you can take:\n")
                                print("Use Eye Drops: Over-the-counter eye drops or hexane-free castor oil drops can soothe dry, itchy eyes.")
                                print("Cool Compress: Apply a cool compress to your eyes to reduce inflammation and discomfort.")
                                print("Avoid Allergens: Stay away from allergens that might trigger irritation.")
                                print("Take Screen Breaks: If you spend a lot of time looking at screens, take frequent breaks to rest your eyes.")
                                print("Run a Humidifier: Using a humidifier in your room at night can help keep your eyes moist\n")        

                            case "28":  
                                print("Your sneeze could a result from allergies.\n")
                                print(f"{name}, here are some tips that could help in preventing the spread of germs:\n")
                                print("1 Cover your nose and mouth with a thick tissue.")  
                                print("2 Sneeze into your elbow.\n")  
                                print("3 Don't sneeze into your hands.\n")  
                                print("4 Wash your hands.\n")  
                                print("5 Stay away from people.\n ")

                            case "29":  
                                    print(f"{name}, here are some self- care steps that may be helpful in some less-serious cases:\n")
                                    print("Gargle in salt water.\n")             
                                    print("Stay away from irritants such as smoke.\n")
                                    print("Drink warm soup.\n")
                                    print("Try home remedies such as herbal tea, ginger tea, or turmeric in milk.\n")
                                    print("Rest your throat if the cause is strain due to continuous shouting or singing practice for events\n \n")
                                    print(" See a doctor if you notice:")
                                    print("Persistent symptoms")
                                    print("Fever")
                                    print("Difficulty swallowing")
                                    print("Hoarseness or impaired voice")
                                    


                            case "30":  
                                    print(f"{name}, here are some tips that could help:\n")
                                    print("Self-treatment: Self- care steps that may be helpful in some less- serious cases:")     
                                    print("Use non- scented soaps.\n")
                                    print("Limit scratching of the rash.\n")
                                    print("Use tepid water for bathing.\n")
                                    print("Use over the counter anti fungal creams for conditions such as athlete's foot.\n")
                                    print("If it get worse, contact your doctor!")
                            
                            case "31":  
                                
                                    print(f"{name}, See a doctor immediately if you notice: shortness in breath\n")

                        loop += 1


        if (len(user_symptom.split()) > 1 or len(input_symptoms) > 1) :
            symptom = []
            if len(input_symptoms) == 0:
                symptom = user_symptom.split()
            else:
                symptom = input_symptoms

            x = len(symptom)
            malariaCounter = 0
            ulcerCounter = 0
            TyphoidCounter = 0
            FeverCounter = 0
            Heat_strokeCounter = 0
            cancerCounter = 0
            allergiesCounter=0
            High_blood_pressurecounter = 0

            for i in symptom:
                if (int(i) in Malaria):
                    malariaCounter += 1
                if (int(i) in Ulcer):
                    ulcerCounter += 1
                if (int(i) in Typhoid):
                    TyphoidCounter += 1
                if (int(i) in Fever):
                    FeverCounter += 1
                if (int(i) in Heat_stroke):
                    Heat_strokeCounter +=  1  
                if (int(i) in cancer):
                    cancerCounter +=  1      
                if (int(i) in allergies):
                    allergiesCounter += 1     
                if (int(i) in High_blood_pressure):
                    High_blood_pressurecounter += 1   


            if malariaCounter == x:
                print(f"{name}, you have Malaria symptom, Pls visit your Doctor to do blood test")

            elif ulcerCounter == x:
                print(f"{name}, you have Ulcer symptom, Pls visit your Doctor ")
            
            elif FeverCounter == x:
                print(f"{name}, you have fever symptom, Pls visit your Doctor")

            elif TyphoidCounter == x:
                print(f"{name}, you have Typhoid symptom, Pls visit your Doctor for proper Check up and administretion of drugs ")
            
            elif cancerCounter == x:
                print(f"{name}, you have cancer symptom, Pls visit your Doctor for proper Check up and administretion of drugs  ")

            elif Heat_strokeCounter == x:
                print(f"{name}, you have heat stroke symptom, Drink enough of water and stay in an Open space and seek medical attention ")
            
            elif High_blood_pressurecounter == x:
                print(f"{name}, you have high blood pressure symptom, Drink enough of water and stay in an Open space and seek medical attention ")
            elif allergiesCounter == x:
                print(f"{name}, you have allergies symptom, Be mindfull of what you consume and if your symptoms get worse\n")
                print("Try to pin point what triggers your allergies and then take steps to minimize your expose to them or consult a specialist.")

            elif malariaCounter >= (x*(65/100)):
                print(f"{name}, you probabaly have malaria.")

            elif ulcerCounter >= (x*(65/100)):
                print(f"{name}, you probabaly have ulcer.")

            elif TyphoidCounter >= (x*(65/100)):
                print(f"{name}, you probabaly have Typhoid.")

            elif FeverCounter >= (x*(65/100)):
                print(f"{name}, you probabaly have Fever.")     

            elif Heat_strokeCounter >= (x*(65/100)):
                    print(f"{name}, you probabaly have heat stroke.")
        
            elif cancerCounter >= (x*(65/100)):
                print(f"{name}, you probabaly have cancer.")

            elif High_blood_pressurecounter >= (x*(65/100)):
                print(f"{name}, you probabaly have high blood pressure.")

            else:
                print(f"{name}, sorry I can't process your ailment, kindly seek a medical attention.")
            
            loop += 1
            
        #loop_continue = input("\n Do you have any other issues (YES/NO) \n ->")
       # if loop_continue.lower() == "no":
#loop += 1
        
      #  if loop_continue.lower() == "yes":
       #     break
    print(f"\n It was great to help you with an health check {name}. \n")   
    print("Don't forget always go for your regular check up within three to six months\n ")    
    print("Stay healthy, remember health is wealth 😊\n")   
    extra = input("\nIs there any other aliment you want me to help you check  (NO?YES)\n ->")        
    if extra.lower() == "yes":
        print (f"Ok {name}")

    else:
      print("Thank you and have a nice day 😊")
      break
      quit()
      

  #

    # something else

    # if user_symptom.lower() == "a " :
    #  print("")
      

# if symptom in Malaria :#or symptom ==  Malaria:
#     print("You have Malaria symptom, Pls visit your Doctor to do blood test")

#     if user_symptom.lower() == "a " :
#      print("")













#else:
  # print("You are advice to See your Doctor ")



























