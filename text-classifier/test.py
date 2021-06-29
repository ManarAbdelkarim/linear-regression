import urllib
import urllib.request



# def read_text():
#     quotes = open("text_for_test.txt")
#     content_of_file = quotes.read()
#     print(content_of_file)
#     quotes.close()
#     check_profanity(content_of_file)

# def check_profanity(text_to_check):

#      output1 = "Mama always said, life is like a box of chocolates. You never know what you are going to get. (Forrest Gump) \nYou cant hand le the truth.(A Few Good Men) "
#      with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+"shit") as connection:
#         output = connection.read()

#      if "true" in output:
#         print("true profanity")
#      elif "false" in output:
#         print("false profanity")
#      else:
#         print("could not scan file")

# read_text()

# import urllib
def read_text():
    quotes=open(r"text_for_test.txt")
    connects_file=quotes.read()
    print (connects_file)
    check_profanity(connects_file)

def check_profanity(text_to_check):
    # url = "http://www.wdylike.appspot.com/?q="
    text = text_to_check.replace(" ","%20")
    print(text)
    connection=urllib.request.urlopen(f"http://www.wdylike.appspot.com/?q={text}")
    output=connection.read()
    print (output)
    connection.close()
    print("done")


read_text()
    