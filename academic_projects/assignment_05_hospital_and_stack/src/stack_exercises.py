class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def removeDuplicates(numbers_stack):
    seen = []
    temp_stack = Stack()
    result_stack = Stack()

    while not numbers_stack.is_empty():
        current = numbers_stack.pop()
        temp_stack.push(current)

    while not temp_stack.is_empty():
        current = temp_stack.pop()
        if current not in seen:
            seen.append(current)
            result_stack.push(current)

    return result_stack


def findUnmatch(parentheses_string):
    stack = Stack()

    for char in parentheses_string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.is_empty():
                return ")"
            stack.pop()

    if not stack.is_empty():
        return "("

    return None


def equalStacks(stack1, stack2):
    if stack1.size() != stack2.size():
        return False

    temp_stack1 = Stack()
    temp_stack2 = Stack()
    values1 = []
    values2 = []

    while not stack1.is_empty():
        value = stack1.pop()
        values1.append(value)
        temp_stack1.push(value)

    while not stack2.is_empty():
        value = stack2.pop()
        values2.append(value)
        temp_stack2.push(value)

    while not temp_stack1.is_empty():
        stack1.push(temp_stack1.pop())

    while not temp_stack2.is_empty():
        stack2.push(temp_stack2.pop())

    return sorted(values1) == sorted(values2)


def compressStr(text):
    if text == "":
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1]
            if count > 1:
                result += str(count)
            count = 1

    result += text[-1]
    if count > 1:
        result += str(count)

    return result


def reverseSentence(sentence):
    words = sentence.split(" ")
    result = []

    for word in words:
        stack = Stack()

        for char in word:
            stack.push(char)

        reversed_word = ""
        while not stack.is_empty():
            reversed_word += stack.pop()

        result.append(reversed_word)

    return " ".join(result)


def run_stack_examples():
    stack_numbers = Stack()
    stack_numbers.push(1)
    stack_numbers.push(2)
    stack_numbers.push(2)
    stack_numbers.push(3)
    stack_numbers.push(1)

    result_stack = removeDuplicates(stack_numbers)
    while not result_stack.is_empty():
        print(result_stack.pop())

    print(findUnmatch("(()))"))
    print(findUnmatch("((())"))
    print(findUnmatch("(())"))

    stack1 = Stack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)

    stack2 = Stack()
    stack2.push(3)
    stack2.push(1)
    stack2.push(2)

    print(equalStacks(stack1, stack2))

    print(compressStr("aabbbcc"))
    print(compressStr("abbcbb"))

    print(reverseSentence("hello world!"))


if __name__ == "__main__":
    run_stack_examples()
