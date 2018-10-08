import datetime
supplier_id=set()
supplier_base =[]
user_base = {}
current_user = ""
invoice_base= []


def fill_user_data():
    for i in xrange(0,10):
        user_base["14-5" + str(i+1)] = 'hansa5' + str(i+1)

"--------------------------suppler_details----------------------------------------"
def verify_id(s_id):
    if s_id.isalnum() and s_id.startswith("sup") :
        if s_id not in supplier_id :
            supplier_id.add(s_id)
            return True

def get_supplier_id():
   return current_user

def get_company_name():
    x= ""
    while len(x) == 0:
        x = raw_input("enter company name :: ")
    return x
def get_address():
    x = ""
    while len(x) == 0:
        x = raw_input("enter address ::  ")
    return x

def get_contact_number():
    option = ""
    while not (option=='y' or option=='n'):
        option = raw_input("would you like to give contact number:: y/n :::: ")
    if option == 'y':
        contact = raw_input("enter contact number :: ")
        return contact
    return None

def get_city():
    return raw_input('enter city')

def add_new_entry_util():
    supplier_detail = {}
    s_id="";company_name="";contact_number=""
    address = "";city= ""
    s_id = get_supplier_id()
    supplier_detail['sup_id'] = s_id

    supplier_detail['sup_company_name'] = get_company_name()

    supplier_detail['sup_address'] = get_address()

    supplier_detail['sup_contact']= get_contact_number()

    supplier_detail['city'] = get_city()

    return supplier_detail

def print_suppler_base():
    print 'current suppliers'
    print "id       company_name    address     contact     city"
    print "------------------------------------------------------"
    for i in supplier_base:
        print i['sup_id'], "  ", i['sup_company_name'], "       ", i['sup_address'], "      ", i['sup_contact'], "     ", i['city']

def supplier_details():
    print_suppler_base()
    option = 1
    option = raw_input("do you want to add supplier entry :: 'y - enter/no - 9' :: ")
    while option != '9':
       supplier_base.append(add_new_entry_util())
       option = raw_input("do you want to add supplier entry :: 'y - enter/no - 9' :: ")
       pass
    print_suppler_base()
"--------------------------login----------------------------------------"
def login():
    login_flag = False
    while not login_flag :
        u_id = raw_input("enter user id :::: ")
        if u_id  in user_base:
            password = raw_input("enter password :::: ")
            if user_base[u_id] == password:
                global current_user
                current_user += u_id
                return True
            return False
    return False


def purchases_invoices_util():
    invoice = []
    tdate = str(datetime.date.today())
    invoice.append(tdate)
    sup_id = current_user
    invoice.append(sup_id)
    invoice_number = int(raw_input("enter invoice number :: "))
    invoice.append(invoice_number)
    goods_code = raw_input("enter goods code :: ")
    invoice.append(goods_code)
    no_of_items = int(raw_input("enter no : of items"))
    invoice.append(no_of_items)
    purchases_unit_rate = int(raw_input("enter purchase unit rate"))
    invoice.append(purchases_unit_rate)
    gross_value = no_of_items*purchases_unit_rate
    invoice.append(gross_value)
    gst =  int(raw_input("gst"))
    invoice.append(gst)
    total_value = gross_value + (gst/100)*gross_value
    invoice.append(total_value)
    sales_unit_rate = -1
    while sales_unit_rate>0:
        sales_unit_rate = int(raw_input("enter sales unit rate > 0 "))
    invoice.append(sales_unit_rate)
    expiry_date = str(datetime.date.today()).split('-')
    expiry_date[2] = str(int(expiry_date[2])+4)
    expiry_date = '-'.join(i for i in expiry_date)
    invoice.append(expiry_date)
    return invoice

def print_invoice_base():
    printlist = ['date','supplier_id','invoice_no','goods_code','no_of_items','purchase_unit_rate',
                 'gross_value','gst','total_value','sales_unit_rate','expiry_date']
    for i in invoice_base:
        for j in range(len(i)):
            print  printlist[j],i[j]

def purchase_invoice():
    option = 1
    while option!=9:
        invoice_base.append(purchases_invoices_util())
        option = int(raw_input("do u want more invoices :: yes - enter/no - 9"))
    print_invoice_base()

if __name__ == "__main__":
     fill_user_data()
     if login():
        supplier_details()
        purchase_invoice()





