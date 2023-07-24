
# Connect to WebLogic Admin Server
connect('weblogic', 'P@$$w0rd', '172.17.16.49:7001')

# Start an edit session
edit()

startEdit()

# Navigate to the desired MBean location
cd('Servers')
cd('AdminServer')
cd('SSL')
cd('AdminServer')

# Enable SSL
cmo.setEnabled(true)

# Save and activate the changes
save()
activate()

# Disconnect from the WebLogic Admin Server
disconnect()

# Exit the script
exit()
