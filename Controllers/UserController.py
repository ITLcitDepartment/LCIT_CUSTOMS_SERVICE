from ldap3 import Server, Connection, ALL,SUBTREE,NTLM
class UserController :
    def login(USER_DATA):
        # Active Directory server IP and credentials
        server_ip = "172.19.240.37"
        dns =  "lcit\\"
        search_filter = "(sAMAccountName="+USER_DATA.AD_USERNAME+")"  # Replace USERNAME with the target username
        base_dn = "DC=lcit,DC=com"  
     
        
        # Create a server object
        server = Server(server_ip, get_info=ALL)

        # Establish a connection using NTLM authentication
        conn = Connection(server, user=dns+USER_DATA.AD_USERNAME, password=USER_DATA.AD_PASSWORD)
        resultAuth = ""

        # Validate credentials
        if conn.bind():
            conn.search(
                search_base=base_dn,
                search_filter=search_filter,
                search_scope=SUBTREE,
                attributes=["mail", "department", "displayName","Title"]  # Specify attributes to retrieve
            )

            resultsProfile = []
            for entry in conn.entries:
                user_info = {
                    "Name": str(entry.displayName),
                    "Email": str(entry.mail),
                    "Department": str(entry.department),
                    "Title": str(entry.title),
                }
                resultsProfile.append(user_info)


            resultAuth = {"Result" :  {"Status" : "OK", "result" :  "Successfully"}, "ProfileData" : resultsProfile}
        else:
            resultAuth = {"Result" :  {"Status" : "Unauthorized", "result" : conn.result['description']}}

        # Unbind the connection (cleanup)
        conn.unbind()

        return resultAuth