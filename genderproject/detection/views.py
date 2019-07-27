from django.shortcuts import render
import random

#nltk.download('names')
from nltk.corpus import names
import nltk
from .set import training_set
# Create your views here.
from django.http import HttpResponse


def feature(word):
    return {'last_letter': word[-1]}
# making list to contain our training set
#training_set = ([(name, 'male') for name in names.words('male.txt')] +[(name, 'female') for name in names.words('female.txt')])

random.shuffle(training_set)

# Process the data
featuresets = [(feature(n), gender)
               for (n, gender) in training_set]

# Learning Process and get percentage for every char whether male or female
train_set, test_set = featuresets[500:], featuresets[:500]
#Get our Data Ready
classifier = nltk.NaiveBayesClassifier.train(train_set)



def home(request):
    if request.method == 'GET': #if nothing in input so show our page without result section
        return render(request,'detect.html')
    else: #when request.method == 'POST' so we have input
        name = request.POST['name'] #getting the input data from our html
        result = classifier.classify(feature(name)) #male or female
        truewith = nltk.classify.accuracy(classifier, train_set) * 100 #getting the percentage of accurancy
        percent = "%8.2f" % (truewith) #get 4 digits xx.xx
        context = {
            'result':result,
            'name':name,
            'percent':percent
        }
        print(classifier.show_most_informative_features(5))
        return render(request,'detect.html',context)