connect('weblogic','PocWLS0723$','0.0.0.0:7001')
edit()
startEdit()
cd('/Servers/MS1')
cmo.unSet('CustomIdentityKeyStoreFileName')
cmo.unSet('CustomIdentityKeyStoreType')
cmo.unSet('CustomIdentityKeyStorePassPhrase')
cmo.unSet('CustomTrustKeyStoreFileName')
cmo.unSet('CustomTrustKeyStoreType')
cmo.unSet('CustomTrustKeyStorePassPhrase')
save()
activate()
edit()
startEdit()
cd('/Servers/MS1/SSL/MS1')
cmo.unSet('ServerPrivateKeyAlias')
cmo.unSet('ServerPrivateKeyPassPhrase')
save()
activate()
edit()
startEdit()
cmo.setHostnameVerificationIgnored(false)
cmo.setHostnameVerifier('weblogic.security.utils.SSLWLSWildcardHostnameVerifier')
cmo.setTwoWaySSLEnabled(false)
cmo.setClientCertificateEnforced(false)
save()
activate()
edit()
startEdit()
cmo.setEnabled(false)
save()
activate()
disconnect()
exit()
