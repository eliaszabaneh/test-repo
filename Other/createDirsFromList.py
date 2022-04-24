import os


def main():
    # Get the list of directories to create
    # dirList = input("Enter a list of directories to create (separated by spaces): ").split()
    dirList = ["Supplier Information", "Supplier Profile", "Commercial Register", "ISO Certificate",
               "Manufacturer profile", "Authorization letter", "Manufacturer’s Authorization Letter to Supplier",
               "Supplier’s Authorization Letter to IDC", "Datasheets of the Product",
               "Bill of Material", "Datasheets for Proposed Items", "Country of Origin Certificate",
               "Recent Test Certificates", "Previous Project Approvals", "QCDD Certificate", "Warranty Letter",
               "Sample Photo", "Physical Sample"]
    homepath = "C:\\Users\\user\\Desktop\\FOR IDC"
    for dir in dirList:
        try:
            path = os.path.join(homepath, dir)
            os.mkdir(path)
        except FileExistsError:
            print("Directory '% s' already exists" % dir)
            pass
        except Exception as e:
            print(e)
            pass
        else:
            print("Directory '% s' created" % path)
        finally:
            # print('next')
            pass



if __name__ == '__main__':
    main()
