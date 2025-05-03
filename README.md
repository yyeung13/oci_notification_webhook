# OCI Notification with WebHook
This repository explains how to use WebHook with OCI Notification Service<br>
<br>
OCI Notification with WebHook is generally easy to implement as long as we watch out for a few items below:<br>
<br>
1. SSL Certificate<br>
<br>
OCI WebHook only allows https instead of http, and you need to have a SSL certificate that can be validated by OCI, which rules out self-signed free certificates. It's recommended to use certificates issued by popular Certificate Authority (CA) for ease of WebHook implementation.<br>
For development and POC, we have chosen to use DuckDNS to setup a free domain for the OCI Compute where WebHook is running, and use CertBot to generate a free certifiate for this domain name.<br>
Also, while using CertBot to generate a certificate, let CertBot use a temporary web server for quick setup of the certificate.<br>
<br>
2. Security List and Firewall<br>
Ensure you have configured Security List in OCI and either disable or configure Firewall in OCI Compute to allow the necessary ports. For the sample webhook code provided, we are using port 5443 and this port should be opened.<br>
<br>
3. JSON Message<br>
OCI Notification is using JSON format, make sure while testing to publish a message, test with a properly formatted JSON message.<br>
<br>
Highlevel steps to configure is as follows:<br>
<br>
Step 1: Get a free/commercial domain for your compute where webhook is running, you can use DuckDNS to get a free one for testing purposes.<br>
<br>
Step 2: Get a free/commercial SSL certificate for your domain. You can use CertBot/Let's Encrypt to do so.<br>
<br>
Step 3: Open the necessary firewall/security list in OCI to allow access to the port where WebHook is running, e.g., 5443<br>
<br>
Step 4: Write a webhook program to use the above SSL certificate and ensure the webhook program can handle auto subscription confirmation from OCI. OCI Notification subscription with WebHook will send a special HTTPS request with conformation header message. The webhook code should be able to detect this and completes the registration automatically. Sample provided in webhook code here.<br>
<br>
Step 5: Configure a OCI Notification Topic<br>
<br>
Step 6: Configure a OCI Ntoficiation subscription under the topic with the custom URL as something like this: https://yyeung.duckdns.org:5443/oci_webhook. You should use your own domain name, your own port number if not 5443, and your own context root (if different from the sample webhook code). Once you submit the request for subscription, you should refresh the subscription page on OCI to see webhook subscription is successful.<br>
<br>
Step 7: Test sending a JSON message as notification and verify from webhook output that you can see the message.<br>
<br>
That's it!<br>
