'''
try:
    #l=[1,2]
    #for i in range(3):
    #    print(l[i])
    p=int(input('enter number'))
except IndexError as e:
    print(e)
except ValueError as v:
    print(v)
except:
    print('any other problem')
print("hello")'''
#------------------------------------------------
'''def f():
    try:
        l=[1,5,6,7]
        i=int(input('enter index'))
        print(l[i])
        return 1
    except:
        print('error')
        return 0
    finally:
        print('always')
x=f()
print(x)'''
#--------------------------------------------
'''n=int(input("enter a integer"))
if(n<5 or n>9):
    raise EOFError('not a valid answer')'''
#-------------------------------------------------
'''try:
    n=int(input('enter index'))
    l=[1,2]
    print(l[n])
except IndexError as i:
    print(i)
else:
    print('correct')'''
#----------------------------------------------------
'''try:
    x=-1
    assert x>0,'x must be +ve'
except AssertionError as e:
    print(e)'''
#-------------------------------------------------------
'''try:
    raise ValueError('Invalid',404)
except ValueError as e:
    print(e.args)
    print(e.args[0])
    print(e.args[1])'''
#--------------------------------------------------------
"""class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email
        self.message = f"Invalid email format: '{self.email}'"
        super().__init__(self.message)

def validate_email(email_address):
    if "@" not in email_address:
        raise InvalidEmailError(email_address)
    print(f"Email '{email_address}' is valid.")

# Using the custom exception
try:
    validate_email("user@example.com")
    validate_email("invalid-email")
except InvalidEmailError as e:
    print(f"Caught a custom error: {e}")
except Exception as e:
    print(f"Caught a generic error: {e}")

# Example with a valid email
try:
    validate_email("test@example.com")
except InvalidEmailError as e:
    print(f"Caught a custom error: {e}")
"""