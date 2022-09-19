

def main():
    new_say = shorten(input())
    print(new_say)


def shorten(word):
    vowels = "AEIOUaeiou"
    new_say = ""
    for i in word:
        if vowels.count(i) == 0:
            new_say = new_say + i
    return new_say

if __name__ == "__main__":
    main()
