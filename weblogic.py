connect('weblogic', 'PocWLS0723$', '3.6.299.170:7001')

edit()

startEdit()

cd('/Servers/MS1')
cmo.setKeyStores('CustomIdentityAndCustomTrust')

save()
activate()

startEdit()
cmo.setCustomIdentityKeyStoreFileName('/home/sakir/certificate/Identity.jks')
cmo.setCustomIdentityKeyStoreType('jks')
setEncrypted('CustomIdentityKeyStorePassPhrase', 'CustomIdentityKeyStorePassPhrase_1690353949671', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Config', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Secret')
cmo.setCustomTrustKeyStoreFileName('/home/sakir/certificate/Trust.jks')
cmo.setCustomTrustKeyStoreType('jks')
setEncrypted('CustomTrustKeyStorePassPhrase', 'CustomTrustKeyStorePassPhrase_1690353949749', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Config', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Secret')

save()
activate()

startEdit()

cd('/Servers/MS1/SSL/MS1')
cmo.setServerPrivateKeyAlias('new')
setEncrypted('ServerPrivateKeyPassPhrase', 'ServerPrivateKeyPassPhrase_1690353991279', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Config', '/home/pavan/fmw/domains/poc_domain/Script1690353856071Secret')

save()
activate()

startEdit()
cmo.setExportKeyLifespan(500)
cmo.setUseServerCerts(false)
cmo.setSSLRejectionLoggingEnabled(true)
cmo.setAllowUnencryptedNullCipher(false)
cmo.setInboundCertificateValidation('BuiltinSSLValidationOnly')
cmo.setOutboundCertificateValidation('BuiltinSSLValidationOnly')
cmo.setHostnameVerificationIgnored(true)
cmo.setHostnameVerifier(None)
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)

save()
activate()
startEdit()
cmo.setEnabled(true)

save ()
activate()

disconnect()

exit()

