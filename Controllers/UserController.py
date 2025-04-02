from ldap3 import Server, Connection, ALL,SUBTREE,NTLM
from Connection.CustomDBConnector import Connect_To_Customs_SQLSRV,close_connection
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
    
    def FetchCustomsUser(USER_DATA):

        conn = Connect_To_Customs_SQLSRV()
        if conn:
            try:
                cursor = conn.cursor()

                query = (
                    f"SELECT * FROM TB_AD_USERS WHERE UName = ?"
                )
                cursor.execute(query,USER_DATA.AD_USERNAME)

                columns = [column[0] for column in cursor.description]
                rows = cursor.fetchall()

                if not rows:
                    return {"status": 404, "message": "Data not found"}

                result_json = [dict(zip(columns, row)) for row in rows]

            except Exception as e:
                return {"status": 500, "message": f"Error: {e}"}
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()            
                    
        return {"status": 200, "data": result_json}