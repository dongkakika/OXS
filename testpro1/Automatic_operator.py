# This is the main controller of the project
import os
import time

while True:
    
    # Here for static crawling with BS
    os.system("Crawler_SW.py")
    os.system("Crawler_JJ.py")
    os.system("Crawler_COM.py")
    os.system("Crawler_JJD.py")
    os.system("Crawler_CBNU.py")

    # Here for dynamic crawling with Selenium
    os.system("Crawler_JT.py")
    os.system("Crawler_JK.py")

    # A few seconds for blocking collisions of the programs
    time.sleep(3)
    
    # This area is for activating DB_handlers to update tables
    os.system("DB_handler_sw.py")
    os.system("DB_handler_jj.py")
    os.system("DB_handler_com.py")
    os.system("DB_handler_jjd.py")
    os.system("DB_handler_cbnu.py")
    os.system("DB_handler_jt.py")
    os.system("DB_handler_jk.py")
    
    # After finishing DB update, we should delete all data files
    # because, each crawler writes files continuously
    # But don't worry about DB_handlers.
    # it initializes the tables of DB whenever to use 'INSERT' command
    # so, no redundancy.
    os.system("deleteFile.py")

    # it takes 1800s to work again : 재동작하기 위해 1800초(30분)가 소요
    time.sleep(1800)

    
