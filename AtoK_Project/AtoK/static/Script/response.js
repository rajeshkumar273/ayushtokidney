function getBotResponse(input) {
    //Main Kidney Questions 
    if (input == "What is a kidney disease?") {
        return "Chronic kidney disease (CKD) is a long-term condition where the kidneys don't work as well as they should.";
    } else if (input == "what food suggest if a person has kidney disease eat?") {
        return "It's a diet rich in fruits, veggies, low-fat dairy products, whole grains, fish, poultry, beans, seeds, and nuts. It's low in sodium, sugars and sweets, fats, and red meats.";
    } else if (input == "What is the best medicine for CKD?") {
        return "Commonly used medicines include calcium acetate and calcium carbonate. Some people with CKD also have low levels of vitamin D, which is necessary for healthy bones. If you're low in vitamin D, you may be given a supplement called colecalciferol or ergocalciferol to boost your vitamin D level.";
    } else if (input == "What medications can improve kidney function?") {
        return "ACE inhibitors and ARBs are two types of blood pressure medicine that may slow the loss of kidney function and delay kidney failure.";
    }else if (input == "Tests might include:") {
        return "Blood tests,  Urine tests, Imaging tests, Removing a sample of kidney tissue for testing";
    } else if (input == "Treating the cause") {
        return "Your doctor will work to slow or control the cause of your kidney disease. Treatment options vary depending on the cause. But kidney damage can continue to worsen even when an underlying condition, such as diabetes mellitus or high blood pressure, has been controlled.";
    } else if (input == "What do kidneys do for us?") {
        return "Kidneys filter waste and excess fluid from our blood.";
    }
    // More Questions
    else if (input == "Causes?") {
        return "It s can be caused by type 1 or 2 diabetes, high blood pressure, glomerulonephritis (inflammation of the kidneys filtering units), vesicoureteral (condition that causes urine to back up into the kidneys), and many more.";
    }else if (input == "Treatment") {
        return "Kidney disease does not usually become apparent until the kidneys function is significantly impaired. This can lead to the disease being fatal wihtout treatment such as dialysis (artificial filtering) or a kidney transplant.";
    }else if (input == "How would I know if I have a kidney disease?") {
        return "Since the kidneys purify and keep nutrients in the blood, then dispose of waste through urine, both blood and urine tests can reveal if you have a kidney disease.";
    } else if (input == "I don t have any pain. How can I have a kidney problem?") {
        return "Symptoms of kidney diseases may not show right away. As the number of nephrons in each kidney can be as many as a million, you may not notice issues even if your kidneys are functioning at only 10% of their capacity 1.";
    }else if (input == "What are the common causes of kidney diseases?") {
        return "High blood pressure, diabetes and obesity are the most common causes of kidney diseases.High blood pressure damages the tiny blood vessels and filtering units in the kidneys, reducing the kidneys’ capacity to remove excess water and waste from the blood.";
    }else if (input == "I have had high blood pressure for a long time — is that normal?") {
        return "Blood pressure at <120/80 mm Hg is considered normal. A reading of 120-129 mm Hg systolic and greater than 80 mm Hg diastolic is considered high. An individual with a blood pressure of 130 mm Hg systolic or 80-89 mm Hg diastolic has hypertension and is more vulnerable to have heart disease and stroke 3.";
    }else if (input == "What are the symptoms of kidney disease?") {
        return "When the kidneys cannot filter waste products and retain nutrients properly, protein and blood may “leak” into the urine. If your urine is foamy, it may indicate that there is protein in it 4.";
    }else if (input == "How does kidney disease cause anemia?") {
        return "Kidney disease or damage can be the cause of anemia. Anemia means that the body does not have enough red blood cells to transport oxygen throughout the body. The kidneys create a hormone called erythropoietin (EPO), 5 which produces red blood cells. Damaged kidneys may not generate this hormone, resulting in fewer red blood cells to deliver oxygen.";
    }else if (input == "What drugs are harmful to the kidneys?") {
        return "All drugs pass through the kidneys. In particular, pain medications, antibiotics, prescription laxatives and contrast dye can reduce blood flow to the organs. Make sure you follow the instructions of your healthcare provider to prevent injury to the kidneys.";
    }else if (input == "How can I protect my kidneys if I take medicines to treat a health condition?") {
        return "If you have chronic pain, consult a doctor and do not use over-the-counter pain relievers for more than 10 days. The same is true if you have a fever for more than three days.";
    }else if (input == "What foods should I avoid for my kidney health?") {
        return "If you have kidney disease, consult with a renal dietitian for advice on how to support your nutritional needs. But in general, avoid foods that are high in sodium. Too much sodium can cause high blood pressure and therefore bad for your kidneys. When the kidneys cannot remove excess salt and fluid from the body, you may see swelling in your legs and around your eyes.";
    }else if (input == "How does my doctor know I need to have dialysis or get a transplant?") {
        return "Most people do not know that kidney function can be assessed with a simple blood test. Chances are you have had your kidney function tested during routine blood work. ";
    }
    
    

    


    // Personal responses
    if (input == "Hi") {
        return "Hi";
    } else if (input == "Hello!") {
        return "Hai!, How are you doing?";
    } else if (input == "Hi!") {
        return "Hi, How are you doing?";
    }  else if (input == "I'm doing great.") {
        return "That is good to hear.";
    } else if (input == "Thank you") {
        return "You're welcome.";
    } else if (input == "Are you a robot?") {
        return "Yes, My name is AtoK_ChatBot";
    } else if (input == "Are you a bot?") {
        return "Yes, My name is AtoK_ChatBot";
    } else if (input == "Are you a chatbot?") {
        return "Yes, My name is AtoK_ChatBot";
    } else if (input == "Are you real?!") {
        return "I am a ChatBot, My name is AtoK_ChatBot";
    } else if (input == "What is your name?") {
        return "My name is AtoK_ChatBot";
    } else if (input == "Who made you?") {
        return "Mothukuri RajeshKumar made me";
    } else if (input == "What do you do?") {
        return "I am made to give Ayush to Kidney(AtoK) Information about how to extend life of Kidney";
    } else {
        return "Try asking something else!";
    }


    
}