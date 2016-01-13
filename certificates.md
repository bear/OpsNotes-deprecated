# Generate a CSR

```
#!/bin/bash
set -ex

NAME="domain"
CN="${NAME}.com"
SAN="www.${NAME}.com"
SUBJ="/O=Your Org Name/C=US/streetAddress=123 Road St/L=San Francisco/ST=California/CN=${CN}/subjectAltName=DNS.1=${SAN}"

openssl req -newkey rsa:2048 -nodes -sha256 -keyout ${NAME}.pkey -out ${NAME}.csr -subj "${SUBJ}"
```

# Check web site's SSL certificate
(thanks Mahmood!)

```
echo yes | openssl s_client -connect circle-artifacts.com:443 2>/dev/null | openssl x509 -noout -dates -subject
```

will generate this:

```
notBefore=Jan  7 20:22:11 2016 GMT
notAfter=Feb  7 22:45:48 2017 GMT
subject= /CN=circle-artifacts.com
```

# Upload certificate to AWS IAM

```
aws iam upload-server-certificate --server-certificate-name unique_name_20160111 --certificate-body file://STAR_domain_com.crt --private-key file://domain.pkey --certificate-chain file://domain_com.ca-bundle
```
