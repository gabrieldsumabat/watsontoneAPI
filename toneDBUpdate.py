from ApiToDB import dbStorage
##from email import emailExtract


if __name__=="__main__":
    pmr="PMR123"
    text=r"Hello's, World"	
    dateTime="03072017"
    text=text.replace("'","''")

    dbStorage(pmr, text, dateTime)
