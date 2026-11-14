1. Basics of Artificial Intelligence and Machine Learning
Artificial Intelligence (AI) is the ability of a machine to perform tasks that normally need
human intelligence, such as understanding language, recognizing images, solving
problems and making decisions.
Machine Learning (ML) is a part of AI where a computer learns patterns from data
instead of being given fixed rules. The more good data it sees, the better it gets.
Types of Machine Learning
1. Supervised learning: learns from labeled data (input with the correct answer).
Examples: spam detection, house price prediction, disease classification.
2. Unsupervised learning: finds patterns in unlabeled data. Examples: customer
segmentation, grouping similar news articles.
3. Reinforcement learning: an agent learns by trial and error and gets rewards or
penalties. Examples: game-playing AI, robotics, self-driving systems.
Basic ML Workflow
1. Collect data
2. Clean and prepare data
3. Split into training and testing sets
4. Train a model
5. Evaluate it on test data
6. Improve and deploy
Key Terms
Dataset: the collection of data used to train and test.
Feature: an input variable (e.g., house size).
Label: the output we want to predict (e.g., house price).
Model: the learned pattern or function that makes predictions.
Training: the process of the model learning from data.
Overfitting: the model memorizes training data and performs badly on new data.
Page 1 of 6
AI & ML Internship: Week 1 Learning Notes
2. AI vs. Machine Learning vs. Deep Learning
AI
Machine Learning
Deep Learning
Meaning
Scope
Data
needed
Example
Making machines
act intelligently
Broadest
Varies
Machines learn from
data
Subset of AI
ML using multi-layer neural
networks
Subset of ML
Moderate
Chatbot, rule-based
expert system
Recommendation
engine, spam filter
Very large
Face recognition, speech
recognition, language
models
Remember: Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence (nested circles).
Neural network in one line: layers of connected "neurons" that pass numbers forward,
adjusting their weights during training to reduce errors.
3. Real-World AI Applications
Healthcare: detecting diseases from X-rays and scans, drug discovery.
Finance: fraud detection, credit scoring, stock trend analysis.
E-commerce: product recommendations on Amazon and Flipkart.
Entertainment: Netflix and Spotify suggestions, content creation.
Transport: self-driving cars, traffic prediction, route optimization on Google Maps.
Agriculture: crop disease detection, yield prediction, smart irrigation.
Education: personalized learning, automated grading.
Daily life: voice assistants (Siri, Alexa, Google Assistant), face unlock, Google
Translate, email spam filters.
How to explain one in an answer: state the problem, say what data the AI uses, and
describe the benefit. Example: Netflix has millions of titles and users cannot browse all of
them. It uses your watch history to predict what you will enjoy, which saves time and keeps
users engaged.
4. Installing Python
1. Go to python.org and download the latest stable version.
2. Run the installer. On Windows, tick Add Python to PATH.
Page 2 of 6
AI & ML Internship: Week 1 Learning Notes
3. Open a terminal or command prompt and run 
python --version to verify.
4. Use an editor such as VS Code or IDLE, or use Google Colab to code in the browser
with no setup.
5. Run a file with 
python filename.py .
5. Python Programming Basics
Variables and Data Types
A variable stores a value. Python figures out the type automatically.
name = "Raviteja"     
age = 21              
height = 5.9          
is_student = True     
print(name, age)
print(type(age))
# str
# int
# float
# bool
Operators
Arithmetic: 
+ - * / // % **
Comparison: 
== != > < >= <=
Logical: 
and or not
Input and Output
name = input("Enter your name: ")
print("Hello,", name)
input() always returns a string, so use 
Conditions
marks = 72
if marks >= 90:
print("A")
elif marks >= 60:
print("B")
else:
print("C")
int() or 
float() to convert numbers.
Page 3 of 6
AI & ML Internship: Week 1 Learning Notes
Loops
# for loop
for i in range(1, 6):
print(i)
# while loop
count = 1
while count <= 3:
print(count)
count += 1
Use 
break to exit a loop early and 
Lists
continue to skip to the next round.
A list is an ordered, changeable collection.
skills = ["Python", "ML", "SQL"]
skills.append("Deep Learning")   # add
skills.remove("SQL")             
# remove
print(skills[0])                 
print(len(skills))               
for s in skills:
print(s)
Functions
A function is a reusable block of code.
def add(a, b):
return a + b
print(add(3, 4))   # 7
# first item
# length
6. Beginner Programs to Practice
# 1. Even or odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")
# 2. Multiplication table
n = int(input("Table of: "))
for i in range(1, 11):
Page 4 of 6
AI & ML Internship: Week 1 Learning Notes
print(f"{n} x {i} = {n*i}")
# 3. Largest number in a list
nums = [4, 19, 7, 33, 2]
print("Largest:", max(nums))
# 4. Reverse a string
print("Machine Learning"[::-1])
# 5. Factorial
def factorial(n):
result = 1
for i in range(1, n + 1):
result *= i
return result
print(factorial(5))
# 6. Simple calculator
def calculate(a, b, op):
if op == "+": return a + b
if op == "-": return a - b
if op == "*": return a * b
if op == "/": return a / b if b != 0 else "Cannot divide by zero"
print(calculate(10, 5, "*"))
7. Quick Revision Points
AI is the goal, ML is the method, Deep Learning is a powerful technique within ML.
ML learns from data; supervised uses labels, unsupervised does not, reinforcement
uses rewards.
Good data matters more than complex models.
Python is popular for AI because it is simple and has libraries like NumPy, pandas,
scikit-learn, TensorFlow and PyTorch.
Practice by typing the code yourself, not just reading it.
8. Self-Check Questions
1. What is the difference between AI, ML and Deep Learning?
2. Name the three types of machine learning with one example each.
3. What is overfitting?
4. Give three real-world AI applications and explain one in detail.
Page 5 of 6
AI & ML Internship: Week 1 Learning Notes
5. What does 
range(1, 6) produce?
6. What is the difference between a list and a variable?
7. Why do we use functions?
Page 6 of 6# codomax-ai-ml-internship-2026
“Learning notes and Python programs from my AI &amp; ML internship at Codomax”
