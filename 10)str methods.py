name="!!!!! Pruthviraj yadav !!!!!!!! Pruthviraj yadav"
#1.len()
print(len(name))

#2.upper()
print(name.upper())#convert uppercase

#3.lower()
print(name.lower())#convert lowercase

#4.rstrip()
print(name.rstrip("!"))#rightside ! remove of name

#5.lstrip()
print(name.lstrip("!"))#leftside ! remove of name

#6.replace()
print(name.replace("Pruthviraj yadav","shubham lendve"))

#7.split()
print(name.split(" "))# give a list 

#8.capitalize()
blogHeading="inTROduction tO pyThon "# first letter capital &arrange all   others letter  small letter
print(blogHeading.capitalize())

#9.center()
str1="welcome to python programming "
print(len(str1))#string length
print(len(str1.center(50)))#string+space(30+20=50)
print(str1.center(50))# 50 is space to text adding in center

#10.count()
print(name.count("Pruthviraj"))# count words to repeat in string

#11.endswitch()
print(name.endswith("yadav"))#sting end kise ho rhi hai btata hai t/f
print(str1.endswith("to",4,10))


#12.find()
str2="his  name is dan .is honest man"
print(str2.find("is"))#first akruns(pahla word) uska index return and return -1 to word is not find

#13.index() same as find()
# but if the element is present then it will raise an error instead returning only integer value
print(str2.index("is"))

#14.isinum()-return alphanumeric char(A-Z,a-z,0-9)
# or return (True False).
str3="welcomeToTheConsole"
print(str3.isalnum())

#15.isalpha()
# check for alphabetic character
# only i.e A-Za-z. Return True else false
print(str3.isalpha())

#16.islower()
str4="hello world"
print(str4.islower())

#isprintable()all the value given string printable otherwise return false
print(str4.isprintable())
# str4="hello world\n"-return false because \n is not printable

# 17.isspace()-true only if the string contains whitespacen else return false
str5="           "#using spacebar
print(str5.isspace())
str6="              "#using tab
print(str6.isspace())


#18.istitle()-return true only if first letter is capital all string
str7="World  Health Organization"
print(str7.istitle())

str8="To kill a Mocking bird"
print(str8.istitle())

# 19.startswith()-#sting start kha se ho rhi hai btata hai t/f
str9="Python is Interpretered"
print(str9.startswith("Python"))

#21.swapcase()-convert lower to upper
print(str9.swapcase())

#22.title()-first char capital
print(str2.title())