import prettytable

inputFile = open('ExamInputFile.txt').readlines()
outputFile = prettytable.PrettyTable(["Student ID", "Questions Right", "Questions Wrong", "Total Answered", "Answered Correct Pct", "Questions Omitted", "More Right or Wrong", "Score"])

for i in inputFile:
    if i != '-1':
        inputFileArray = i.split()
        studentId = int(inputFileArray[0])
        right = int(inputFileArray[1])
        wrong = int(inputFileArray[2])
        totalAnswered = right + wrong
        omitted = 50 - (right + wrong)
        score = right * 2
        answeredCorrectperct = (right / totalAnswered) * 100
        if right > wrong:
            moreRightOrWrong = "More Right than Wrong"
        if right == wrong:
            moreRightOrWrong = "Right and Wrong are Equal"
        if right < wrong:
            moreRightOrWrong = "More Wrong than Write"
        if omitted < 10:
            omitStr = "Less than 10 Omitted"
        elif omitted == 10:
            omitStr = "10 Omitted"
        elif omitted > 10:
            omitStr = "More than 10 Omitted"
        outputFile.add_row([studentId, right, wrong, totalAnswered, answeredCorrectperct, omitStr, moreRightOrWrong, score])

print(outputFile)
outputFileTxt = open('ExamOutputFile.txt', "w")
outputFileTxt.write(str(outputFile))