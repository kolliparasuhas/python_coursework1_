def get_questions():
    return [
        {
            "question": "What is the result of 10 // 3 in Python?",
            "options": {"a": "3.33", "b": "3", "c": "4", "d": "Error"},
            "answer": "b",
        },
        {
            "question": "Which data type can store multiple items and is mutable?",
            "options": {"a": "List", "b": "Tuple", "c": "String", "d": "Integer"},
            "answer": "a",
        },
        {
            "question": "What keyword is used to define a loop that iterates over a sequence?",
            "options": {"a": "while", "b": "loop", "c": "iterate", "d": "for"},
            "answer": "d",
        },
        {
            "question": "Which of the following is a valid variable name?",
            "options": {"a": "1var", "b": "var_name", "c": "var-name", "d": "def"},
            "answer": "b",
        },
        {
            "question": "What is the output of bool(0)?",
            "options": {"a": "True", "b": "False", "c": "0", "d": "None"},
            "answer": "b",
        },
        {
            "question": "Which statement is used to stop a loop early?",
            "options": {"a": "exit", "b": "end", "c": "break", "d": "stop"},
            "answer": "c",
        },
        {
            "question": "What is the keyword used to handle exceptions?",
            "options": {"a": "catch", "b": "try", "c": "trap", "d": "except"},
            "answer": "d",
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": {"a": ".py", "b": ".pt", "c": ".python", "d": ".p"},
            "answer": "a",
        },
        {
            "question": "Which function converts an integer to a string?",
            "options": {"a": "int()", "b": "str()", "c": "float()", "d": "chr()"},
            "answer": "b",
        },
        {
            "question": "Which built-in function returns the absolute value?",
            "options": {"a": "abs()", "b": "absolute()", "c": "fabs()", "d": "val()"},
            "answer": "a",
        },
        {
            "question": "Which keyword creates an object from a class?",
            "options": {"a": "class", "b": "define", "c": "create", "d": "None of these"},
            "answer": "d",  
        },
        {
            "question": "Which operator is used for floor division?",
            "options": {"a": "/", "b": "//", "c": "%", "d": "**"},
            "answer": "b",
        },
        {
            "question": "What does the input() function return?",
            "options": {"a": "int", "b": "str", "c": "bool", "d": "float"},
            "answer": "b",
        },
        {
            "question": "Which method adds an element to the end of a list?",
            "options": {"a": "append()", "b": "insert()", "c": "add()", "d": "push()"},
            "answer": "a",
        },
        {
            "question": "How do you create a comment in Python?",
            "options": {"a": "# comment", "b": "// comment", "c": "<!-- comment -->", "d": "/* comment */"},
            "answer": "a",
        },
        {
            "question": "Which module is used for generating random numbers?",
            "options": {"a": "random", "b": "rand", "c": "math", "d": "numbers"},
            "answer": "a",
        },
        {
            "question": "What is the output of 3 * 'ab'?",
            "options": {"a": "ababab", "b": "ab3", "c": "ab ab ab", "d": "Error"},
            "answer": "a",
        },
        {
            "question": "What does 'is' compare in Python?",
            "options": {"a": "Value", "b": "Type", "c": "Memory location", "d": "All of the above"},
            "answer": "c",
        },
        {
            "question": "Which keyword is used to define a function?",
            "options": {"a": "function", "b": "def", "c": "define", "d": "fun"},
            "answer": "b",
        },
        {
            "question": "Which method removes all items from a list?",
            "options": {"a": "remove()", "b": "delete()", "c": "clear()", "d": "empty()"},
            "answer": "c",
        },
    ]

def ask_question(q, num):
    print(f"\nQuestion {num + 1}: {q['question']}")
    for key in sorted(q["options"]):
        print(f"    {key}) {q['options'][key]}")
    while True:
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer in q["options"]:
            return answer == q["answer"]
        else:
            print("Invalid input. Please enter a, b, c, or d.")

def run_quiz():
    questions = get_questions()
    score = 0
    print("\nWelcome to the Python Interview Prep Quiz!\n")
    for i, q in enumerate(questions):
        if ask_question(q, i):
            print("Correct!\n")
            score += 1
        else:
            correct_option = q['answer']
            correct_text = q['options'][correct_option]
            print(f"Wrong! The correct answer was '{correct_option}) {correct_text}'.\n")
    percentage = (score / len(questions)) * 100
    print(f"Quiz Over! Your Score: {score}/{len(questions)}")
    print(f"Your Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    run_quiz()

