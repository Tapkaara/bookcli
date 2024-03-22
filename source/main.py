

def countLetters(text):
    lowered = text.lower()

    charMap = {}

    for char in lowered:
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1

    return charMap

def countWords(text):
    words = text.split()
    return len(words)

def buildReport(wordCount, charCounts, bookPath):
    report = f"--- Begin report of {bookPath} ---\n\n"
    report += f"{wordCount} words found in the document.\n"

    charTuples = []

    for key, value in charCounts.items():
        if key.isalpha():
            charTuples.append((key, value))

    charTuples.sort(reverse = True, key = lambda tup: tup[1])
    
    for tup in charTuples:
        report += f"The '{tup[0]}' character was found {tup[1]} times.\n"

    report += "--- End report ---"

    return report

def main():
    bookPath = "./books/frankenstein.txt" 
    with open(bookPath, "r") as f:
        contents = f.read()
        wordCount = countWords(contents)
        charCounts = countLetters(contents)
        print(buildReport(wordCount, charCounts, bookPath))

main()
