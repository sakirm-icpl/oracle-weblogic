# Connect to server
connect('weblogic', 'PocWLS0723$', '3.6.299.170:7001')

# Start Editing
edit()

startEdit()

#Change directory

cd('/Servers/MS1')

# Add key.jks file
cmo.setCustomIdentityKeyStoreFileName('/home/sakir/certificate/Identity.jks')

cmo.setCustomIdentityKeyStoreType('jks')

setEncrypted('CustomIdentityKeyStorePassPhrase', 'CustomIdentityKeyStorePassPhrase_1690203825100', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Config', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Secret')

# Add Trust.jks 

cmo.setCustomTrustKeyStoreFileName('/home/sakir/certificate/Trust.jks')

cmo.setCustomTrustKeyStoreType('jks')

setEncrypted('CustomTrustKeyStorePassPhrase', 'CustomTrustKeyStorePassPhrase_1690203825586', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Config', 'C:/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain/Script1690203742496Secret')

save()

activate()

startEdit()

cd('/Servers/MS1/SSL/MS1')

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
