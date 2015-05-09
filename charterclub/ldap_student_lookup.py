import ldap
import models
import re

# As follows is the expected return from an ldap query.
# The return format is a dictionary:
# first variable is key, second is value

# dn: uid=jwhitton,o=princeton university,c=us
# cn: Jeremy D. Whitton
# sn: Whitton
# objectClass: inetorgperson
# objectClass: organizationalPerson
# objectClass: person
# objectClass: top
# objectClass: puPerson
# objectClass: nsMessagingServerUser
# objectClass: inetUser
# objectClass: ipUser
# objectClass: inetMailUser
# objectClass: inetLocalMailRecipient
# objectClass: nsManagedPerson
# objectClass: userPresenceProfile
# objectClass: oblixorgperson
# objectClass: oblixPersonPwdPolicy
# objectClass: eduPerson
# objectClass: posixAccount
# givenName: Jeremy
# uid: jwhitton
# displayName: Jeremy D. Whitton
# ou: Undergraduate Class of 2016
# mail: jwhitton@princeton.edu
# pudisplayname: Whitton, Jeremy D.
# eduPersonPrincipalName: jwhitton@princeton.edu
# pustatus: undergraduate
# puclassyear: 2016
# eduPersonPrimaryAffiliation: student
# universityid: 123456789
# eduPersonEntitlement: urn:mace:dir:entitlement:common-lib-terms
# purescollege: Forbes
# eduPersonAffiliation: member
# eduPersonAffiliation: student
# loginShell: /bin/bash
# puhomedepartmentnumber: 54604

# perform an ldap lookup with a query of the form
# "var1=query1,var2=query2,var3=query3,..."
# returns a list of dictionaries, where each dictionary is a 
def ldap_lookup(query):
    # establish ldap connection
    princetonldap = ldap.initialize("ldap://ldap.princeton.edu")

    # perform query
    matches = princetonldap.search_s("o=Princeton University,c=US",
                                     ldap.SCOPE_SUBTREE, query)

    # format return value of query
    students = []
    for match in matches:
        dn, student = match
        students.append(student)

    return students

# form a Member instance given a netid
def get_student_info(netid):
    # scrub non-alphanumeric characters from lookup
    netid = re.sub(r"\W+", "", netid)

    # assume there will only be one student returned
    attributes = ldap_lookup("uid=" + netid)[0]
    student = models.Student(netid = attributes["uid"][0],
                      first_name = attributes["givenName"][0],
                             last_name = attributes["sn"][0])
    if "puclassyear" in attributes:
        student.year = int(attributes["puclassyear"][0])

    return student
