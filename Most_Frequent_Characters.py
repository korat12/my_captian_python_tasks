def most_frequent(string):
    freq = {}

    for char in string:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_freq:
        print(f"{char} = {count:02d}", end=" ")

# Input from user
s = input("Please enter a string ")
most_frequent(s)
