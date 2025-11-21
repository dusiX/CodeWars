# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    sList = s.split()
    for x in range(len(sList)):
        sList[x] = sList[x].lower().capitalize()
    if len(s) == 0 or len("#" + "".join(sList)) > 140:
        return False
    else:
        return "#" + "".join(sList)
