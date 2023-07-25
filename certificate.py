# Connect to server
connect('weblogic', 'P@$$w0rd', '172.17.16.49:7001')

# Start Editing
edit()

startEdit()

#Change directory

cd('/Servers/AdminServer')

# Add key.jks file
cmo.setCustomIdentityKeyStoreFileName('C:\\Oracle\\Middleware\\Oracle_Home\\user_projects\\domains\\base_domain\\certificate\\Identity.jks')

cmo.setCustomIdentityKeyStoreType('jks')

setEncrypted('CustomIdentityKeyStorePassPhrase', 'CustomIdentityKeyStorePassPhrase_1690203825100', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Config', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Secret')

# Add Trust.jks 

cmo.setCustomTrustKeyStoreFileName('C:\\Oracle\\Middleware\\Oracle_Home\\user_projects\\domains\\base_domain\\certificate\\Trust.jks')

cmo.setCustomTrustKeyStoreType('jks')

setEncrypted('CustomTrustKeyStorePassPhrase', 'CustomTrustKeyStorePassPhrase_1690203825586', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Config', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Secret')

save()

activate()

startEdit()

cd('/Servers/AdminServer/SSL/AdminServer')

# Set Alis

cmo.setServerPrivateKeyAlias('new')

setEncrypted('ServerPrivateKeyPassPhrase', 'ServerPrivateKeyPassPhrase_1690203865459', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Config', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Secret')

save()

activate()

startEdit()

cmo.setHostnameVerificationIgnored(true)

cmo.setHostnameVerifier(None)

cmo.setTwoWaySSLEnabled(false)

cmo.setClientCertificateEnforced(false)

save()

activate()

startEdit()

cmo.setEnabled(true)

save()

activate()

disconnect()

exit()
