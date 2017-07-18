from watsonToneAPI import watsonAPI
import sqlite3


def dbStorage(numberPMR, text, dateTime):
    toneValues=watsonAPI(str(text))
    angerValue=toneValues[0][1]
    disgustValue=toneValues[0][2]
    fearValue=toneValues[0][3]
    joyValue=toneValues[0][4]
    sadValue=toneValues[0][5]
    analyticalValue=toneValues[1][1]
    confidentValue=toneValues[1][2]
    tentativeValue=toneValues[1][3]
    openessValue=toneValues[2][1]
    conscientiousnessValue=toneValues[2][2]
    extraversionValue=toneValues[2][3]
    agreeablenessValue=toneValues[2][4]
    emotionalRange=toneValues[2][5]
    
    ##Database Operation
    conn=sqlite3.connect('toneAnalysis.db')
    c=conn.cursor()
    ##Check if PMR record already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+str(numberPMR)+"'")
    checkExists=c.fetchone()
    if checkExists==None:
        ##Create the table if it does not exist
        c.execute("CREATE TABLE "+str(numberPMR)+" (dateTime TEXT, anger REAL NOT NULL, disgust REAL NOT NULL, fear REAL NOT NULL, joy REAL NOT NULL, sad REAL NOT NULL, analytical REAL NOT NULL, confident REAL NOT NULL, tentative REAL NOT NULL, openness REAL NOT NULL, conscientiousness REAL NOT NULL, extraversion REAL NOT NULL, agreeableness REAL NOT NULL, emotionalRange REAL NOT NULL, inputText text NOT NULL);")
    c.execute("INSERT INTO "+str(numberPMR)+" VALUES ("+str(dateTime)+", "+str(angerValue)+", "+str(disgustValue)+", "+str(fearValue)+", "+str(joyValue)+", "+str(sadValue)+", "+str(analyticalValue)+", "+str(confidentValue)+", "+str(tentativeValue)+", "+str(openessValue)+", "+str(conscientiousnessValue)+", "+str(extraversionValue)+", "+str(agreeablenessValue)+", "+str(emotionalRange)+", '"+str(text)+"');")
    ## Delta Table Function
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+str(numberPMR)+"_delta';")
    checkExists=c.fetchone()
    if checkExists==None:
        ##Create the table if it does not exist
        c.execute("CREATE TABLE "+str(numberPMR)+"_delta (number INTEGER, angerDelta REAL, disgustDelta REAL, fearDelta REAL, joyDelta REAL, sadDelta REAL)")
    ##Update Delta Row
    c.execute("SELECT number FROM "+str(numberPMR)+"_delta;")
    checkExists=c.fetchone()
    if checkExists==None:
        n=1
        c.execute("INSERT INTO "+str(numberPMR)+"_delta VALUES ("+str(n)+","+str(angerValue)+","+str(disgustValue)+","+str(fearValue)+","+str(joyValue)+","+str(sadValue)+");")
    else:
        n=int(checkExists[0])+1
        c.execute("SELECT avg(anger) FROM "+str(numberPMR)+";")
        angerDelta=c.fetchone()
        c.execute("SELECT avg(disgust) FROM "+str(numberPMR)+";")
        disgustDelta=c.fetchone()
        c.execute("SELECT avg(fear) FROM "+str(numberPMR)+";")
        fearDelta=c.fetchone()
        c.execute("SELECT avg(joy) FROM "+str(numberPMR)+";")
        joyDelta=c.fetchone()
        c.execute("SELECT avg(sad) FROM "+str(numberPMR)+";")
        sadDelta=c.fetchone()
        c.execute("INSERT INTO "+str(numberPMR)+"_delta VALUES ("+str(n)+","+str(angerDelta[0])+","+str(disgustDelta[0])+","+str(fearDelta[0])+","+str(joyDelta[0])+","+str(sadDelta[0])+");")
    ##Close out operation
    conn.commit()
    conn.close()
    




##Experimental Table
if __name__=="__main__":
    ##PRESETS
    numberPMR="PMR111"
    dateTime=1
    text="A word is dead when it is said, some say. Emily Dickinson"
    ##PRESETS

    toneValues=watsonAPI(str(text))
    print (toneValues)
    angerValue=toneValues[0][1]
    disgustValue=toneValues[0][2]
    fearValue=toneValues[0][3]
    joyValue=toneValues[0][4]
    sadValue=toneValues[0][5]
    analyticalValue=toneValues[1][1]
    confidentValue=toneValues[1][2]
    tentativeValue=toneValues[1][3]
    openessValue=toneValues[2][1]
    conscientiousnessValue=toneValues[2][2]
    extraversionValue=toneValues[2][3]
    agreeablenessValue=toneValues[2][4]
    emotionalRange=toneValues[2][5]
    
    ##Database Operation
    ########### Need to include dateSent and numberPMR
    ##Open operation
    conn=sqlite3.connect('test.db')
    c=conn.cursor()
    ##Check if PMR record already exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+str(numberPMR)+"';")
    checkExists=c.fetchone()
    if checkExists==None:
        ##Create the table if it does not exist
        c.execute("CREATE TABLE "+str(numberPMR)+" (dateTime TEXT, anger REAL NOT NULL, disgust REAL NOT NULL, fear REAL NOT NULL, joy REAL NOT NULL, sad REAL NOT NULL, analytical REAL NOT NULL, confident REAL NOT NULL, tentative REAL NOT NULL, openness REAL NOT NULL, conscientiousness REAL NOT NULL, extraversion REAL NOT NULL, agreeableness REAL NOT NULL, emotionalRange REAL NOT NULL, inputText text NOT NULL);")
    ##Insert new record
    c.execute("INSERT INTO "+str(numberPMR)+" VALUES ("+str(dateTime)+", "+str(angerValue)+", "+str(disgustValue)+", "+str(fearValue)+", "+str(joyValue)+", "+str(sadValue)+", "+str(analyticalValue)+", "+str(confidentValue)+", "+str(tentativeValue)+", "+str(openessValue)+", "+str(conscientiousnessValue)+", "+str(extraversionValue)+", "+str(agreeablenessValue)+", "+str(emotionalRange)+", '"+str(text)+"');")
    ##Verify
    c.execute("SELECT * from "+str(numberPMR)+";")
    print(c.fetchall())
	
	##Add the Delta Analysis Table tracking the change in mood over the emails
	##This keeps all the data and analysis seperate 
	
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+str(numberPMR)+"_delta';")
    checkExists=c.fetchone()
    if checkExists==None:
        ##Create the table if it does not exist
        c.execute("CREATE TABLE "+str(numberPMR)+"_delta (number INTEGER, angerDelta REAL, disgustDelta REAL, fearDelta REAL, joyDelta REAL, sadDelta REAL)")
    ##Update Row
    c.execute("SELECT number FROM "+str(numberPMR)+"_delta;")
    checkExists=c.fetchone()
    if checkExists==None:
        n=1
        c.execute("INSERT INTO "+str(numberPMR)+"_delta VALUES ("+str(n)+","+str(angerValue)+","+str(disgustValue)+","+str(fearValue)+","+str(joyValue)+","+str(sadValue)+");")
    else:
        print(type(checkExists))
        n=int(checkExists[0])+1
        c.execute("SELECT avg(anger) FROM "+str(numberPMR)+";")
        angerDelta=c.fetchone()
        c.execute("SELECT avg(disgust) FROM "+str(numberPMR)+";")
        disgustDelta=c.fetchone()
        c.execute("SELECT avg(fear) FROM "+str(numberPMR)+";")
        fearDelta=c.fetchone()
        c.execute("SELECT avg(joy) FROM "+str(numberPMR)+";")
        joyDelta=c.fetchone()
        c.execute("SELECT avg(sad) FROM "+str(numberPMR)+";")
        sadDelta=c.fetchone()
        #print(type(angerDelta))
        #print(str(angerDelta[0]))
        c.execute("INSERT INTO "+str(numberPMR)+"_delta VALUES ("+str(n)+","+str(angerDelta[0])+","+str(disgustDelta[0])+","+str(fearDelta[0])+","+str(joyDelta[0])+","+str(sadDelta[0])+");")
    ##Close out operation
    c.execute("SELECT * from "+str(numberPMR)+"_delta;")
    print(c.fetchall())	
    conn.commit()
    conn.close()
    
    
    
