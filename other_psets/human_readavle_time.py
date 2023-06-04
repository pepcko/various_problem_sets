def format_duration(seconds: int) -> str:
    
    if seconds == 0:
        return "now"
    
    result = ""
    time = {}
    if seconds // 31536000 != 0: 
        time["year"] = seconds // 31536000
    if (seconds % 31536000) // 86400 != 0: 
        time["day"] = (seconds % 31536000) // 86400
    if (seconds % 86400) // 3600 != 0: 
        time["hour"] = (seconds % 86400) // 3600
    if (seconds % 3600) // 60 != 0:
        time["minute"] = (seconds % 3600) // 60
    if (seconds % 3600) % 60 != 0: 
        time["second"] = (seconds % 3600) % 60

    time_used = list(time.keys())
    
    for times in time_used:
        value = time.pop(times)
        answer = f"{value} {times}"
        
        if len(time) == 0:
            if value > 1:
                answer += "s"
        elif len(time) == 1:
            if value > 1: 
                answer += "s and " 
            else: 
                answer += " and "
        else:
            if value > 1:
                answer += "s, "
            else:
                answer += ", "
        
        result += answer
    
    return result