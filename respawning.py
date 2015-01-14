from collections import defaultdict
import sqlite3

def get_id_values(DB):
    """
    Grab the identifying cookie values for this specific database
    """
    # Load the database
    con = sqlite3.connect(DB)
    cur = con.cursor()

    id_cookies = defaultdict(set)
    # Extract identifying value strings for this db
    cur.execute("SELECT domain, name, value FROM http_cookies WHERE http_type = 'response'")
    for domain, name, value in cur.fetchall():
        id_cookies[(domain,name)].add(value)
        
        # Look for potential nested cookies
        if "=" in value:
            for delimiter in ["&", ":"]:
                for part in value.split(delimiter):
                    params = part.split("=")

                    if (len(params) == 2 and name + "#" + params[0] in id_cookies[domain]
                            and params[0] != '' and params[1] != ''):
                        id_cookies[(domain,name + '#' + params[0])].add(params[1])
    con.close()
    
    return id_cookies

DB1 = 'verizon_u1_d1_m1.sqlite' #XUIDH_1
DB2 = 'verizon_u1_d1_m2.sqlite' #XUIDH_1
DB3 = 'verizon_no_u_d1_m3.sqlite' #NO XUIDH
DB4 = 'verizon_u1_d2_m1.sqlite' #XUIDH_1 new day
DB5 = 'verizon_u2_d2_m2.sqlite' #XUIDH_2 new day
cookies_1 = get_id_values(DB1)
cookies_2 = get_id_values(DB2)
cookies_3 = get_id_values(DB3)
cookies_4 = get_id_values(DB4)
cookies_5 = get_id_values(DB5)

for key in cookies_1.keys():
    if cookies_2.has_key(key) and cookies_4.has_key(key):
        shared_values = cookies_1[key].intersection(cookies_2[key]).intersection(cookies_4[key])
    if cookies_2.has_key(key):
        shared_values = cookies_1[key].intersection(cookies_2[key])
        if cookies_3.has_key(key):
            shared_values = shared_values.difference(cookies_3[key])
            if cookies_5.has_key(key):
                shared_values = shared_values.difference(cookies_5[key])
                if len(shared_values) > 0:
                    print key
                    print shared_values
                    print "------------------------------------------\n"
