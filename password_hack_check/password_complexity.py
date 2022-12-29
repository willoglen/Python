'''
functions to test password meets requirements
'''
import re
    
def check_min_max(min_length, max_length, pwd):
    ''' tests if the supplied password between min and max values'''
    if min_length is not None and max_length is not None and pwd is not None and max_length > min_length:
        if len(pwd) >= int(min_length) and len(pwd) <= int(max_length):
            return True 
    return False

def check_complexity(upper, special, pwd):
    ''' checks the complexity of the supplied password against the supplied flags'''
    result = []
    if upper is not None and special is not None and pwd is not None:
        pattern = re.compile('[A-Z]')
        pattern1 = re.compile('[/^[!@#$%^&*()_+\-=\[\]\{\};\'\:"\\|,.<>\/?]')
        result = [True, 'Pass']
        if upper == 1 and re.search(pattern, pwd) is None:
            result[0] = False
            result[1] = 'Failed Upper Case Requirement'
        if special == 1 and re.search(pattern1, pwd) is None:
            result[0] = False
            result[1] = 'Failed Special Character Requirement'
    else:
        result = [False, 'Arguments must all have a value']
    return result
