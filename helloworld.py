# ============================================
# TASK 1 & 2: Create int, float, string and print their types
# ============================================

x = 10        # int (whole number)
y = 10.0      # float (decimal number)
z = "siddharth"  # string (text)

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>


# ============================================
# TASK 3: Variable names starting with _ , alphabet, number
# ============================================

_myvar = "starts with underscore"   # (a) underscore _
myvar = "starts with alphabet"      # (b) alphabet
# 3myvar = "starts with number"     # (c) THIS WILL CAUSE AN ERROR!
                                    # Python does NOT allow variable names starting with a number

print(_myvar)
print(myvar)


# ============================================
# TASK 4: List variables in memory using dir()
# ============================================

print(dir())   # shows all variable names currently in memory


# ============================================
# TASK 5: List objects inside the variable "mystr"
# ============================================

mystr = "DSA"
print(dir(mystr))   # shows all things you can do with a string


# ============================================
# TASK 6: Type casting using float(), int(), str()
# ============================================

# (a) "ten" — the word ten
#
print(str("ten"))     # Works! Output: ten

# (b) "10" — the number 10 written as text
print(float("10"))    # Works! Output: 10.0
print(int("10"))      # Works! Output: 10
print(str("10"))      # Works! Output: 10

# (c) 10.0 — a decimal number
print(float(10.0))    # Works! Output: 10.0
print(int(10.0))      # Works! Output: 10  (drops the decimal)
print(str(10.0))      # Works! Output: 10.0

# (d) 10 — a whole number
print(float(10))      # Works! Output: 10.0
print(int(10))        # Works! Output: 10
print(str(10))        # Works! Output: 10