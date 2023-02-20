class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dot_counter, colon_counter = 0, 0
        for char in queryIP:
            if char == ".":
                dot_counter += 1
            elif char == ":":
                colon_counter += 1
        
        verdict = ""
        if dot_counter == 3 and colon_counter == 0:
            verdict = "potential_ipv4"
        elif dot_counter == 0 and colon_counter == 7:
            verdict = "potential_ipv6"
        else:
            return "Neither"
        
        if verdict == "potential_ipv4":
            arr = queryIP.split(".")
            IPv4 = True
            for segment in arr:
                if IPv4:
                    for i in range(len(segment)):
                        if (i == 0 and segment[i] == "0" and len(segment) > 1) or not segment[i].isdigit():
                            IPv4 = False
                            break
                    # print(segment, IPv4, not segment)
                    if IPv4 and ((not segment) or (segment and int(segment) > 255)):
                        IPv4 = False
                else:
                    break
            if IPv4:
                return "IPv4"
            else:
                return "Neither"
        else:
            arr = queryIP.split(":")
            IPv6 = True
            for segment in arr:
                if len(segment) < 1 or len(segment) > 4:
                    IPv6 = False
                
                if IPv6:
                    for i in range(len(segment)):
                        if not segment[i].isdigit() and (ord(segment[i]) < 65 or ord(segment[i]) > 70) and (ord(segment[i]) < 97 or ord(segment[i]) > 102):
                            IPv6 = False
                            break
                else:
                    break
            
            if IPv6:
                return "IPv6"
            else:
                return "Neither"