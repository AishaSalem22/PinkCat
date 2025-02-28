# DeliveryOrder Class
class DeliveryOrder:
    def __init__(self, orderID: str, totalAmount: float, customerID: str, orderDate: str, orderStatus: str):
        # Initialize the attributes of the DeliveryOrder
        self.orderID = orderID
        self.totalAmount = totalAmount
        self.customerID = customerID
        self.orderDate = orderDate
        self.orderStatus = orderStatus

# Method to generate a delivery note
    def generateDeliveryNote(self) -> str:
        # This method would create and return a delivery note
        return f"Delivery Note for Order {self.orderID}"

    # Method to update the order status
    def updateStatus(self, newStatus: str) -> None:
        self.orderStatus = newStatus

# Getter and setter methods for each attribute
    def get_orderID(self):
        return self.orderID

    def set_orderID(self, orderID):
        self.orderID = orderID

    def get_totalAmount(self):
        return self.totalAmount

    def set_totalAmount(self, amount):
        self.totalAmount = amount

    def get_customerID(self):
        return self.customerID

    def set_customerID(self, customerID):
        self.customerID = customerID

    def get_orderDate(self):
        return self.orderDate

    def set_orderDate(self, orderDate):
        self.orderDate = orderDate

    def get_orderStatus(self):
        return self.orderStatus

    def set_orderStatus(self, status):
        self.orderStatus = status

    # Method to display order information
    def displayDeliveryOrder(self):
        print(f"Order ID: {self.orderID}")
        print(f"Total Amount: ${self.totalAmount}")
        print(f"Customer ID: {self.customerID}")
        print(f"Order Date: {self.orderDate}")
        print(f"Order Status: {self.orderStatus}")

# Creating two DeliveryOrder objects
order1 = DeliveryOrder("DO001", 100.50, "MIST001", "2025-02-25", "Pending")
order2 = DeliveryOrder("DO002", 75.25, "MIS002", "2025-02-25", "In Transit")

# Display the order information
print("Order 1 details:")
order1.displayDeliveryOrder()
print("\nOrder 2 details:")
order2.displayDeliveryOrder()


# Payment Class
class Payment:
    def __init__(self, paymentID, orderID, paymentMethod, paymentAmount, paymentDate):
        # Initialize the attributes of the Payment
        self.paymentID = paymentID
        self.orderID = orderID
        self.paymentMethod = paymentMethod
        self.paymentAmount = paymentAmount
        self.paymentDate = paymentDate

    # Method to process payment
    def processPayment(self):
        # This method would handle payment processing
        return True

    # Method to validate payment
    def validatePayment(self):
        # This method would validate payment details
        return True

    # Getter and setter methods for each attribute
    def get_paymentID(self):
        return self.paymentID

    def set_paymentID(self, paymentID):
        self.paymentID = paymentID

    def get_orderID(self):
        return self.orderID

    def set_orderID(self, orderID):
        self.orderID = orderID

    def get_paymentMethod(self):
        return self.paymentMethod

    def set_paymentMethod(self, method):
        self.paymentMethod = method

    def get_paymentAmount(self):
        return self.paymentAmount

    def set_paymentAmount(self, amount):
        self.paymentAmount = amount

    def get_paymentDate(self):
        return self.paymentDate

    def set_paymentDate(self, paymentDate):
        self.paymentDate = paymentDate

    # Method to display payment information
    def displayPaymentInfo(self):
        print(f"Payment ID: {self.paymentID}")
        print(f"Order ID: {self.orderID}")
        print(f"Payment Method: {self.paymentMethod}")
        print(f"Payment Amount: ${self.paymentAmount}")
        print(f"Payment Date: {self.paymentDate}")

# Create two Payment objects
payment1 = Payment("MIS001", "DO001", "Credit Card", 100.50, "2025-02-25")
payment2 = Payment("MIS002", "DO002", "Tabby", 75.25, "2025-02-25")

# Display the payment information
print("\nPayment 1 details:")
payment1.displayPaymentInfo()
print("\nPayment 2 details:")
payment2.displayPaymentInfo()


# Customer Class
class Customer:
    def __init__(self, customerID, firstName, lastName, contactNumber, emailAddress):
        # Initialize the attributes of the Customer
        self.customerID = customerID
        self.firstName = firstName
        self.lastName = lastName
        self.contactNumber = contactNumber
        self.emailAddress = emailAddress

    # Method to place an order
    def placeOrder(self, orderDetails):
        # This method would create and return a new DeliveryOrder
        return DeliveryOrder(orderDetails['orderID'], orderDetails['totalAmount'], self.customerID, orderDetails['orderDate'], "Pending")

    # Method to track delivery
    def trackDelivery(self, orderID):
        # This method would return the status of an order
        return "In Transit"

    # Getter and setter methods for each attribute
    def get_customerID(self):
        return self.customerID

    def set_customerID(self, customerID):
        self.customerID = customerID

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, name):
        self.firstName = name

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, name):
        self.lastName = name

    def get_contactNumber(self):
        return self.contactNumber

    def set_contactNumber(self, number):
        self.contactNumber = number

    def get_emailAddress(self):
        return self.emailAddress

    def set_emailAddress(self, email):
        self.emailAddress = email

    # Method to display customer information
    def displayCustomerInfo(self):
        print(f"Customer ID: {self.customerID}")
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Contact Number: {self.contactNumber}")
        print(f"Email Address: {self.emailAddress}")

# Create two Customer objects
customer1 = Customer("MIS001", "Afshan", "Parker", "+050000000", "Afshan.parker@zu.ac.ae")
customer2 = Customer("MIS002", "Aisha", "Salem", "+0544058022", "202304302@zu.ac.ae")

# Display the customer information
print("\nCustomer 1 details:")
customer1.displayCustomerInfo()
print("\nCustomer 2 details:")
customer2.displayCustomerInfo()






# Recipient Class
class Recipient:
    def __init__(self, recipientID, firstName, lastName, phoneNumber, emailAddress, address):
        # Initialize the attributes of the Recipient
        self.recipientID = recipientID
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address

    # Method to confirm receipt of a package
    def confirmReceipt(self, orderID):
        # This method would confirm receipt of a package
        return True

    # Getter and setter methods for each attribute
    def get_recipientID(self):
        return self.recipientID

    def set_recipientID(self, recipientID):
        self.recipientID = recipientID

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, firstName):
        self.firstName = firstName

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_phoneNumber(self):
        return self.phoneNumber

    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def get_emailAddress(self):
        return self.emailAddress

    def set_emailAddress(self, emailAddress):
        self.emailAddress = emailAddress

    def get_address(self):
        return self.address

    def set_address(self, newAddress):
        self.address = newAddress

    # Method to display recipient information
    def displayRecipientInfo(self):
        print(f"Recipient ID: {self.recipientID}")
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Email Address: {self.emailAddress}")
        print(f"Address: {self.address}")

# Create two Recipient objects
recipient1 = Recipient("REC001", "Wadha", "Saeed", "+1122334455", "wadha.sa@email.com", "123 Main St, City, Country")
recipient2 = Recipient("REC002", "Aisha", "Salem", "+5544332211", "aisha.w@email.com", "456 Elm St, Town, Country")

# Display the recipient information
print("\nRecipient 1 details:")
recipient1.displayRecipientInfo()
print("\nRecipient 2 details:")
recipient2.displayRecipientInfo()



# System Class
class System:
    def __init__(self, systemID, transactionLog, accountDatabase, securityProtocol):
        # Initialize the attributes of the System
        self.systemID = systemID
        self.transactionLog = transactionLog
        self.accountDatabase = accountDatabase
        self.securityProtocol = securityProtocol

    # Method to verify user
    def verifyUser(self, userID, password):
        # This method would verify user credentials
        return True

    # Method to log a transaction
    def logTransaction(self, orderID, action):
        # This method would log a transaction
        self.transactionLog.append(f"Order {orderID}: {action}")

    # Getter and setter methods for each attribute
    def get_systemID(self):
        return self.systemID

    def set_systemID(self, systemID):
        self.systemID = systemID

    def get_transactionLog(self):
        return self.transactionLog

    def set_transactionLog(self, log):
        self.transactionLog = log

    def get_accountDatabase(self):
        return self.accountDatabase

    def set_accountDatabase(self, database):
        self.accountDatabase = database

    def get_securityProtocol(self):
        return self.securityProtocol

    def set_securityProtocol(self, protocol):
        self.securityProtocol = protocol

    # Method to display system information
    def displaySystemInfo(self):
        print(f"System ID: {self.systemID}")
        print(f"Transaction Log: {self.transactionLog}")
        print(f"Account Database: {self.accountDatabase}")
        print(f"Security Protocol: {self.securityProtocol}")

# Create two System objects
system1 = System("SYS001", [], {"user1": "pass1"}, "AES-256")
system2 = System("SYS002", [], {"user2": "pass2"}, "RSA-2048")

# Display the system information
print("\nSystem 1 details:")
system1.displaySystemInfo()
print("\nSystem 2 details:")
system2.displaySystemInfo()





# DeliveryStaff Class
class DeliveryStaff:
    def __init__(self, staffID, firstName, lastName, contactNumber, vehicleID):
        # Initialize the attributes of the DeliveryStaff
        self.staffID = staffID
        self.firstName = firstName
        self.lastName = lastName
        self.contactNumber = contactNumber
        self.vehicleID = vehicleID

    # Method to update delivery status
    def updateDeliveryStatus(self, orderID, status):
        # This method would update the status of a delivery
        print(f"Updated status of order {orderID} to {status}")

    # Method to assign an order
    def assignOrder(self, orderID):
        # This method would assign an order to the delivery staff
        print(f"Assigned order {orderID} to staff {self.staffID}")

    # Getter and setter methods for each attribute
    def get_staffID(self):
        return self.staffID

    def set_staffID(self, staffID):
        self.staffID = staffID

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, name):
        self.firstName = name

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, name):
        self.lastName = name

    def get_contactNumber(self):
        return self.contactNumber

    def set_contactNumber(self, number):
        self.contactNumber = number

    def get_vehicleID(self):
        return self.vehicleID

    def set_vehicleID(self, vehicleID):
        self.vehicleID = vehicleID

    # Method to display staff information
    def displayStaffInfo(self):
        print(f"Staff ID: {self.staffID}")
        print(f"Name: {self.firstName} {self.lastName}")
        print(f"Contact Number: {self.contactNumber}")
        print(f"Vehicle ID: {self.vehicleID}")

# Create two DeliveryStaff objects
staff1 = DeliveryStaff("DS001", "Ahmed", "Salem", "+1357924680", "VEH001")
staff2 = DeliveryStaff("DS002", "Zayed", "Salem", "+2468013579", "VEH002")

# Display the staff information
print("\nDelivery Staff 1 details:")
staff1.displayStaffInfo()
print("\nDelivery Staff 2 details:")
staff2.displayStaffInfo()