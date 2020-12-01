import re
def open_file():
   with open('assets/text_file.txt' , 'r+') as file:
       content = file.read()
       print (content)
       return content

       
    
def edit_file(content):
    return re.sub('\{(.*?)\}', '{}', content)



def handle_input():
    user_array = ['Adjective', 'Adjective', 'A First Name','Past Tense Verb','A First Name', 'Adjective', 'Adjective', 'Plural Noun', 'large animal', 'Small Animal', 'A Girl\'s Name', 'Adjective', 'Plural Noun', 'Adjective', 'Plural Noun', 'Number 1-50','First Name\'s', 'Number', 'Plural Noun', 'Number', 'Plural Noun' ]

    answer = []

    

    for i in user_array:
       input_user = input('insert: ' + i + " ")
       answer.append(input_user)
    return answer

def merge(text, answer):
    formatting = text.format(answer[0], answer[1], answer[2],answer[3],answer[4],answer[5],answer[6],answer[7],answer[8],answer[9],answer[10],answer[11],answer[12],answer[13],answer[14],answer[15],answer[16],answer[17],answer[18],answer[19],answer[20])

    return formatting







    


    
          


if __name__ == "__main__":
    openFile = open_file()
    editFile = edit_file(openFile)
    handleInput = handle_input()
    merge = merge(editFile, handleInput)
    print(merge)
    