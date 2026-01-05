# Papers, Please is an indie video game where the player takes on a the role of a border crossing immigration officer in the fictional dystopian Eastern Bloc-like country of Arstotzka in the year 1982. As the officer, the player must review each immigrant and returning citizen's passports and other supporting paperwork against a list of ever-increasing rules using a number of tools and guides, allowing in only those with the proper paperwork, rejecting those without all proper forms, and at times detaining those with falsified information.

# Objective
# Your task is to create a constructor function (or class) and a set of instance methods to perform the tasks of the border checkpoint inspection officer. The methods you will need to create are as follow:

# Method: receiveBulletin
# Each morning you are issued an official bulletin from the Ministry of Admission. This bulletin will provide updates to regulations and procedures and the name of a wanted criminal.

# The bulletin is provided in the form of a string. It may include one or more of the following:

# Updates to the list of nations (comma-separated if more than one) whose citizens may enter (begins empty, before the first bulletin):
# example 1: Allow citizens of Obristan
# example 2: Deny citizens of Kolechia, Republia
# Updates to required documents
# example 1: Foreigners require access permit
# example 2: Citizens of Arstotzka require ID card
# example 3: Workers require work pass
# Updates to required vaccinations
# example 1: Citizens of Antegria, Republia, Obristan require polio vaccination
# example 2: Entrants no longer require tetanus vaccination
# Update to a currently wanted criminal
# example 1: Wanted by the State: Hubert Popovic
# Method: inspect
# Each day, a number of entrants line up outside the checkpoint inspection booth to gain passage into Arstotzka. The inspect method will receive an object representing each entrant's set of identifying documents. This object will contain zero or more properties which represent separate documents. Each property will be a string value. These properties may include the following:

# Applies to all entrants:
# passport
# certificate_of_vaccination
# Applies only to citizens of Arstotzka
# ID_card
# Applies only to foreigners:
# access_permit
# work_pass
# grant_of_asylum
# diplomatic_authorization
# The inspect method will return a result based on whether the entrant passes or fails inspection:

# Conditions for passing inspection

# All required documents are present
# There is no conflicting information across the provided documents
# All documents are current (ie. none have expired) -- a document is considered expired if the expiration date is November 22, 1982 or earlier
# The entrant is not a wanted criminal
# If a certificate_of_vaccination is required and provided, it must list the required vaccination
# A "worker" is a foreigner entrant who has WORK listed as their purpose on their access permit
# If entrant is a foreigner, a grant_of_asylum or diplomatic_authorization are acceptable in lieu of an access_permit. In the case where a diplomatic_authorization is used, it must include Arstotzka as one of the list of nations that can be accessed.
# If the entrant passes inspection, the method should return one of the following string values:

# If the entrant is a citizen of Arstotzka: Glory to Arstotzka.
# If the entrant is a foreigner: Cause no trouble.
# If the entrant fails the inspection due to expired or missing documents, or their certificate_of_vaccination does not include the necessary vaccinations, return Entry denied: with the reason for denial appended.

# Example 1: Entry denied: passport expired.
# Example 2: Entry denied: missing required vaccination.
# Example 3: Entry denied: missing required access permit.
# If the entrant fails the inspection due to mismatching information between documents (causing suspicion of forgery) or if they're a wanted criminal, return Detainment: with the reason for detainment appended.

# If due to information mismatch, include the mismatched item. e.g.Detainment: ID number mismatch.
# If the entrant is a wanted criminal: Detainment: Entrant is a wanted criminal.
# NOTE: One wanted criminal will be specified in each daily bulletin, and must be detained when received for that day only. For example, if an entrant on Day 20 has the same name as a criminal declared on Day 10, they are not to be detained for being a criminal.
# Also, if any of an entrant's identifying documents include the name of that day's wanted criminal (in case of mismatched names across multiple documents), they are assumed to be the wanted criminal.
# In some cases, there may be multiple reasons for denying or detaining an entrant. For this exercise, you will only need to provide one reason.

# If the entrant meets the criteria for both entry denial and detainment, priority goes to detaining.
# For example, if they are missing a required document and are also a wanted criminal, then they should be detained instead of turned away.
# In the case where the entrant has mismatching information and is a wanted criminal, detain for being a wanted criminal.
# Test Example
# bulletin = """Entrants require passport
# Allow citizens of Arstotzka, Obristan"""

# inspector = Inspector()
# inspector.receive_bulletin(bulletin)

# entrant1 = {
#     "passport": """ID#: GC07D-FU8AR
#     NATION: Arstotzka
#     NAME: Guyovich, Russian
#     DOB: 1933.11.28
#     SEX: M
#     ISS: East Grestin
#     EXP: 1983.07.10"""
# }

# inspector.inspect(entrant1) #=> 'Glory to Arstotzka.'
# Additional Notes
# Inputs will always be valid.
# There are a total of 7 countries: Arstotzka, Antegria, Impor, Kolechia, Obristan, Republia, and United Federation.
# Not every single possible case has been listed in this Description; use the test feedback to help you handle all cases.
# The concept of this kata is derived from the video game of the same name, but it is not meant to be a direct representation of the game.

from datetime import date

bulletin_info = {
        "banned" : ["Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"],
        "wanted" : "",
        "Arstotzka" : [],
        "Antegria" : [],
        "Impor" : [],
        "Kolechia" : [],
        "Obristan" : [],
        "Republia" : [],
        "United Federation" : [],
        "workers" : [],
        "vaccines" : []
    }

foreigners = ["Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"]
nations = ["Arstotzka", "Antegria", "Impor", "Kolechia", "Obristan", "Republia", "United Federation"]

def details(document):
        document_details = {}
        for line in document:
            key, value = line.split(" ", 1)
            if key == "NAME:":
                splitted = value.split(", ")
                new_value = splitted[1] + " " + splitted[0]
                value = new_value
            document_details[key] = value
        return document_details

def check_date(document):
    if "EXP:" not in document:
        return True
    start = document.find("EXP:") + 5
    if date(int(document[start:start + 4]), int(document[start + 5:start + 7]), int(document[start + 8:start + 10])) <= date(1982, 11, 22):
            return False
    else:
        return True
    
def check_details(document, passport):
    for detail in document:
        if detail == "EXP:":
            continue
        if detail not in passport:
            continue
        if passport[detail] != document[detail]:
            if detail == "ID#:":
                return "ID number"
            elif detail == "NATION:":
                return "nationality"
            elif detail == "DOB:":
                return "date of birth"
            else:
                return detail[:-1].lower()
    return False

class Inspector:

    def add_requirements(self, point, start, nation):
        requirements = [x.strip() for x in point[start:].split(",")]
        bulletin_info[str(nation)].extend(requirements)

    def del_requirements(self, point, start, nation):
        to_remove = [x.strip() for x in point[start:].split(",")]
        for x in to_remove:
            if x in bulletin_info[str(nation)]:
                bulletin_info[str(nation)].remove(x)

    def receive_bulletin(self, bulletin):

        bulletin_list = bulletin.split("\n")

        for point in bulletin_list:
            if point.startswith("Allow"):
                start = point.find("of") + 3
                allowed = [x.strip() for x in point[start:].split(",")]
                bulletin_info["banned"] = [c for c in bulletin_info["banned"] if c not in allowed]

            elif point.startswith("Deny"):
                start = point.find("of") + 3
                denied = [x.strip() for x in point[start:].split(",")]
                bulletin_info["banned"].extend(denied)

            elif point.startswith("Wanted"):
                start = point.find("State:") + 7
                bulletin_info["wanted"] = point[start:].strip()

            elif "Foreigners require" in point:
                start = point.find("require") + 8
                for nation in foreigners:
                    self.add_requirements(point, start, nation)

            elif "Foreigners no longer require" in point:
                start = point.find("require") + 8
                for nation in foreigners:
                    self.del_requirements(point, start, nation)

            elif "Arstotzka" in point:
                start = point.find("require") + 8
                self.add_requirements(point, start, "Arstotzka")

            elif point.startswith("Workers"):
                start = point.find("require") + 8
                bulletin_info.update({"workers" : point[start:]})

            elif "Entrants no longer require" in point:
                start = point.find("require") + 8
                for nation in nations:
                    self.del_requirements(point, start, nation)
            
            elif "Entrants require" in point:
                start = point.find("require") + 8
                for nation in nations:
                    self.add_requirements(point, start, nation)
            
    def inspect(self, person):

        if not len(person):
            return "Entry denied: missing required passport."

        # check nationality and name
        nationality = None
        for name in person:
            if person[name].find("NAME:") != -1 and name:
                start = person[name].find("NAME:") + 6
                splitted = person[name][start:].split("\n")[0].split(", ")
                person_name = splitted[1] + " " + splitted[0]
            if person[name].find("NATION:") != -1:
                start = person[name].find("NATION:") + 8
                nationality = person[name][start:].split("\n")[0]
                break
        if not nationality:
            nationality = "Arstotzka"

        # wanted
        if person_name == bulletin_info["wanted"]:
            return "Detainment: Entrant is a wanted criminal."
        
        # check docs mismatch
        docs = []
        for name in person:
            docs.append(name)
        if len(person) > 1:
            document1 = details(person[docs[0]].split("\n"))

            for doc in range(1, len(person)):
                document2 = details(person[docs[doc]].split("\n"))
                mismatch = check_details(document1, document2)
                if mismatch != False:
                    return "Detainment: " + mismatch + " mismatch."

        # check docs expiration 
        for doc in person:
            if doc != "passport":
                if not check_date(doc):
                    return "Entry denied: access permit expired."
                    
        # check passport
        if "passport" in bulletin_info[nationality]:
            try:
                person['passport']
            except KeyError:
                return "Entry denied: missing required passport."
            
            # expired passport
            if check_date(person['passport']) == False:
                return "Entry denied: passport expired."
        
        # banned
        if nationality in bulletin_info["banned"]:
            return "Entry denied: citizen of banned nation."
        
        # required docs
        # ID card
        if "ID card" in bulletin_info[nationality] and nationality == "Arstotzka":
            if "ID_card" not in person:
                    return "Entry denied: missing required ID card."
            if not check_date(person["ID_card"]):
                        return "Entry denied: ID card expired."
        
        # access permits
        if "access permit" in bulletin_info[nationality]:
            access_permit = False
            if "access_permit" in person:
                if not check_date(person["access_permit"]):
                    return "Entry denied: access permit expired."
                access_permit = True
            if "diplomatic_authorization" in person:
                start = person["diplomatic_authorization"].find("ACCESS:") + 8
                accesses = person["diplomatic_authorization"][start:].split(", ")
                if "Arstotzka" not in accesses:
                    return "Entry denied: invalid diplomatic authorization."
                access_permit = True
            if "work_pass" in person:
                if not check_date(person["work_pass"]):
                    return "Entry denied: work pass expired."
                access_permit = True
            if "grant_of_asylum" in person:
                if not check_date(person["grant_of_asylum"]):
                    return "Entry denied: grant of asylum expired."
                access_permit = True
            if not access_permit:
                return "Entry denied: missing required access permit."
            
        # vaccination
        for required_doc in bulletin_info[nationality]:
            if required_doc.find("vaccination") != -1:
                if "certificate_of_vaccination" not in person:
                    return "Entry denied: missing required certificate of vaccination."
                start = person["certificate_of_vaccination"].find("VACCINES:") + 10
                vaccines = person["certificate_of_vaccination"][start:].split(", ")
                end = required_doc.find(" vaccination")
                if required_doc[:end] not in vaccines:
                    return "Entry denied: missing required vaccination."
            
        # work permit
        if bulletin_info["workers"] == "work pass" and nationality != "Arstotzka":
            if "access_permit" in person:
                start = person["access_permit"].find("PURPOSE:") + 9
                purpose = person["access_permit"][start:]
                if "WORK" in purpose and "work_pass" not in person:
                    return "Entry denied: missing required work pass."
                
        # PASS
        if nationality == "Arstotzka":
            return "Glory to Arstotzka."
        else:
            return "Cause no trouble."