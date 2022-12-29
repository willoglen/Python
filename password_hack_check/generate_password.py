'''
generate a complex password using upper,lower,numbers and special chars

'''
import random
import array
import password_vunerable

def generate(password_length):
    ''' generates a random password of x length according to value passed in '''
    if password_length is not None and password_length > 0:
        # declare arrays of the character that we need in out password
        # Represented as chars to enable easy string concatenation
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        lower_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                            'z']

        upper_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                            'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                            'Z']

        symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']

        # combines all the character arrays above to form one array
        full_list = digits + upper_chars + lower_chars + symbols

        # randomly select at least one character from each character set above
        rand_digit = random.choice(digits)
        rand_upper = random.choice(upper_chars)
        rand_lower = random.choice(lower_chars)
        rand_symbol = random.choice(symbols)

        # combine the character randomly selected above
        # at this stage, the password contains only 4 characters but
        # we want a x-character password
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


        # now that we are sure we have at least one character from each
        # set of characters, we fill the rest of
        # the password length by selecting randomly from the combined
        # list of character above.
        for x in range(password_length - 4):
            temp_pass = temp_pass + random.choice(full_list)
            # convert temporary password into array and shuffle to
            # prevent it from having a consistent pattern
            # where the beginning of the password is predictable
            temp_pass_list = array.array('u', temp_pass)
            random.shuffle(temp_pass_list)
    
        password = ""
        for x in temp_pass_list:
            password = password + x
            
        # check if vunerable
        # if password_vunerable.check_password(password) is False:
        #     generate(password_length)
        return password
    return ''
