# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
    
# Task 3
def calc (a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                result = a + b
            case "subtract":
                result = a - b
            case "multiply":
                result = a * b
            case "divide":
                result = a / b
            case "modulo":
                result = a % b
            case "int_divide":
                result = a // b
            case "power":
                result = a ** b
            case _:
                result = "Unknown operation"
        return result
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc("a", "b", "multiply"))
print(calc(2, 2))                 
print(calc(2, 3, "add"))
print(calc(7, 0, "divide"))

# Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "int":
                result = int(value)
            case "float":
                result = float(value)
            case "str":
                result = str(value)
        return result
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {type}."
    
print(data_type_conversion(4.2, "int"))
print(data_type_conversion("nonsense", "float"))

# Task 5
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except (ValueError, TypeError, ZeroDivisionError):
        return "Invalid data was provided."

print(grade(68, 91, 78))

# Task 6
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return(result)
print(repeat("Hi", 5))

# Task 7
def student_scores(mode,**kwargs):
       if mode.upper() == "BEST":
            best_score = list(kwargs.values())[0]
            best_name = list(kwargs.keys())[0]      
            for name, score in kwargs.items():
                if score > best_score:
                    best_score = score
                    best_name = name
            return best_name
       elif mode.upper() == "MEAN":
            total = sum(kwargs.values())
            count = len(kwargs)
            return total/count


print(student_scores("Mean", Rida = 92, Waheed = 77, Kishwar = 65, Jameel = 52))
print(student_scores("Best", Rida=92, Waheed=77, Kishwar=65, Jameel=52))

# Task 8
def titleize (sentence):
    words = sentence.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    final_list = []
    for i, word in enumerate(words):
        if i ==0:
            first_word = word.capitalize()
            final_list.append(first_word)
        elif i == len(words)-1:
            last_word = word.capitalize()
            final_list.append(last_word)
        elif word in little_words:
            small = word.lower()
            final_list.append(small)
        else:
            remaining = word.capitalize()
            final_list.append(remaining)
    return ' '.join(final_list)

print(titleize("hi my name is sadia"))
print(titleize("i am a fan of stranger things"))
                        
# Task 9
def hangman(secret, guess):
    final_guess = []
    for letter in secret:
        if letter in guess:
            result = final_guess.append(letter)
        else:
            result = final_guess.append("_")
    return "".join(final_guess)

print(hangman("cookie", "oo"))

# Task 10
def pig_latin(string):
    vowels = ["a", "e", "i", "o", "u"]
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            index = 0
            while index < len(word):
                if word[index] in vowels:
                    break
                if word[index] == "q" and index + 1 < len(word) and word[index + 1] == "u":
                    index += 2
                    break
                index += 1

            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)

print(pig_latin("queen love quails"))
print(pig_latin("california is pretty"))
