from collections import defaultdict

#create a default dict to store patient responses
# an empty list means an answer has not been given yet
#(defaultdict avoids the need for avoiding key errors in the code)
patient = defaultdict(list)

def question(query):
    """asks for a user response and returns True or False"""
    #First check if query has already been asked
    if len(patient[query])>0:
        return patient[query][0]
    #if it is a new question, then ask for an answer, store answer and return
    print(query)
    answer = input('Y/N\n>')
    if answer.lower() == 'y':
        patient[query].append(True)
        return True
    elif answer.lower()=='n':
        patient[query].append(False)
        return False
    else:
        print("I'm sorry I didn't understand your answer")
        return question(query)

def or_question(*args):
    #check if any questions answered to save going through one by one
    for arg in args:
        if len(patient[q(arg)])>0 and patient[q(arg)][0]== True:
            return True
    for arg in args:
        if question(q(arg)):
            return True
    return False

def q(symptom):
    """Converts a symptom into a question"""
    return "Does the patient have " + symptom + "?"


def acquire_age():
    try:
        patient['age'] = int(input('How old is the patient?\n>'))
    except:
        acquire_age()
    def confirm_age():
        answer = input('Confirm patient is %s (Y/N)\n>'%(patient['age']))
        if answer.lower() == 'y':
            pass
        elif answer.lower() == 'n':
            acquire_age()
        else:
            confirm_age()
    confirm_age()


# Oesophageal Cancer -----------------------------
acquire_age()

if question(q('dysphagia')) or (
patient['age'] >= 55 and question(q('weight loss')) and (
    or_question('upper abdominal pain', 'reflux', 'dyspepsia')
)):
    print("Offer urgent direct access upper gastrointestinal endoscopy\
 (to be performed within 2 weeks) to assess for oesophageal cancer")

elif question(q('haematemesis')) or\
(patient['age'] >= 55 and \
    ((question(q('dyspepsia')) and question('Has dyspepsia treatment failed?'))or\
    or_question('upper abdominal pain', 'low haemoglobin levels') or\
    (question(q('raised platelet count')) and (
        or_question('nausea','vomiting','weight loss','reflux','dyspepsia','upper abdominal pain'))or
    (or_question('nausea','vomiting')and(
        or_question('weight loss','reflux','dyspepsia','upper abdominal pain')
    ))
    ))):
    print("Consider non-urgent direct access upper gastrointestinal\
 endoscopy to assess for oesophageal cancer")

# Pancreatic cancer-------------------------------------------------

elif patient['age']>40 and question(q('jaundice')):
    print('Refer  using a suspected cancer pathway referral (for an appointment",\
    "within 2 weeks) for pancreatic cancer')

elif patient['age']>=60 and question(q('weight loss')) and\
    or_question('diarrhoea','back pain','abdominal pain','nausea','vomiting',\
    'constipation','new‑onset diabetes'):
    print("Consider an urgent direct access CT scan (to be performed within 2 weeks),",\
    "or an urgent ultrasound scan if CT is not available, to assess for pancreatic cancer ")

#Stomach Cancer ---------------------------------------------------
elif question(q('an upper abdominal mass?')):
    if question('Is it consistent with stomach cancer?'):
        print("Consider a suspected cancer pathway referral (for an appointment ",\
        "within 2 weeks)")
#------ Gall badder and liver cancer-----------------
    elif question("Is it consistent with an enlarge liver or gall bladder?"):
        print("Consider an urgent direct access ultrasound scan (to be performed",\
        "within 2 weeks) to assess for gall bladder or liver cance")
#Stomach cancer ----------------------------------------------------
elif question(q('dysphagia')) or (patient['age']>=55 and question(q('weight loss')) and(
    or_question('upper abdominal pain','reflux','dyspepsia')
)):
    print("Offer urgent direct access upper gastrointestinal endoscopy ",\
    "(to be performed within 2 weeks) to assess for stomach cancer")

elif patient['age']>=55 and (question(q('dyspepsia')) and question('Has dyspepsia treatment failed?')or\
    (question(q('upper abdominal pain')) and question(q('low haemoglobin levels')))or\
    (question(q('raised platelet count')) and\
     or_question('nausea','vomiting','weight loss','reflux','dyspepsia','upper abdominal pain'))or\
     ((or_question('nausea','vomiting')) and\
     or_question('weight loss','reflux','dyspepsia','upper abdominal pain'))):
    print("Consider non‑urgent direct access upper gastrointestinal endoscopy",\
    "to assess for stomach cancer ")

else:  print("Referral not required")
