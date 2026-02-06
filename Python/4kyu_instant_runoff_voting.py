# Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

# Each voter selects several candidates in order of preference.
# The votes are tallied from the each voter's first choice.
# If the first-place candidate has more than half the total votes, they win.
# Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
# In case of a tie for least, remove all of the tying candidates.
# In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).
# Start over.
# Continue until somebody has more than half the votes; they are the winner.
# Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference. You should return the symbol corresponding to the winning candidate. See the default test for an example!

def runoff(voters):
    numofvoters = len(voters)
    print(voters)
    
    while True:
        candidates = {}
        loosers = []
        
        votes = [voter[0] for voter in voters]
        
        print(voters)

        for candidate in voters[0]:
            candidates.update({
                candidate : votes.count(candidate)
            })
            
        if max(candidates.values()) > numofvoters / 2:
            return max(candidates, key=candidates.get)
            
        minimum = min(candidates.values())

        for candidate in candidates:
            if candidates[candidate] == minimum:
                loosers.append(candidate)
                
        if len(loosers) == len(candidates):
            return None
                    
        for looser in loosers:
            for voter in voters:
                if looser in voter:
                    voter.remove(looser)
            del candidates[looser]