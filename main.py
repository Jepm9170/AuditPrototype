
#patient sex
Sex= input('M or F: ');
sex= Sex.lower();

#patient age
age = int(input('Age: '));

#smoker
Smoke= input('Smokes? Y or N: ');
smoke= Smoke.lower();

havesmoked= input('Have smoked in last 15 yrs? Y or N: ');
havesmoekd= havesmoked.lower();


#diabetes

diabetes= input('Diabetes? Y or N: ');
diabetes= diabetes.lower();

#bmi

bmi = float(input('Bmi: '));

#Sexually active
Sexact = input('Sexually active in the past 12 months? Y or N: ');
sexact = Sexact.lower();

if sexact == 'y':
    partners=input('More than 1? Y or N: ')

#Federal
federal= input('federal? Y or N: ');
federal= federal.lower();

#Banco Popoular

banco=input("Banco popular? Y or N: ");
banco= banco.lower();

if banco =='y':
    BPdependant=input('Principal or dependant? P or D: ')

##Tests FUNCTIONS AND VARIABLES
testrequired=0;
testsdone=0;
testsNotDone=0;

#HIV Test#####################
def HIVTEST (age):
    if age < 66:
        return 1;
    else:
        return 0;


HIVresult= HIVTEST(age);

if HIVresult == 1:
    testrequired = testrequired+1;


#Hepatisis C##################

def HepatisisC (age):
    if age < 80:
        return 1;
    else:
        return 0;

HepaCresult= HepatisisC (age);

if HepaCresult == 1:
    testrequired = testrequired + 1;


##Fasting Blood Sugar############

def FastBlood (age, bmi):
    if age > 34 and bmi > 24.99:
        return 1;
    else:
        return 0;

fastblood= FastBlood(age,bmi);

if fastblood == 1:
    testrequired = testrequired + 1;

#####Diabetes only#####

def A1cbloodtest (diabetes):
    if diabetes== 'y':
        return 1;
    else:
        return 0;

a1cblood=A1cbloodtest(diabetes);

if a1cblood==1:
    testrequired = testrequired+1;


def MicroalbuminTest (diabetes):
    if diabetes== 'y':
        return 1;
    else:
        return 0;

microalbumin=MicroalbuminTest(diabetes);
if microalbumin==1:
    testrequired = testrequired+1;

def FundoscopyeyeTest (diabetes):
    if diabetes == 'y':
        return 1;
    else:
        return 0;

fundoresult=FundoscopyeyeTest(diabetes);
if fundoresult==1:
    testrequired = testrequired+1;

##PROGRAM START MAIN
print(' ')
print(f' TOTAL TEST REQUIRED: {testrequired} ')

HIVTEST(age);

HepatisisC(age);

FastBlood(age,bmi);

A1cbloodtest(diabetes);

MicroalbuminTest(diabetes);

FundoscopyeyeTest(diabetes);

if HIVresult == 1:
    print('HIV TEST ');


if HepaCresult == 1:
    print('Hepatisis C TEST ');


if fastblood == 1:
    print('Fasting Blood Sugar TEST ');

if a1cblood==1:
    print('A1C BLOOD TEST');

if microalbumin==1:
    print('Microalbumin TEST');

if fundoresult==1:
    print('Fundoscopy Eye TEST')



###HIV TEST CHOICE
print(' ');
if HIVresult == 1:
    hivdone=input(' HIV TEST Done? Y or N: ');
    hivdone= hivdone.lower();
    if hivdone == 'y':
        testsdone= testsdone+1;
    else:
        testsNotDone = testsNotDone+1;

####HEPATISIS TEST CHOICE
if HepaCresult == 1:
    hepatisisdone = input('Hepatisis C Test Done? Y or N: ');
    hepatisisdone = hepatisisdone.lower();
    if hepatisisdone == 'y':
        testsdone = testsdone + 1;
    else:
        testsNotDone = testsNotDone + 1;

####Fast Blood Choice
if fastblood == 1:
    fastdone = input('Fast Blood sugar test Done? Y or N: ');
    fastdone = fastdone.lower();
    if fastdone == 'y':
        testsdone = testsdone + 1;
    else:
        testsNotDone = testsNotDone + 1;

#####A1C CHOICE#####
if a1cblood==1:
    a1cdone = input('A1C Blood Test Done? Y or N: ');
    a1cdone = a1cdone.lower();
    if a1cdone == 'y':
        testsdone = testsdone + 1;
    else:
        testsNotDone = testsNotDone + 1;

#####Microalbumin choice######

if microalbumin==1:
    microdone = input('Microalbumin Test Done? Y or N: ');
    microdone = microdone.lower();
    if microdone == 'y':
        testsdone = testsdone + 1;
    else:
        testsNotDone = testsNotDone + 1;

####Fundoscopy eye test choice#####

if fundoresult==1:
    fundodone = input('Fundoscopy Eye Test Done? Y or N: ');
    fundodone = fundodone.lower();
    if fundodone == 'y':
        testsdone = testsdone + 1;
    else:
        testsNotDone = testsNotDone + 1;





print(f'Total Test Done: {testsdone}')
FinalTest= (testsdone/testrequired) *100;

print(f'Compliance percentage: {FinalTest} %');


















