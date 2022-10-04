import json

def c(status):
    if status == True:

        with open("package.json") as f:
            pk = json.load(f)


        ###### PRINTING CURRENT PACKAGE.JSON INFORMATIONS
        for package_alpha in pk['package_alpha']:
            print(package_alpha['id'])
            print(package_alpha['version'])
            print(package_alpha['name'])
            print(package_alpha['language'])
        ################################################

        ###### VALUES THAT MUST BE IN PACKAGE.JSON AS WELL
        id_ = '04102022'
        version = '0.3'
        name = "alpha"
        language = "python3"
        ##################################################




        ###### CHECKING THOSE VALUES WITH PACKAGE.JSON
        for package_alpha in pk['package_alpha']:
            if package_alpha['id'] == id_:
                print("ID: OK")
            else:
                print("ID: Incorrect")
            if package_alpha['version'] == version:
                print("Version: OK")
            else:
                print("Version: Incorrect")
            if package_alpha['name'] == name:
                print("Module: OK")
            else:
                print("Module: Incorrect")

            if package_alpha['language'] == language:
                print("Language: OK")
            else:
                print("Language: Incorrect")
        ###############################################
    




            

