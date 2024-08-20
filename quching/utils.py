
def ms_to_str(ms):
    val = ms
    hours = val // 3600000
    val -= hours * 3600000
    mins = val // 60000
    val -= mins * 60000
    secs = val // 1000
    if hours > 0:
        return F"{hours:02}:{mins:02}:{secs:02}"
    else:
        return F"{mins:02}:{secs:02}"
