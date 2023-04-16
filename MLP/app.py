import torch
import openai
from MLP import MLP
from flask import Flask, request
openai.api_key = "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"






# One hot mapping
def one_hot(map_, num_cls, v):
    if type(v) != list:
        v = [v]
    v = torch.tensor([map_[i] for i in v])
    v_ = torch.zeros((v.shape[0], num_cls + 1))
    v_[torch.arange(v.shape[0]), v] = 1
    return v_

# Convert the variables to a vector
def vars_to_vec(Age, Income, Gender, Married, Education, Past_Accidents, Has_Children, Has_Sports_Car, Vehicle_Year):
    # Age
    if Age > 0:
        if Age <= 25:
            Age = "16-25"
        elif Age <= 39:
            Age = "26-39"
        elif Age <= 64:
            Age = "40-64"
        else:
            Age = "65+"
    else:
        Age = "NA"
    map_ = {"16-25":0, "26-39":1, "40-64":2, "65+":3, "NA":4}
    Age_oh = one_hot(map_, 4, Age)
    Age_oh[Age_oh[:, -1] == 1] *= 0
    Age = Age_oh[:, :-1]
            
    # Income
    if Income >= 0:
        if Income < 35_800:
            Income = "poverty"
        elif Income < 52_200:
            Income = "working class"
        elif Income < 156_600:
            Income = "middle class"
        else:
            Income = "upper class"
    else:
        Income = "NA"
    map_ = {"poverty":0, "working class":1, "middle class":2, "upper class":3, "NA":4}
    Income_oh = one_hot(map_, 4, Income)
    Income_oh[Income_oh[:, -1] == 1] *= 0
    Income = Income_oh[:, :-1]
    
    # Gender
    map_ = {"female":0, "male":1, "NA":2}
    Gender_oh = one_hot(map_, 2, Gender)
    Gender_oh[Gender_oh[:, -1] == 1] *= 0
    Gender = Gender_oh[:, :-1]
    
    # Married
    map_ = {"False":0, "True":1, "NA":2}
    Married_oh = one_hot(map_, 2, Married)
    Married_oh[Married_oh[:, -1] == 1] *= 0
    Married = Married_oh[:, :-1]
    
    # Education
    map_ = {"NA":0, "HS":1, "B":2, "BA":2, "BS":2, "M":3, "MA":3, "MS":3, "PHD":4}
    Education = one_hot(map_, 4, Education)
    
    # Past_Accidents
    Past_Accidents = torch.tensor([[Past_Accidents]])/15
    
    # Has_Children
    map_ = {"No":0, "Yes":1, "NA":2}
    Has_Children_oh = one_hot(map_, 2, Has_Children)
    Has_Children_oh[Has_Children_oh[:, -1] == 1] *= 0
    Has_Children = Has_Children_oh[:, :-1]
    
    # Has_Sports_Car
    map_ = {"No":0, "Yes":1, "NA":2}
    Has_Sports_Car_oh = one_hot(map_, 2, Has_Sports_Car)
    Has_Sports_Car_oh[Has_Sports_Car_oh[:, -1] == 1] *= 0
    Has_Sports_Car = Has_Sports_Car_oh[:, :-1]
    
    # Vehicle_Year
    if Vehicle_Year > 2000:
        if Vehicle_Year < 2015:
            Vehicle_Year = "before 2015"
        else:
            Vehicle_Year = "before 2015"
    else:
        Vehicle_Year = "NA"
    map_ = {"before 2015":0, "after 2015":1, "NA":2}
    Vehicle_Year_oh = one_hot(map_, 2, Vehicle_Year)
    Vehicle_Year_oh[Vehicle_Year_oh[:, -1] == 1] *= 0
    Vehicle_Year = Vehicle_Year_oh[:, :-1]
    
    
    return torch.cat((Age, Income, Gender, Married, Education, Past_Accidents,
                      Has_Children, Has_Sports_Car, Vehicle_Year), axis=-1)
















age = "39"
income = "13M"
gender = "male"
married = "not married"
education = "Masters in Biology"
past_accidents = "0"
children = "no"
sports_car = "Jeep"
vehicle_year = "from 2010"

prompt_1 = f"""I'm a {age}-year-old {gender} who earns {income} annually. I'm {married}, have a {education} degree, and my prior accident history consists of {past_accidents} accidents. I have {children} children, drive a {sports_car}, and the vehicle is {vehicle_year} years old. Can I claim my case with an insurance company?
Age: {age}
Income: 13000000
Gender (male/female/NA): male
Married (False/True/NA): False
Education (NA/HS/B/M/PHD): M
Past Accidents: 0
Children (No/Yes/NA): No
Sports Car (No/Yes/NA): No
Vehicle Year (20xx/NA): 2011"""



income = "41,849"
gender = "Male"
education = "High School"
past_accidents = "3"
children = "have"
sports_car = "Masda"
vehicle_year = "11"

prompt_2 = f"""Hello! I would like to know if my case can be claimed by insurance. I'm {gender}, and have an annual income of {income}. I possess a {education} education. I've had {past_accidents} accidents, and I {children} children. I drive a {sports_car} that is from {vehicle_year}. Is my case eligible for a claim?
Age: NA
Income: 41849
Gender (male/female/NA): male
Married (False/True/NA): False
Education (NA/HS/B/M/PHD): HS
Past Accidents: 3
Children (No/Yes/NA): No
Sports Car (No/Yes/NA): No
Vehicle Year (20xx/NA): 2011"""




age = "37"
income = "$$$11,891"
gender = "girl"
married = "not married"
education = "dropped out of high school"
past_accidents = "1"
children = "2"
sports_car = "Ford"

prompt_3 = f"""Can you please help me determine if my circumstances qualify for an insurance claim? I'm a {gender} of {age} years. I'm {married} and {education}. Additionally, I've been involved in {past_accidents} past accidents, have {children} children, and my car is a {sports_car}.
Age: {age}
Income: 11891
Gender (male/female/NA): female
Married (False/True/NA): False
Education (NA/HS/B/M/PHD): NA
Past Accidents: 1
Children (No/Yes/NA): Yes
Sports Car (No/Yes/NA): No
Vehicle Year (20xx/NA): NA"""




age = "26"
income = "54K"
gender = "Female"
married = "I am divorced"
education = "PHD"
past_accidents = "1"
children = "1"
sports_car = "Ferrari"
vehicle_year = "13"

prompt_4 = f"""I'd appreciate assistance in learning if I can claim my case with an insurance company. My information includes: {age} years old, {gender}, {income} annual income, {married} marital status, {education} education level, {past_accidents} previous accidents, {children} child, {sports_car} car model, and a {vehicle_year}-year-old vehicle.
Age: {age}
Income: 54000
Gender (male/female/NA): female
Married (False/True/NA): False
Education (NA/HS/B/M/PHD): PHD
Past Accidents: 1
Children (No/Yes/NA): Yes
Sports Car (No/Yes/NA): Yes
Vehicle Year (20xx/NA): 2010"""




age = "91"
income = "61 ,197 ,6 30"
gender = "MALE"
married = "Currently married"
education = "Bachelors"
past_accidents = "3"
children = "6"
sports_car = "Honda Civic"
vehicle_year = "10"

prompt_5 = f"""I need to know if my personal situation is eligible for an insurance claim. Here are some details about me: {age} years old, {gender}, {income} yearly income, {married} marital status, {education} level of education, a history of {past_accidents} accidents, {children} children, and I drive a {sports_car} that has been in use for {vehicle_year} years.
Age: {age}
Income: 13000000
Gender (male/female/NA): {gender}
Married (False/True/NA): False
Education (NA/HS/B/M/PHD): B
Past Accidents: 0
Children (No/Yes/NA): No
Sports Car (No/Yes/NA): No
Vehicle Year (20xx/NA): 2013"""



















global model
model = None

# create the Flask app
app = Flask(__name__)



@app.route('/load', methods=['GET', 'POST'])
def load():
    global model
    model = MLP()
    model.load_state_dict(torch.load("model.pt"))
    model.eval()
    
    return {}




@app.route('/data',methods = ['POST', 'GET'])
def main(text="I am a male with 200,000 dollars. Who got divoriced, but is educated with a BA. I have no kids, and I drive a 2010 Honda Civic."):
    # Create a prompt
    prompt = f"""
        It is currently the year 2023. Pull information from the prompts.

        {prompt_1}

        {prompt_2}

        {prompt_3}

        {prompt_4}

        {prompt_5}

        {text}"""
        
    # Generate a completion
    messages = openai.ChatCompletion.create(
        model="gpt-4",
        # model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "It is currently the year 2023. Pull information from the prompts."},
                {"role": "user", "content": f"{prompt}\nAge:"},
            ]
    )["choices"][0]["message"]["content"].split("\n")
    
    # Extract the information from the text
    Age = messages[0]
    Income = messages[1].split(" ")[-1]
    Gender = messages[2].split(" ")[-1]
    Married = messages[3].split(" ")[-1]
    Education = messages[4].split(" ")[-1]
    Past_Accidents = messages[5].split(" ")[-1]
    Has_Children = messages[6].split(" ")[-1]
    Has_Sports_Car = messages[7].split(" ")[-1]
    Vehicle_Year = messages[8].split(" ")[-1]
    
    # Convert to integers
    Age = int(Age) if Age != "NA" else -1
    Income = int(Income) if Income != "NA" else -1
    try:
        Past_Accidents = int(Past_Accidents) if type(Past_Accidents) != "NA" else 0
    except:
        Past_Accidents = 0
    try:
        Vehicle_Year = int(Vehicle_Year) if Vehicle_Year != "NA" else -1
    except:
        Vehicle_Year = -1
    
    # Create the vector from the variables
    vec = vars_to_vec(Age, Income, Gender, Married, Education, Past_Accidents, Has_Children, Has_Sports_Car, Vehicle_Year)
    
    # Predict the outcome
    print(vec)
    out = model(vec)
    
    return {"data": out.cpu().detach().item()}










if __name__ == "__main__":
    load()
    app.run(debug=True, port=5001)
    
    # out = script("I am a male with 200,000 dollars. Who got divoriced, but is educated with a BA. I have no kids, and I drive a 2010 Honda Civic.")
    
    # print(out["data"])